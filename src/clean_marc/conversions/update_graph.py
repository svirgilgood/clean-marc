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
    SIXHUNDERDTEN_CODES,
    EIGHTHUNDRED_CODES,
    EIGHTHUNDREDTEN_CODES,
    SEVENHUNDREDTEN_CODES,
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
        case "610": value_dict = SIXHUNDERDTEN_CODES
        case "700": value_dict = SEVENHUNDRED_CODES
        case "710": value_dict = SEVENHUNDREDTEN_CODES
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
        for original_iri in agent_row.ari.split(";"):
            agent_graph.add(
                (agent_iri, RDFS.seeAlso, URIRef(original_iri))
            )
        agent_graph.add(
            (agent_iri, RDFS.label, Literal(label, datatype=XSD.string))
        )
        bnode = BNode()
        agent_graph.add((agent_iri, HAS_MARC_FIELD, bnode))
        agent_graph.add((bnode, RDF.type, CMO.MarcField))
        agent_graph.add((bnode, CMO.fieldNumber, Literal(
            agent_row.marcfield, datatype=XSD.string)))
        agent_graph.add((bnode, CMO.firstIndicator, Literal(
            agent_row.firstIndicator, datatype=XSD.string)))
        agent_graph.add((bnode, CMO.secondIndicator, Literal(
            agent_row.secondIndicator, datatype=XSD.string)))
        agent_graph.add((bnode, RDF.value, Literal(agent_row.marcKey)))
        value_dict = return_value_dict(
            agent_row.marcfield.strip(), agent_row.marcKey)
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


def update_graph(graph: Graph) -> Graph:
    # pre clean up queries
    # these queries should be run before the clean up scripts
    for sparql_update in (update_dir/"pre").glob("*.ru"):
        graph.query(sparql_update)
    graph = clean_agents(graph)

    # post clean up scripts
    # these are scripts for running after running different functions
    for sparql_update in (update_dir/"post").glob("*.ru"):
        graph.query(sparql_update)

    return graph
