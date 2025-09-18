"""

"""
from typing import Dict


def decompose_marc_string(marc: str) -> Dict[str, str]:
    """
    A function for cleaning the marc keys that are
    """
    series_additions = {}
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


# class MarcField
"""
    I think It wwould be good to have a proper class definition
    """


class SevenHundredTen:
    def __init__(self, marc_key):
        """
        """
