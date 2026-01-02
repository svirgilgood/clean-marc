"""
The conversion scripts take a RDF Graph
and run update queries and cleaning functions to make
the reports much cleaner.
"""

from rdflib import Graph, URIRef, BNode, Literal, RDF, RDFS, XSD, Namespace
from pathlib import Path
import hashlib

from ..marc.marc_data import (
    ONEHUNDRED_CODES,
    ONEHUNDREDTEN_CODES,
    SIXHUNDRED_CODES,
    SIXHUNDREDTEN_CODES,
    SIXHUNDREDELEVEN_CODES,
    EIGHTHUNDRED_CODES,
    EIGHTHUNDREDTEN_CODES,
    SEVENHUNDREDTEN_CODES,
    SEVENHUNDREDELEVEN_CODES,
    SEVENHUNDRED_CODES,
)

update_dir = Path(__file__).parent
with open(update_dir / "fetch_agents.rq", "r") as fa_proc:
    FETCH_AGENTS_QUERY = fa_proc.read()

BASE_NAMESPACE = "http://svirgilgood.github.io/clean_marc/"
DATA_NAMESPACE = BASE_NAMESPACE + "data/"
ONTO_NAMESPACE = BASE_NAMESPACE + "onto/"

CMO = Namespace(ONTO_NAMESPACE)
CMD = Namespace(DATA_NAMESPACE)
CMT = Namespace(BASE_NAMESPACE + "taxonomy/")
HAS_MARC_FIELD = URIRef(ONTO_NAMESPACE + "hasMarcField")

BF = Namespace("http://id.loc.gov/ontologies/bibframe/")


def create_data_iri(
        label: str, datatype="Agent", namespace=DATA_NAMESPACE
) -> URIRef:
    base = f"{namespace}_{datatype}_"
    return URIRef(base + hashlib.sha256(str.encode(label)).hexdigest()[:18])


def return_value_dict(field: str, marc: str):
    match field:
        case "100": value_dict = ONEHUNDRED_CODES
        case "110": value_dict = ONEHUNDREDTEN_CODES
        case "600": value_dict = SIXHUNDRED_CODES
        case "610": value_dict = SIXHUNDREDTEN_CODES
        case "611": value_dict = SIXHUNDREDELEVEN_CODES
        case "700": value_dict = SEVENHUNDRED_CODES
        case "710": value_dict = SEVENHUNDREDTEN_CODES
        case "711": value_dict = SEVENHUNDREDELEVEN_CODES
        case "800": value_dict = EIGHTHUNDRED_CODES
        case "810": value_dict = EIGHTHUNDREDTEN_CODES
        case _:
            print(f"\033[31mField not found!!! {field}!\033[0m")
            print(f"marc code '{marc}'")
            return {}
    # print(value_dict)
    return value_dict


def create_contribution_link(work: URIRef, agent: URIRef, graph: Graph):
    contribution_bn = BNode()
    graph.add((work, BF.contribution, contribution_bn))
    graph.add((contribution_bn, BF.agent, agent))


