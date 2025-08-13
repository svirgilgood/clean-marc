from pathlib import Path
from typing import List, Dict

query_dir = Path(__file__).parent


def collect_queries() -> List[Dict[str, str]]:
    """
    Read the contents of the queries directory to create
    queries
    """
    queries: List[Dict[str, str]] = []
    for query in query_dir.glob("*.rq"):
        basename = query.stem
        with open(query, "r") as fp:
            queries.append({"query_name": basename, "query": fp.read()})
    return queries
