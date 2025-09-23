import lxml.etree as ET
from pathlib import Path
from io import StringIO
from rdflib import Graph
from typing import Tuple, Union
from lxml.etree import _Element, _ElementTree
import re


xsl_dir = Path(__file__).parent/"marc2bibframe2"/"xsl"
marc_t = xsl_dir/"marc2bibframe2.xsl"
marc_xsl = ET.parse(marc_t)
transform = ET.XSLT(marc_xsl)

# pre_process_t = Path(__file__).parent/"ConvSpec-Preprocess0-Splitting.xsl"
pre_process_t = xsl_dir/"ConvSpec-Preprocess0-Splitting.xsl"
pre_process_xsl = ET.parse(pre_process_t)
work_trans = ET.XSLT(pre_process_xsl)


MARC_SLIM = 'http://www.loc.gov/MARC21/slim'
ns = {
    "atom": "http://www.w3.org/2005/Atom",
    None: MARC_SLIM,
    "marc": MARC_SLIM
}

namespaces = {
    "marc": MARC_SLIM
}


def count_marc_records(marc_tree: Union[_ElementTree, _Element]) -> int:
    """
    Count the number of marc:record are in the XML tree
    This should be used to provide a check for other examples
    """
    return len(list(marc_tree.findall(".//{%s}" % MARC_SLIM + "record")))


def clean_lang_fields(et: _ElementTree):
    """
    Language fields should not have numbers,
    they should be moved to be a part
    """
    root = et.getroot()
    print("in the cleaning field")
# ".//marc:datafield[@tag='600' or @tag='610' or @tag='700' or @tag='710' or @tag='800' or @tag='810']/marc:subfield[@code='l']/..",
    for datafield in root.xpath(
        ".//marc:datafield[@tag='600' or @tag='610' or @tag='710' or @tag='700' or @tag='800' or @tag='810']/marc:subfield[@code='l']/..",
        namespaces=namespaces
    ):
        # print(f"Datafield: {datafield.tag}")
        for lang in datafield.findall(".//{%s}subfield[@code='l']" % MARC_SLIM):
            # print(f"lang: {lang.text}")
            numbers = re.findall(r'[\d ]+', lang.text)
            # print(f"numbers: {numbers}")
            if len(numbers) == 0:
                continue
            for num in numbers:
                num_ele = ET.SubElement(datafield, "{%s}subfield" % MARC_SLIM)
                num_ele.set("code", "n")
                num_ele.text = str(num).strip()
    return et


def read_marc_file(marc_file: Path) -> _ElementTree:
    with open(marc_file, "r")as fp:
        marc_xml = fp.read()
    marc_xml = marc_xml.replace(
        'xmlns="http://www.w3.org/2005/Atom"',
        'xmlns="http://www.loc.gov/MARC21/slim"'
    )
    marc_xml = marc_xml.replace('encoding="UTF-8"', "")
    marc_tree = ET.parse(StringIO(marc_xml))
    collection_et = ET.Element("{%s}" % MARC_SLIM + "collection", nsmap=ns)
    marc_tree = clean_lang_fields(marc_tree)
    for record in marc_tree.findall(".//{%s}" % MARC_SLIM + "record"):
        collection_et.append(record)

    return collection_et


def marc2rdf(marc: Union[_ElementTree, _Element], graph: Graph, separate_works=False) -> Tuple[int, Graph]:
    """Add a MARC-XML File to an existing graph, return the graph
    Right now, the separate works flag is not working for some reason.
    This function takes a collection of marc records with the structure:

    ```
    <?xml version="1.0"?>
        <collection xmlns="http://www.loc.gov/MARC21/slim">
            <record>
    ```
    Where <record> can be a repetting element.
    """

    marc_records = count_marc_records(marc)

    # new_dom = transform(marc_tree)
    if separate_works:
        new_dom = work_trans(marc)
    else:
        new_dom = transform(marc)
    # print(ET.tostring(new_dom, pretty_print=True).decode())

    graph.parse(ET.tostring(new_dom), format="xml")

    return (marc_records, graph)