def clean_agents(graph: Graph) -> Graph:
    """
    Find all of the agents,
    * make sure the same names are aligned under a single URI
    * make sure that the predicates linking Agents to items are correct
    * Simplify all of the subfield codes in a way that makes sense
    * Create a model that accounts for the codes
    """

    retrieve_agents = graph.query(FETCH_AGENTS_QUERY)
    agent_graph = Graph()
    agent_graph.bind("cmo", CMO)
    agent_graph.bind("cmd", CMD)
    agent_graph.bind("cmt", CMT)
    for agent_row in retrieve_agents:
        label = agent_row.label
        agent_iri = create_data_iri(label)
        agent_graph.add((agent_iri, RDF.type, CMO.Agent))
        work_iris = [URIRef(iri) for iri in agent_row.workUris.split(";")]

        for original_iri in agent_row.ari.split(";"):
            agent_graph.add(
                (agent_iri, RDFS.seeAlso, URIRef(original_iri))
            )
        agent_graph.add(
            (agent_iri, RDFS.label, Literal(label, datatype=XSD.string))
        )
        bnode = BNode()
        """Creates triples with approximate shape
        <agent_iri>
            a cmo:Organization ;
            cmo:hasMarcField [
                a cmo:MarcField ;
                cmo:fieldNumber "710" ;
                cmo:firstIndicator "1" ;
                cmo:secondIndicator "2" ;
                cmo:hasPart [
                    a cmo:SubField ;
                    cmo:hasEntry "Form Subheading (R)" ;
                    cmo:hasValue "Manuscript" ;
                    cmo:hasCode "k" ;
                    cmo:hasCategory cmt:_SFCat_Subtitle ;
                ]
            ] ;
        """
        agent_graph.add((agent_iri, HAS_MARC_FIELD, bnode))
        agent_graph.add((bnode, RDF.type, CMO.MarcField))
        agent_graph.add((bnode, CMO.fieldNumber, Literal(
            agent_row.marcfield, datatype=XSD.string)))
        # for work_iri in work_iris:
        #    agent_graph.add(
        #        (work_iri, URIRef(ONTO_NAMESPACE + agent_row.marcfield), agent_iri))
        agent_graph.add((bnode, CMO.firstIndicator, Literal(
            agent_row.firstIndicator, datatype=XSD.string)))
        agent_graph.add((bnode, CMO.secondIndicator, Literal(
            agent_row.secondIndicator, datatype=XSD.string)))
        agent_graph.add((bnode, RDF.value, Literal(agent_row.marcKey)))
        for work_iri in work_iris:
            agent_graph.add((bnode, CMO.relatedToWork, work_iri))
        value_dict = return_value_dict(
            agent_row.marcfield.strip(), agent_row.marcKey)
        if not value_dict:
            continue
        agent_graph.add((agent_iri, RDF.type, value_dict["class"]))
        # print("marc key: ", agent_row.marcKey)
        for subfield in agent_row.marcKey[5:].split("$"):
            if subfield == "":
                continue
            subfield_node = BNode()
            subfield_code = subfield[0]
            subfield_key = value_dict["subfield-codes"][subfield_code]["value"]
            subfield_value = subfield[1:].strip()
            subfield_category = value_dict["subfield-codes"][subfield_code]["term"]
            agent_graph.add((bnode, CMO.hasPart, subfield_node))
            agent_graph.add((subfield_node, RDF.type, CMO.SubField))
            agent_graph.add(
                (subfield_node, CMO.hasEntry, Literal(subfield_key)))
            agent_graph.add(
                (subfield_node, CMO.hasValue, Literal(subfield_value)))
            agent_graph.add(
                (subfield_node, CMO.hasCode, Literal(subfield_code)))
            agent_graph.add(
                (subfield_node, CMO.hasCategory, subfield_category)
            )

    # print(agent_graph.serialize(format="turtle"))
    return graph + agent_graph


def run_clean_scripts(dire: str, graph: Graph) -> Graph:
    """
    These update queries and functions are intended to be run
    before the reasoner
    """
    for sparql_update in (update_dir/dire).glob("*.ru"):
        with open(sparql_update, "r") as qfp:
            update_query = qfp.read()
            # print("\nCLEAN UP SCRIPTS\n\n", update_query)
            graph.update(update_query)
    return graph


def pre_reasoner_scripts(graph: Graph) -> Graph:
    """
    Pre-reasoner scripts are run before the OWL reasonerL
    """
    graph = run_clean_scripts("pre", graph)
    graph = clean_agents(graph)
    """
    Some of the Bibframe from Marc Records use spaces
    in the IRIs. So far, these seem to only be IDs (especially
    call numbers), but only used as objects.
    This will fix these objects
    """
    for object_uri in graph.objects():
        obj = object_uri.encode().decode()
        if type(object_uri) is not URIRef:
            continue
        # if type(object) is not URIRef or obj.find(" ") > -1:
        if obj.find(" ") <= -1:
            continue
        print("object", obj)
        obj = obj.replace(" ", "%20")
        new_obj_uri = URIRef(obj)
        for subj, pred, _ in graph.triples((None, None, object_uri)):
            graph.remove((subj, pred, object_uri))
            graph.add((subj, pred, new_obj_uri))

    return graph


def post_reasoner_scripts(graph: Graph) -> Graph:
    """
    These update queries and functions will run
    after the reasoner
    """
    print("Running Post Scripts")
    return run_clean_scripts("post", graph)
