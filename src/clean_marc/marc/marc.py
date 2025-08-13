# 100
# FIELD DEFINITION AND SCOPE
# Personal name used as a main entry in a bibliographic record.
# Main entry is assigned according to various cataloging rules, usually to the
# person chiefly responsible for the work.
ONEHUNDRED_CODES = {
    "first-indicator": {
        "0": "Forename",
        "1": "Surname",
        "3": "Family name",
    },
    "second-indicator": {
        "#": "Undefined",
    },
    "subfield-codes": {
        "a": "Personal name (NR)",
        "b": "Numeration (NR)",
        "c": "Titles and words associated with a name (R)",
        "d": "Dates associated with a name (NR)",
        "e": "Relator term (R)",
        "f": "Date of a work (NR)",
        "g": "Miscellaneous information (R)",
        "j": "Attribution qualifier (R)",
        "k": "Form subheading (R)",
        "l": "Language of a work (NR)",
        "n": "Number of part/ section of a work(R)",
        "p": "Name of part/ section of a work(R)",
        "q": "Fuller form of name (NR)",
        "t": "Title of a work (NR)",
        "u": "Affiliation (NR)",
        "0": "Authority record control number or standard number (R)",
        "1": "Real World Object URI (R)",
        "2": "Source of heading or term (NR)",
        "4": "Relationship (R)",
        "6": "Linkage (NR)",
        "7": "Data provenance (R)",
        "8": "Field link and sequence number (R)",

    }
}
# 110
# FIELD DEFINITION AND SCOPE
# Corporate name used as a main entry in a bibliographic record.
#
# According to various cataloging rules, main entry under corporate name is
# assigned to works that represent the collective thought of a body.
#
# Conference and meeting names that are entered subordinately to a corporate
# body are contained in this field rather than in field 111.
ONEHUNDREDTEN_CODES = {
    "first-indicator": {
        # Type of corporate name element
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order",
    },
    "second-indicator": {
        # undefined
        "#": "Undefined",
    },
    "subfield-codes": {
        "a": "Corporate name or jurisdiction name as entry element (NR)",
        "b": "Subordinate unit (R)",
        "c": "Location of meeting (R)",
        "d": "Date of meeting or treaty signing (R)",
        "e": "Relator term (R)",
        "f": "Date of a work (NR)",
        "g": "Miscellaneous information (R)",
        "k": "Form subheading (R)",
        "l": "Language of a work (NR)",
        "n": "Number of part/section/meeting (R)",
        "p": "Name of part/section of a work (R)",
        "t": "Title of a work (NR)",
        "u": "Affiliation (NR)",
        "0": "Authority record control number or standard number (R)",
        "1": "Real World Object URI (R)",
        "2": "Source of heading or term (NR)",
        "4": "Relationship (R)",
        "6": "Linkage (NR)",
        "7": "Data provenance (R)",
        "8": "Field link and sequence number (R)",
    }
}

# 600
# Subject added entry in which the entry element is a personal name.
#
# Subject added entries are assigned to a bibliographic record to provide
# access according to established subject cataloging principles and
# guidelines. Field 600 may be used by any institution assigning
# subject headings based on the lists and authority files identified in the
# second indicator position or in subfield $2 (Source of heading or term).
SIXHUNDRED_CODES = {
    "first-indicator": {
        "0": "Forename",
        "1": "Surname",
        "3": "Family name",
    },
    "second-indicator": {
        "0": "Library of Congress Subject Headings",
        "1": "Library of Congress Childrens and Young Adult Subject Headings",
        "2": "Medical Subject Headings",
        "3": "National Agricultural Library subject authority file",
        "4": "Source not specified",
        "5": "Canadian Subject Headings",
        "6": "Répertoire de vedettes-matière",
        "7": "Source specified in subfield $2"
    },
    "subfield-codes": {
        "a": "Personal name (NR)",
        "b": "Numeration (NR)",
        "c": "Titles and other words associated with a name (R)",
        "d": "Dates associated with a name (NR)",
        "e": "Relator term (R)",
        "f": "Date of a work (NR)",
        "g": "Miscellaneous information (R)",
        "h": "Medium (NR)",
        "j": "Attribution qualifier (R)",
        "k": "Form subheading (R)",
        "l": "Language of a work (NR)",
        "m": "Medium of performance for music (R)",
        "n": "Number of part / section of a work(R)",
        "o": "Arranged statement for music (NR)",
        "p": "Name of part / section of a work(R)",
        "q": "Fuller form of name (NR)",
        "r": "Key for music (NR)",
        "s": "Version (R)",
        "t": "Title of a work (NR)",
        "u": "Affiliation (NR)",
        "v": "Form subdivision (R)",
        "x": "General subdivision (R)",
        "y": "Chronological subdivision (R)",
        "z": "Geographic subdivision (R)",
        "0": "Authority record control number or standard number (R)",
        "1": "Real World Object URI (R)",
        "2": "Source of heading or term (NR)",
        "3": "Materials specified (NR)",
        "4": "Relationship (R)",
        "6": "Linkage (NR)",
        "7": "Data provenance (R)",
        "8": "Field link and sequence number (R)",

    }
}
SEVENHUNDRED_CODES = {
    "first-indicator": {
        "0": "Forename",
        "1": "Surname",
        "3": "Family name",
    },
    "second-indicator": {
        "#": "No information provided",
        "2": "Analytical entry",
    },
    "subfield-codes": {
        '0': "Standard Number",
        '1': "VIAF Number",
        '4': "Relations",
        "5": "Institution to which field applies",  # we may want save this one
        'a': "Name",
        'b': "Numeration",
        'c': "Associated Works",
        'd': "Dates",
        'e': "Relator Term",
        "f": "Date of a work",
        "h": "Medium",
        'i': "relationship",
        'k': "Form Subheading",
        "l": "Language of a work",
        'm': "Medium of Performance",
        'n': "Number or Part",
        'o': "Arranged Statement",
        'p': "Name of part/section",
        'q': "Alt Name",
        'r': "Key for Music",
        't': "Title",
        "v": "",
    }
}


