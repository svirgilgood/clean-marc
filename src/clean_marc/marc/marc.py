from .marc_data import (
    ONEHUNDRED_CODES,
    ONEHUNDREDTEN_CODES,
    SIXHUNDRED_CODES,
    SIXHUNDREDTEN_CODES,
    SIXHUNDREDELEVEN_CODES,
    EIGHTHUNDRED_CODES,
    EIGHTHUNDREDTEN_CODES,
    SEVENHUNDREDTEN_CODES,
    SEVENHUNDREDELEVEN_CODES,
    SEVENHUNDRED_CODES,
)
from typing import Dict, Set

ONEHUNDRED_CODES = ONEHUNDRED_CODES
ONEHUNDREDTEN_CODES = ONEHUNDREDTEN_CODES
SIXHUNDRED_CODES = SIXHUNDRED_CODES
SIXHUNDREDTEN_CODES = SIXHUNDREDTEN_CODES
SIXHUNDREDELEVEN_CODES = SIXHUNDREDELEVEN_CODES
EIGHTHUNDRED_CODES = EIGHTHUNDRED_CODES
EIGHTHUNDREDTEN_CODES = EIGHTHUNDREDTEN_CODES
SEVENHUNDREDTEN_CODES = SEVENHUNDREDTEN_CODES
SEVENHUNDREDELEVEN_CODES = SEVENHUNDREDELEVEN_CODES
SEVENHUNDRED_CODES = SEVENHUNDRED_CODES


def decompose_marc_string(
        marc: str,
        series_additions: Dict[str, Set[str]]
) -> Dict[str, Set[str]]:
    """
    A function for cleaning the marc keys that are
    """
    marc = marc.strip()
    # print(f"marc code '{marc}'")
    field = marc[:3]
    series_additions.setdefault("00 - Field", set()).add(field)
    match field:
        case "100": value_dict = ONEHUNDRED_CODES
        case "110": value_dict = ONEHUNDREDTEN_CODES
        case "600": value_dict = SIXHUNDRED_CODES
        case "610": value_dict = SIXHUNDREDTEN_CODES
        case "700": value_dict = SEVENHUNDRED_CODES
        case "710": value_dict = SEVENHUNDREDTEN_CODES
        case "711": value_dict = SEVENHUNDREDELEVEN_CODES
        case "800": value_dict = EIGHTHUNDRED_CODES
        case "810": value_dict = EIGHTHUNDREDTEN_CODES
        case _:
            print(f"\033[31mField not found!!! {field}!\033[0m")
            print(f"marc code '{marc}'")
            return series_additions

    try:
        first_indicator = marc[3]
        if first_indicator != "" and first_indicator != " ":
            indicator_value = value_dict["first-indicator"].get(
                first_indicator)
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
            subfield_key = value_dict["subfield-codes"][subfield_code]
            series_additions.setdefault(
                f"{subfield_code} - {subfield_key}", set()).add(subfield[1:])
    except KeyError as e:
        print(f"\033[93mKey Error for {marc}\033[0m\n {e}")

    return series_additions
