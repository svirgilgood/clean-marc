from pathlib import Path
from typing import List, Dict

from ..utils import QuerDir

base_dir = Path(__file__).parent


def collect_queries(dir=QuerDir.ITEM) -> List[Dict[str, str]]:
    """
    Read the contents of the queries directory to create
    queries
    """

    match dir:
        case QuerDir.ITEM:
            query_dir = base_dir / "item_queries"
        case QuerDir.RECORD:
            query_dir = base_dir / "record_queries"

    queries: List[Dict[str, str]] = []
    for query in (base_dir / dir.value).glob("*.rq"):
        basename = query.stem
        with open(query, "r") as fp:
            queries.append({"query_name": basename, "query": fp.read()})
    return queries
