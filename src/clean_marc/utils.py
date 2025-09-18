import re
from rdflib import Graph, URIRef, RDF
import pandas as pd
from typing import Union
from .marc.marc import (
    ONEHUNDRED_CODES,
    ONEHUNDREDTEN_CODES,
    SIXHUNDRED_CODES,
    SIXHUNDERDTEN_CODES,
    EIGHTHUNDRED_CODES,
    EIGHTHUNDREDTEN_CODES,
    SEVENHUNDREDTEN_CODES,
    SEVENHUNDRED_CODES,
)

MARC_SLIM = 'http://www.loc.gov/MARC21/slim'

MARC_NAMESPACES = {
    "atom": "http://www.w3.org/2005/Atom",
    None: MARC_SLIM,
    "marc": MARC_SLIM
}

DATE_PATTERN = re.compile(r"((approximately )?[0-9\-\?]+)$")


def count_class_instances(graph: Graph, rdf_class: URIRef) -> int:
    """
    Return the number of instances of a class
    """
    return len(list(graph.subjects(RDF.type, rdf_class)))


NSMAP = {
    # "http://id.loc.gov/ontologies/bibframe/": "bf",
    # "http://www.loc.gov/mads/rdf/v1#": "madsrdf",
    "http://id.loc.gov/ontologies/bibframe/": "bf",
    "http://id.loc.gov/ontologies/bflc/": "bflc",
    "http://creativecommons.org/ns#": "cc",
    "http://purl.org/dc/terms/": "dcterms",
    "http://xmlns.com/foaf/0.1/": "foaf",
    "http://www.loc.gov/mads/rdf/v1#": "madsrdf",
    "http://www.w3.org/2002/07/owl#": "owl",
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf",
    "http://www.w3.org/2000/01/rdf-schema#": "rdfs",
    "http://www.w3.org/2004/02/skos/core#": "skos",
    "http://www.w3.org/2001/XMLSchema#": "xs",
    "http://id.loc.gov/vocabulary/languages/": "lclang",
    "http://id.loc.gov/vocabulary/relators/": "rel",
}


def shorten_uri(uri: str) -> str:
    slash_idx = uri.rfind("/")
    hash_idx = uri.rfind("#")
    index = (slash_idx if slash_idx > hash_idx else hash_idx) + 1
    if (prefix := NSMAP.get(uri[:index])):
        return f"{prefix}:{uri[index:]}"
    return uri


def create_external_id_columns(series: pd.Series, **kwargs) -> pd.Series:
    """
    This takes the marcKey value:
    `7001 $aPörnbacher, Mechthild$eeditor of music$1http://viaf.org/viaf/737569$0http://id.loc.gov/authorities/names/n84174691"`
    and turns it into a list of columns for the agents
    """
    mark_keys = series["_create_external_id_columns"]
    for mark_key in mark_keys.split(";"):
        mark_list = mark_key.split("$")
        # key_errors = {}
        for item in mark_list[1:]:
            if item[0] in ("4", "5", "e", "f", "h", "l"):
                continue
            try:
                series[SEVENHUNDRED_CODES["subfield-codes"][item[0]]] = item[1:]
            except KeyError:
                # How could we create a way of collecting
                # These errors in a way that allow for investigation without
                # duplication?
                # pass
                # key_errors[item[0]] = f"Example: {mark_list}"
                print(f"There is an error with key: {item[0]}\n\t{mark_key}")
        # if key_errors:
            # print("Key Errors for SEVENHUNDRED_CODES:", key_errors)
    return series


def create_topics_hierarchy(series: pd.Series, **kwargs) -> pd.Series:
    """"
    `madsrdf:Topic|Music;madsrdf:Temporal|15th century;madsrdf:Topic|Manuscripts`
    Needs to take this, and create the following headings
    """
    auth_label = series["authLabel"]
    number_of_terms = len(auth_label.split("--"))
    topics = series["_create_topics_hierarchy"]
    if type(topics) is not str:
        return series
    topic_list = topics.split(";")
    term_set = set()
    # We aren't using enumerate here, because there are sometimes duplicates
    # based on the types Like Catholic church is both an agent and organization
    idx = 0
    for topic in topic_list:
        if type(topic) is not str:
            continue
        topic_type, topic_name = topic.split("|")
        if topic_name in term_set or (idx + 1) > number_of_terms:
            continue
            # return series
        series[f"Topic {str(idx).zfill(2)} Type"] = shorten_uri(topic_type)
        series[f"Topic {str(idx).zfill(2)} Name"] = topic_name
        term_set.add(topic_name)
        idx = idx + 1
    return series


