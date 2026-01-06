import pysparql_anything as sa
from enum import Enum
from pathlib import Path
from typing import List
from dataclasses import dataclass


quer_dir = Path(__file__).parent / "queries"


class AnythingQuer(Enum):
    AGENT = "agents_sa.sparql"
    PLACE = "places_sa.sparql"
    CONTENT_ANALYSIS = "content_analysis_sa.sparql"


@dataclass
class QueryObj:
    query: AnythingQuer
    file_path: Path


def format_queries(query_path: str, file_path: Path) -> str:
    """
    This function takes the query and the path to the file that
    will be injected into the spaql-anything query that will be
    executed by the engine.

    Arguments are used to add flexibility to the usage of the script
    so that a user can clean the spreadsheets with openrefine or other
    tools.
    """
    with open(quer_dir / query_path, "r") as fp:
        query = fp.read()
        fpath = str(file_path.resolve())
        query = query.replace("${spreadsheet}", fpath)

    return query


def spanything(queries: List[QueryObj], output_dir: Path):
    """
    Instantiates the sparql-anything engine and runs all of the
    queries passed into the argument.

    We save these to the output directory because the engine isn't
    properly handling the graph output. I think this has to do with
    the log4j not being in the sparql-anything jar.
    """
    engine = sa.SparqlAnything()

    for query_obj in queries:
        query = format_queries(query_obj.query.value, query_obj.file_path)
        destination_file = query_obj.file_path.stem + ".ttl"

        engine.run(
            query=query,
            output=str((output_dir / destination_file).resolve()),
            format="ttl"
        )
