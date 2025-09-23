import owlrl
import time
import reasonable

from rdflib import Graph, URIRef, BNode, RDF, Literal, OWL


def run_owlrl(graph: Graph) -> Graph:
    """
    This calls the pure python implementation of of the OWL-RL
    reasoner. This is much slower, but may work to catch some
    examples or a double check on the reasoning engine.
    """
    print("Running Owlrl Reasoner")
    start = time.time()
    owlrl.DeductiveClosure(
        owlrl.OWLRL_Extension,
        rdfs_closure=True,
        axiomatic_triples=True,
        datatype_axioms=True,
        improved_datatypes=True).expand(graph)
    end = time.time()
    print(f"Reasoner completed in {end - start}")
    return graph


def run_reasonable(graph: Graph) -> Graph:
    """
    This uses the rust reasoner "reasonable".
    The python bindings make this a convenient reaosner.
    """
    print("Running Reasonable Reasoner")
    start = time.time()
    r = reasonable.PyReasoner()
    r.from_graph(graph)
    end = time.time()
    for triple in r.reason():
        graph.add(triple)

    print(f"Reasoner completed in {end - start}")

    return graph


def instantiate_inferred_triples(graph: Graph, py_reasoner=False) -> Graph:
    """
    Because the reasoners infer a lot of stuff we don't need to instantiate,
    this function grabs only the classes for items we are interested in.
    There might be other uses, but belonging to specific classes is the most
    important one.
    """
    inference_graph = Graph()
    print("copying graph for inference")
    inference_graph.parse(data=graph.serialize(
        format="turtle"), format="turtle")

    if py_reasoner:
        inference_graph = run_owlrl(inference_graph)  # 543.9337818622589
    else:
        inference_graph = run_reasonable(inference_graph)  # 1.3564

    print("Run Query to find Classes")
    for triple in inference_graph.query(
        """PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        CONSTRUCT { ?s a ?type .}
        WHERE {
        ?s a ?type .
        FILTER(!isBlank(?s))
        FILTER(!isBlank(?type))
        FILTER(!isLiteral(?s))
        FILTER(?type != owl:Thing)
        FILTER(?type != rdfs:Resource)
        }"""
    ):
        graph.add(triple)

    return graph