# 610
# FIELD DEFINITION AND SCOPE
# Subject added entry in which the entry element is a corporate name.
#
# Subject added entries are assigned to a bibliographic record to provide
# access according to established subject cataloging principles and guidelines.
# Field 610 may be used by any institution assigning subject headings based on
# lists and authority files identified in the second indicator position or in
# subfield $2 (Source of heading or term).
#
# Meeting names that are not entered subordinately to a corporate body are
# recorded in field 611 (Subject Added Entry-Meeting Name).
#
# Indicators
# Second Indicator - Thesaurus
#
# Subject heading system or thesaurus used in constructing the subject heading.
#
# 0 - Library of Congress Subject Headings
# Subject added entry conforms to and is appropriate for use in the Library of
# Congress Subject Headings (LCSH) and the Name authority files that are
# maintained by the Library of Congress.
#
# 1 - Library of Congress Children's and Young Adults' Subject Headings
# Subject added entry conforms to the Library of Congress Children's and Young
# Adults' Subject Headings used for the Library of Congress Children's and
# Young Adults' Cataloging (CYAC) Program and is appropriate for use according
# to CYAC guidelines.
#
# 2 - Medical Subject Headings
# Subject added entry conforms to and is appropriate for use in the National
# Library of Medicine authority files.
#
# 3 - National Agricultural Library subject authority file
# Subject added entry conforms to and is appropriate for use in the National
# Agricultural Library subject authority file.
#
# 4 - Source not specified
# Subject added entry conforms to a controlled list that cannot be identified
# by second indicator values 0-3, 5-6 or by a code in subfield $2. Field 653
# (Index Term-Uncontrolled) is used to record terms that are not derived from
# controlled subject heading lists.
#
# 5 - Canadian Subject Headings
# Subject added entry conforms to and is appropriate for use in the Canadian
# Subject Headings that is maintained by the Library and Archives Canada.
#
# 6 - Répertoire de vedettes-matière
# Subject added entry conforms to the Répertoire de vedettes-matière that is
# maintained by the Bibliothèque de l'Université Laval and/or name authority
# files maintained by libraries in Canada using French as the language of
# description.
#
# 7 - Source specified in subfield $2
# Subject added entry conforms to a set of subject heading system/thesaurus
# building rules. The identifying code is given in subfield $2.
SIXHUNDERDTEN_CODES = {
    "first-indicator": {
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order",
    },
    "second-indicator": {
        "0": "Library of Congress Subject Headings",
        "1": "Library of Congress Children and Young Adult Subject Headings",
        "2": "Medical Subject Headings",
        "3": "National Agricultural Library subject authority file",
        "4": "Source not specified",
        "5": "Canadian Subject Headings",
        "6": "Répertoire de vedettes-matière",
        "7": "Source specified in subfield $2",
    },
    "subfield-codes": {
        "a": "Corporate name or jurisdiction name as entry element (NR)",
        "b": "Subordinate unit (R)",
        "c": "Location of meeting (R)",
        "d": "Date of meeting or treaty signing (R)",
        "e": "Relator term (R)",
        "f": "Date of a work (NR)",
        "g": "Miscellaneous information (R)",
        "h": "Medium (NR)",
        "k": "Form subheading (R)",
        "l": "Language of a work (NR)",
        "m": "Medium of performance for music (R)",
        "n": "Number of part / section/meeting(R)",
        "o": "Arranged statement for music (NR)",
        "p": "Name of part / section of a work(R)",
        "r": "Key for music (NR)",
        "s": "Version (R)",
        "t": "Title of a work (NR)",
        "u": "Affiliation (NR)",
        "v": "Form subdivision (R)",
        "x": "General subdivision (R)",
        "y": "Chronological subdivision (R)",
        "z": "Geographic subdivision (R)",
        "0": "Authority record control number or standard number (R)",
        "1": "Real World Object URI (R)",
        "2": "Source of heading or term (NR)",
        "3": "Materials specified (NR)",
        "4": "Relationship (R)",
        "6": "Linkage (NR)",
        "7": "Data provenance (R)",
        "8": "Field link and sequence number (R)",
    }
}