def clean_name(name: str) -> str:
    """
    Remove final punctuation from a name string
    """
    name_value = name.strip()
    # Removes a final period, if it is not an Abbreviation
    if name_value[-1] == "." and name_value[-3] != " ":
        name_value = name_value[:-1]
    if name_value[-1] in (",", ";"):
        name_value = name_value[:-1]

    return name_value


def extract_dates_from_names(series: pd.Series, **kwargs) -> pd.Series:
    """
    Some names from Marc have the format: `"Shortall, Harrington 1895-1984"`

    But they can also have `?` and use `approximately`
    """
    agent_label = series["agentLabel"]

    """
    Some of these dates won't have a date, but we still need to populate the name field
    """
    if series["types"] == "http://id.loc.gov/ontologies/bibframe/Organization":
        series["Name"] = clean_name(agent_label)
        return series

    if type(agent_label) is not str:
        return series

    matches = list(DATE_PATTERN.finditer(agent_label))

    if len(matches) < 1:
        name_value = clean_name(agent_label)
        # print(f"\033[94mname value: '{name_value}'\033[0m")
        series["Name"] = name_value
    else:
        for idx, pattern_match in enumerate(DATE_PATTERN.finditer(agent_label)):
            name_heading = "Name" if idx == 0 else f"Name {str(idx).zfill(2)}"
            date_heading = "Dates" if idx == 0 else f"Dates {
                str(idx).zfill(2)}"

            name_value = pattern_match.string[:pattern_match.start()].strip()
            # print(f"name value: '{name_value}'")
            name_value = clean_name(name_value)

            # print(f"   name value: '{name_value}'")
            series[name_heading] = name_value

            date = pattern_match.group()
            date = date if date.find(
                "approximately") == -1 else date.replace("approximately ", "") + "~"
            if idx == 0:
                date_split = date.split("-")
                born = date_split[0]
                if len(born) >= 4:
                    series["Born"] = born
                if len(date_split) == 2 and len(date_split[1]) >= 4:
                    series["Died"] = date_split[1]

            series[date_heading] = date
    return series


def split_isbns(series: pd.Series, **kwargs) -> pd.Series:
    """
    split ISBNS based on nuumber
    """
    isbns = series["_split_isbns"]

    if type(isbns) is not str:
        return series

    for isbn in isbns.split(";"):
        column = f"ISBN {len(isbn)}"
        if (existing_isbn := series.get(column)):
            isbn = f"{existing_isbn};{isbn}"
        series[column] = isbn
    return series


def create_contributions(series: pd.Series, **kwargs) -> pd.Series:
    """
    Contributions should come in like
        <ContributionRole>|<Contributor>;<ContributionRole>|<Contributor>.|....
    And they should be split where the columns are the number
    """
    contributors = series["_create_contributions"]
    if type(contributors) is not str:
        return series
    for contribution in contributors.split(";"):
        try:
            role, contributor = contribution.split("|")
            if (existing_contrib := series.get(role)):
                contributor = existing_contrib + ";" + contributor
            series[role] = contributor
        except ValueError:
            series["XXContributor"] = f"{contribution} => {contributors}"
    return series


def return_uuid(series: pd.Series, add_df=Union[None, pd.DataFrame], **kwargs) -> pd.Series:
    """
    The add_df is passed in from the wrapping function.
    """
    if add_df is None:
        return series
    oclc_number = series["_add_uuid"]
    if type(oclc_number) is int and oclc_number > 0:
        oclc_number = str(oclc_number)

    elif type(oclc_number) is not str:
        return series
    else:
        pass
    try:
        oclcs = oclc_number.split(";")
        uuids = []
        abbreviations = []
        for oclc in oclcs:
            uuid_id = add_df.loc[add_df["OCLC number"] == int(oclc)]
            try:
                uuid = uuid_id["UUID"].values[0]
                uuids.append(uuid)
                abr = uuid_id["Abbreviation"].values[0]
                abbreviations.append(abr)
            except IndexError:
                continue
        series["UUID"] = ";".join(uuids)
        series["Abbreviation"] = ";".join(abbreviations)
        return series
    except KeyError:
        return series
    except IndexError:
        print(f"Index Error: {series}")
        print(f"UUID row: {uuid_id}")
        return series


