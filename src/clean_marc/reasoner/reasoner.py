import owlrl
import time

from rdflib import Graph, URIRef, BNode, RDF, Literal, OWL


def remove_blank_classes(graph: Graph, subject: URIRef):
    for obj in graph.objects(subject, None):
        if type(obj) is BNode:
            remove_blank_classes(graph, obj)
    graph.remove((subject, None, None))


def instantiate_inferred_triples(graph: Graph) -> Graph:
    """
    """

    print("Running Owl Reasoner")
    start = time.time()
    owlrl.DeductiveClosure(
        owlrl.OWLRL_Extension,
        rdfs_closure=True,
        axiomatic_triples=True,
        datatype_axioms=True,
        improved_datatypes=True).expand(graph)
    end = time.time()
    print(f"Reasoner completed in {end - start}")

    print("Cleaning up Blank Node Classes")
    graph.remove((None, OWL.sameAs, None))
    for owl_class in graph.objects(None, RDF.type):
        if type(owl_class) is BNode:
            remove_blank_classes(graph, owl_class)

    print("Removing Literal Subjects")
    for subject in graph.subjects():
        if type(subject) is Literal:
            graph.remove((subject, None, None))

    return graph