# 710:
# Added Entry in which the Entry elements is a corporate name
# Added entries are assigned according to various cataloging rules to give
# access to the bibliographic record from corporate name headings which may not
# be more appropriately assigned as 610 (subject added Entry-corporate name) or
# 810 (Series Added Entry-Corporate name) fields
# Guidelines:
# Description of the first indicator position and all subfield codes, as well
# as input conventions for the 710 field are given in the X10 Corporate
# Names-General Information section. Because the second indicator is different
# for various fields, it is not described in the general information section,
# but is described below.
SEVENHUNDREDTEN_CODES = {
    "first-indicator": {
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order",
    },
    "second-indicator": {
        # Used when the added entry is not for an analytic or when no
        # information is provided as to whether the added entry is
        # for an analytic.
        "#": "No information provided",
        # Item in hand contains the work that is represented by the added
        # entry.
        "2": "Analytical entry",
    },
    "subfield-codes": {
        "a": "Corporate name or jurisdiction name as entry element (NR)",
        "b": "Subordinate unit (R)",
        "c": "Location of meeting (R)",
        "d": "Date of meeting or treaty signing (R)",
        "e": "Relator term (R)",
        "f": "Date of a work (NR)",
        "g": "Miscellaneous information (R)",
        "h": "Medium (NR)",
        "i": "Relationship information (R)",
        "k": "Form subheading (R)",
        "l": "Language of a work (NR)",
        "m": "Medium of performance for music (R)",
        "n": "Number of part/section/meeting (R)",
        "o": "Arranged statement for music (NR)",
        "p": "Name of partsection of a work (R)",
        "r": "Key for music (NR)",
        "s": "Version (R)",
        "t": "Title of a work (NR)",
        "u": "Affiliation (NR)",
        "x": "International Standard Serial Number (NR)",
        "0": "Authority record control number or standard number (R)",
        "1": "Real World Object URI (R)",
        "2": "Source of heading or term (NR)",
        "3": "Materials specified (NR)",
        "4": "Relationship (R)",
        "5": "Institution to which field applies (NR)",
        "6": "Linkage (NR)",
        "7": "Data provenance (R)",
        "8": "Field link and sequence number (R)",
    },
}

# 810
# Author/title series added entry in which the author portion is a corporate
# name.
#
# An 810 field is usually justified by a series statement (field 490) or a
# general note (field 500) relating to the series. For reproductions, it may
# be justified by a series statement in subfield $f of field 533 (Reproduction
# Note).
#
# GUIDELINES FOR APPLYING CONTENT DESIGNATORS
# Description of the first indicator position and all subfield codes, as well
# as input conventions for the 810 field are given in the X10 Corporate Names-
# General Information section. Because the second indicator is different for
# various fields, it is not described in the general information section, but
# is described below.
EIGHTHUNDREDTEN_CODES = {
    "first-indicator": {
        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order",
    },
    "second-indicator": {
        "#": "Undefined",
    },
    "subfield-codes": {

        "a": "Corporate",
        "b": 'Subordinate',
        "c": 'Location',
        "d": 'Date',
        "e": 'Relator',
        "f": "Date",
        "g": "Miscellaneous",
        "h": "Medium",
        "k": "Form",
        "l": "Language",
        "m": "Medium",
        "n": "Number",
        "o": "Arranged",
        "p": "Name",
        "r": "Key",
        "s": "Version",
        "t": "Title",
        "u": "Affiliation",
        "v": "Volume/sequential",
        "w": "Bibliographic",
        "x": "International",
        "y": "Data",
        "1": "Real",
        "2": "Source",
        "3": "Materials",
        "4": "Relationship",
        "5": "Institution",
        "6": "Linkage",
        "7": "Control",
        "8": "Field",
    }
}