def split_agent_marc_string(series: pd.Series, **kwargs) -> pd.Series:
    """
    """
    marc_key = series["_split_agent_marc_string"]
    if type(marc_key) is not str:
        return series
    series_additions = {}
    for marc in marc_key.split(";"):
        marc = marc.strip()
        # print(f"marc code '{marc}'")
        field = marc[:3]
        series_additions.setdefault("00 - Field", set()).add(field)
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
                continue

        try:
            first_indicator = marc[3]
            if first_indicator != "" and first_indicator != " ":
                indicator_value = value_dict["first-indicator"].get(
                    first_indicator)
                if type(indicator_value) is dict:
                    indicator_value = indicator_value["value"]
                if not indicator_value:
                    indicator_value = f"{first_indicator}: not found"
                series_additions.setdefault(
                    "1 - Indicator", set()).add(indicator_value)
            second_indicator = marc[4]
            # and first_indicator != " ":
            if second_indicator not in ("", " ", "$"):
                indicator_value = value_dict["second-indicator"].get(
                    second_indicator)

                if not indicator_value:
                    indicator_value = f"{first_indicator}: not found"
                series_additions.setdefault(
                    "2 - Indicator", set()).add(indicator_value)

            for subfield in marc[5:].split("$"):
                if subfield == "":
                    continue
                subfield_code = subfield[0]
                subfield_key = value_dict["subfield-codes"][subfield_code]["value"]
                series_additions.setdefault(
                    f"{subfield_code} - {subfield_key}", set()).add(subfield[1:])
        except KeyError as e:
            print(f"\033[93mKey Error for {marc}\033[0m\n {e}")

    # print(f"series additions {series_additions}")
    for key, value in series_additions.items():
        series[key] = "; ".join(value)
    # print(f"Series = {series}")

    return series


def simplify_types(series: pd.Series, **kwargs) -> pd.Series:
    """
    """
    term_types = {
        x
        .replace("http://id.loc.gov/ontologies/bibframe/", "")
        .replace("http://www.loc.gov/mads/rdf/v1#", "")
        for x in series["_simplify_types"].split(";")
    }
    if "GenreForm" in term_types:
        term_type = "GenreForm"
    elif "Place" in term_types or "Geographic" in term_types:
        term_type = "Geographic"
    elif "Event" in term_types or "Temporal" in term_types:
        term_type = "Temporal"
    elif "Organization" in term_types or "CorporateName" in term_types:
        term_type = "Organization"
    elif "Person" in term_types or "PersonalName" in term_types:
        term_type = "Person"
    else:
        if len(term_types) > 1:
            print(f"\033[93mAdditional Topic Terms: {
                  '; '.join(term_types)}\033[0m")
        term_type = "Topic"

    series["types"] = term_type

    return series


"""
Cleaning Closures, take the keyword argument `add_df`.
The idea is to use the data frame `add_df` to add some additional information
to the dataframe that is collected.

These are closures because they take data from the `add_df`.
"""
# cleaning_closures = {
#    "_add_uuid": add_uuid,
# }

"""
Cleaning functions are intendended to be called with a pd.DataFrame.apply()
Function, takes a series as an argument, returns a series.
All cleaning_functions must take two arguments: a pd.Series, and **kwargs.

Optional keyword arguments could be:
- add_df: this df can provide additional information if it is provided.
"""
cleaning_functions = {
    "_create_external_id_columns": create_external_id_columns,
    "_create_topics_hierarchy": create_topics_hierarchy,
    "_extract_dates_from_names": extract_dates_from_names,
    "_create_contributions": create_contributions,
    "_split_isbns": split_isbns,
    "_simplify_types": simplify_types,
    "_add_uuid": return_uuid,
    "_split_agent_marc_string": split_agent_marc_string,
}
