import argparse
from rdflib import Graph
from pathlib import Path
from pandas import DataFrame
import os

import pandas as pd
from io import StringIO
from typing import Dict, Callable
import lxml.etree as etree

from .oclc import oclc
from .xml2rdf import xml2rdf
from .queries.queries import collect_queries
from .utils import cleaning_functions  # , cleaning_closures
from .conversions.update_graph import pre_reasoner_scripts, post_reasoner_scripts
from .reasoner.reasoner import instantiate_inferred_triples as reasoner


# this is the bibframe model
# Importing this allows ontology aware queries.
bf_model = Path(__file__).parent / "imported_model" / "bibframe.ttl"
rel_model = Path(__file__).parent / "imported_model" / "relators.skosrdf.ttl"
lang_model = Path(__file__).parent / "imported_model" / "languages.madsrdf.ttl"

included_model = Path(__file__).parent / "included_model" / "clean_marc.ttl"


def apply_functions(
    df: DataFrame, cleaning_funcs: Dict[str, Callable], **kwargs
) -> DataFrame:
    """Cleaning functions take a series, and create new dataframe columns based
    on this.
    This allows for extensible functions to be declared by sparql queries and
    defined in cleaning function dictionary.
    """
    columns = df.columns.to_list()
    drop_columns = []
    for column in columns:
        # print(f"Column name {column}")
        # This uses the Walrus Operator to test if the column exists
        # in the dictionary, if it exists run the function on the dataframe
        if f := cleaning_funcs.get(column):
            df = df.apply(f, axis=1, **kwargs)
            drop_columns.append(column)

    # new_columns = df.columns
    for column in df.columns:
        if column in columns:
            continue
        columns.append(column)

    columns = [c for c in columns if c not in drop_columns]

    return df[columns]


def read_worldcat_items(file_name: Path) -> pd.DataFrame:
    """
    This is for reading the world cat items
    """
    _root, ext = os.path.splitext(file_name)
    df = pd.DataFrame()
    if ext == ".xlsx":
        df = pd.read_excel(file_name)
    elif ext == ".csv":
        df = pd.read_csv(file_name)
    else:
        raise Exception("Error in the file")

    return df


def cli():
    """
    This is the command line interface. Handling the calls to the different
    functions.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "marc_files",
        nargs="*",
        help="Marc Files that are to be added to the store and cleaned",
    )
    parser.add_argument(
        "-o",
        "--output",
        nargs="?",
        help="Set the output file for the converted bibframe.",
    )
    parser.add_argument(
        "-w",
        "--worldcat",
        # At some point we are going to want to change these to passing in a
        # text file
        # action="store_true",
        nargs="?",
        help="""return marc record for oclc numbers. These must have a column
        'OCLC number'. The OCLC number column is used to
        query the worldcat
        database""",
    )
    parser.add_argument(
        "-x",
        "--save-xml",
        nargs="?",
        help="""Where the xml should be store. Primarily used for worldcat
        records""",
    )
    parser.add_argument(
        "-q",
        "--query",
        nargs="?",
        help="""Optionally select query or queries to run, not all of the
        queries in the script""",
    )
    parser.add_argument(
        "-d",
        "--dir",
        nargs="?",
        help="""specify the directory to save the output files to, if no
        argument is specified, the default current working directory will be
        used"""
    )
    parser.add_argument(
        "-i",
        "--skip-inference",
        action="store_true",
        help="""skip the inferencing step. Inferencing can take some time, this
        skips the inferencing step"""
    )

    args = parser.parse_args()

    graph = Graph()

    marc_records = 0

    if args.dir:
        dir = Path(args.dir)
        dir.mkdir(parents=True, exist_ok=True)
    else:
        dir = Path(".")

    if args.worldcat:
        worldcat_df = read_worldcat_items(args.worldcat)
        oclc_numbers = list(worldcat_df["OCLC number"])
        marc_tree = oclc.create_marc_collection(oclc_numbers=oclc_numbers)
        if args.save_xml:
            with open(dir / args.save_xml, "w") as fp:
                xmlstr = etree.tostring(marc_tree, pretty_print=True)
                fp.write(xmlstr.decode())
        marc_records, graph = xml2rdf.marc2rdf(
            marc_tree, graph, separate_works=False)
    else:
        worldcat_df = pd.DataFrame()

    for marc_file in args.marc_files:
        print(marc_file)
        marc_path = Path(marc_file)
        marc_tree = xml2rdf.read_marc_file(marc_path)
        m_records, graph = xml2rdf.marc2rdf(
            marc_tree, graph, separate_works=False)
        marc_records = marc_records + m_records

    if args.save_xml:
        with open(dir / args.save_xml, "w") as fp:
            xmlstr = etree.tostring(marc_tree, pretty_print=True)
            fp.write(xmlstr.decode())

    print(f"Number of Marc Records: {marc_records}")

    graph.parse(included_model)
    # scripts for updating the graph
    graph = pre_reasoner_scripts(graph)

    # run inferencing
    if not args.skip_inference:
        graph = reasoner(graph)

    graph = post_reasoner_scripts(graph)

    # Import the models for context aware queries
    graph.parse(bf_model)
    graph.parse(rel_model)
    graph.parse(lang_model)

    if args.output:
        print(dir / args.output)
        graph.serialize(dir / args.output, format="turtle")

    # print("print graph", graph.serialize(format="turtle"))
    queries = collect_queries()

    if args.query:
        queries = [x for x in queries if x["query_name"] in args.query]

    for query_obj in queries:
        name = query_obj["query_name"]
        query = query_obj["query"]

        print(name)
        res = graph.query(query)
        # print(
        df = pd.read_csv(
            StringIO(
                res.serialize(format="csv", encoding="utf-8",
                              separator="\t").decode()
            )
        )
        df = apply_functions(df, cleaning_functions, add_df=worldcat_df)
        df.to_excel(dir / f"{name}.xlsx", index=False)
