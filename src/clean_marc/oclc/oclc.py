from bookops_worldcat import WorldcatAccessToken, MetadataSession
import bookops_worldcat
import time
import os
import json
import lxml.etree as etree
from lxml.etree import _Element
from dotenv import load_dotenv, dotenv_values
from ..utils import MARC_SLIM, MARC_NAMESPACES


load_dotenv()

token = WorldcatAccessToken(
    key=os.getenv("KEY"),
    secret=os.getenv("SECRET"),
    scopes="WorldCatMetadataAPI",
)


oclc_numbers = [
    "1378313410",
    "1378316332",
    "1378318265",
    "1378323010",
    "1378323657",
    "1453254855",
    "1453255301",
    "1453255537",
    "1453255768",
    "1453256841",
    "1453256900",
    "1453256950",
    "1453256997",
    "1453257042",
    "1453257074",
    "1453257174",
    "1453257204",
    "1453257296",
    "1453257347",
    "1453257561",
    "1453399628",
    "1453400053",
    "1453414070",
    "1453414754",
    "1453414802",
    "1453467561",
    "1453467833",
    "1453468165",
    "1453518796",
    "1453620250",
    "1453620508",
    "1453620530",
    "1453620581",
    "1453620703",
    "1453632085",
    "1453632180",
    "1453632186",
    "1453632201",
    "1453632250",
    "1453632293",
    "1453632368",
    "1453632378",
    "1453632389",
    "1453632486",
    "1453632537",
    "1453632539",
    "1453632674",
    "1453632699",
    "1453632706",
    "1453632767",
    "1453639394",
    "1453639558",
    "1453639624",
    "1453639807",
]


def search_oclc(
        token=token,
        search_str="ti: The Power Broker AND au: Caro, Robert"
):
    """
    search_str can use any of the search codes allowed in worldcat.
    """
    with MetadataSession(authorization=token) as session:
        response = session.brief_bibs_search(
            q=search_str)
        j = response.json()
        print(json.dumps(j, indent="  "))


def find_record(token=token, oclc="1463313217"):
    '''
    search oclc for a particular oclc number. These numbers need to be entered
    as strings. The result.text returns an xml document.
    '''
    with MetadataSession(authorization=token) as session:
        result = session.bib_get(oclc)
        # print(result.text)
    return result.text


def create_marc_collection(oclc_numbers=oclc_numbers) -> _Element:
    """
    create a marc element tree based on a OCLC records
    """
    collection_et = etree.Element(
        "{%s}" % MARC_SLIM + "collection", nsmap=MARC_NAMESPACES)
    with MetadataSession(authorization=token) as session:

        for oclc in oclc_numbers:
            # xml_text = find_record(oclc=oclc)
            try:
                result = session.bib_get(oclc)
            except bookops_worldcat.errors.WorldcatRequestError:
                print("Error in Request, Sleeping and trying again")
                time.sleep(2)
                result = session.bib_get(oclc)
            except bookops_worldcat.errors.InvalidOclcNumber:
                print(f"Not an OCLC Number {oclc}")
                continue

            xml_text = result.text
            xml_text = xml_text.replace("encoding='UTF-8'", '')
            parser = etree.XMLParser(
                ns_clean=True, recover=True, encoding='utf-8')
            xml_tree = etree.fromstring(xml_text, parser=parser)
            root = xml_tree.getroottree()
            for child in root.iter("{%s}" % MARC_SLIM + "record"):
                collection_et.append(child)

    return collection_et

    # for record in root.findall("./{%s}" % MARC_SLIM + "record"):
    #    print("record", record)
    # collection_et.append(record)

    # print(etree.tostring(collection_et, pretty_print=True).decode())
