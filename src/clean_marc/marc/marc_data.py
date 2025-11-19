from rdflib import Namespace

BF = Namespace("http://id.loc.gov/ontologies/bibframe/")
CMO = Namespace("http://svirgilgood.github.io/clean_marc/onto/")
CMT = Namespace("http://svirgilgood.github.io/clean_marc/taxonomy/")
# 100
# FIELD DEFINITION AND SCOPE
# Personal name used as a main entry in a bibliographic record.
# Main entry is assigned according to various cataloging rules, usually to the
# person chiefly responsible for the work.
ONEHUNDRED_CODES = {
    "class": CMO.Person,
    "first-indicator": {
        "0": {
            "value": "Forename",
            "term": CMT._NameType_Forename,
        },
        "1": {
            "value": "Surname",
            "term": CMT._NameType_Surname,
        },
        "3": {
            "value": "Family name",
            "term": CMT._NameType_FamilyName,
        }
    },
    "second-indicator": {
        "#": "Undefined",
    },
    "subfield-codes": {
        "a": {
            "value": "Personal name (NR)",
            "term": CMT._SFCat_Name,
        },
        "b": {
            "value": "Numeration (NR)",
            "term": CMT._SFCat_Appelation,
        },
        "c": {
            "value": "Titles and other words associated with a name (R)",
            "term": CMT._SFCat_Appelation,
        },
        "d": {
            "value": "Dates associated with a name (NR)",
            "term": CMT._SFCat_AgentDate,
        },
        "e": {
            "value": "Relator term (R)",
            "term": CMT._SFCat_Relator,
        },
        "f": {
            "value": "Date of a work (NR)",
            "term": CMT._SFCat_WorkDate,
        },
        "g": {
            "value": "Miscellaneous information (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "j": {
            "value": "Attribution qualifier (R)",
            "term": CMT._SFCat_Appelation,
        },
        "k": {
            "value": "Form subheading (R)",
            "term": CMT._SFCat_Subtitle,
        },
        "l": {
            "value": "Language of a work (NR)",
            "term": CMT._SFCat_Language,
        },
        "n": {
            "value": "Number of part/ section of a work(R)",
            "term": CMT._SFCat_Part,
        },
        "p": {
            "value": "Name of part/section of a work(R)",
            "term": CMT._SFCat_Part,
        },
        "q": {
            "value": "Fuller form of name (NR)",
            "term": CMT._SFCat_AltName,
        },
        "t": {
            "value": "Title of a work (NR)",
            "term": CMT._SFCat_Title,
        },
        "u": {
            "value": "Affiliation (NR)",
            "term": CMT._SFCat_Affiliation,
        },
        "0": {
            "value": "Authority record control number or standard number (R)",
            "term": CMT._SFCat_ExternalID,
        },
        "1": {
            "value": "Real World Object URI (R)",
            "term": CMT._SFCat_ExternalID,
        },
        "2": {
            "value": "Source of heading or term (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "3": {
            "value": "Materials specified (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "4": {
            "value": "Relationship (R)",
            "term": CMT._SFCat_Relator,
        },
        "6": {
            "value": "Linkage (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "7": {
            "value": "Control subfield (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        # / "0": "Type of record",
        # / "1": "Bibliographic level",
        "8": {
            "value": "Field link and sequence numb",
            "term": CMT._SFCat_Part,
        },
    },
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
    "class": CMO.Organization,
    "first-indicator": {
        "0": {
            "value": "Inverted name",
            "term": CMT._SFCat_InvertedName,
        },
        "1": {
            "value": "Jurisdiction name",
            "term": CMT._SFCat_JurisdictionName,
        },
        "2": {
            "value": "Name in direct order",
            "term": CMT._NameInDirectOrder,
        }
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
        "a": {
            "value": "Corporate name or jurisdiction name as entry element (NR)",
            "term": CMT._SFCat_Name,
        },
        "b": {
            "value": "Subordinate unit (R)",
            "term": CMT._SFCat_SubordinateUnit,
        },
        "c": {
            "value": "Location of meeting (R)",
            "term": CMT._SFCat_Location,
        },
        "d": {
            "value": "Date of meeting or treaty signing (R)",
            "term": CMT._SFCat_AgentDate,
        },
        "e": {
            "value": "Relator term (R)",
            "term": CMT._SFCat_Relator,
        },
        "f": {
            "value": "Date of a work (NR)",
            "term": CMT._SFCat_WorkDate,
        },
        "g": {
            "value": "Miscellaneous information (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "k": {
            "value": "Form subheading (R)",
            "term": CMT._SFCat_Subtitle,
        },
        "l": {
            "value": "Language of a work (NR)",
            "term": CMT._SFCat_Language,
        },
        "n": {
            "value": "Number of part / section/meeting(R)",
            "term": CMT._SFCat_Part,
        },
        "p": {
            "value": "Name of part / section of a work(R)",
            "term": CMT._SFCat_Part,
        },
        "t": {
            "value": "Title of a work (NR)",
            "term": CMT._SFCat_Title,
        },
        "u": {
            "value": "Affiliation (NR)",
            "term": CMT._SFCat_Affiliation,
        },
        "0": {
            "value": "Authority record control number or standard number (R)",
            "term": CMT._SFCat_ExternalID,
        },
        "1": {
            "value": "Real World Object URI (R)",
            "term": CMT._SFCat_ExternalID,
        },
        "2": {
            "value": "Source of heading or term (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "4": {
            "value": "Relationship (R)",
            "term": CMT._SFCat_Relator,
        },
        "6": {
            "value": "Linkage (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "7": {
            "value": "Data provenance (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "8": {
            "value": "Field link and sequence number (R)",
            "term": CMT._SFCat_MiscInfo,
        },
    },
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
    "class": CMO.Person,
    "first-indicator": {
        "0": {
            "value": "Forename",
            "term": CMT._NameType_Forename,
        },
        "1": {
            "value": "Surname",
            "term": CMT._NameType_Surname,
        },
        "3": {
            "value": "Family name",
            "term": CMT._NameType_FamilyName,
        }
    },
    "second-indicator": {
        " ": "Undefined",
        "#": "Undefined",
    },
    "subfield-codes": {
        "a": {
            "value": "Personal name (NR)",
            "term": CMT._SFCat_Name,
        },
        "b": {
            "value": "Numeration (NR)",
            "term": CMT._SFCat_Appelation,
        },
        "c": {
            "value": "Titles and other words associated with a name (R)",
            "term": CMT._SFCat_Appelation,
        },
        "d": {
            "value": "Dates associated with a name (NR)",
            "term": CMT._SFCat_AgentDate,
        },
        "e": {
            "value": "Relator term (R)",
            "term": CMT._SFCat_Relator,
        },
        "f": {
            "value": "Date of a work (NR)",
            "term": CMT._SFCat_WorkDate,
        },
        "g": {
            "value": "Miscellaneous information (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "h": {
            "value": "Medium (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "j": {
            "value": "Attribution qualifier (R)",
            "term": CMT._SFCat_Appelation,
        },
        "k": {
            "value": "Form subheading (R)",
            "term": CMT._SFCat_Subtitle,
        },
        "l": {
            "value": "Language of a work (NR)",
            "term": CMT._SFCat_Language,
        },
        "m": {
            "value": "Medium of performance for music (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "n": {
            "value": "Number of part/ section of a work(R)",
            "term": CMT._SFCat_Part,
        },
        "o": {
            "value": "Arranged statement for music (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "p": {
            "value": "Name of part/section of a work(R)",
            "term": CMT._SFCat_Part,
        },
        "q": {
            "value": "Fuller form of name (NR)",
            "term": CMT._SFCat_AltName,
        },
        "r": {
            "value": "Key for music (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "s": {
            "value": "Version (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "t": {
            "value": "Title of a work (NR)",
            "term": CMT._SFCat_Title,
        },
        "u": {
            "value": "Affiliation (NR)",
            "term": CMT._SFCat_Affiliation,
        },
        "v": {
            "value": "Volume/sequential designation(NR)",
            "term": CMT._SFCat_Part,
        },
        "x": {
            "value": "International Standard Serial Number (NR)",
            "term": CMT._SFCat_ExternalID,
        },
        "y": {
            "value": "Data provenance (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "z": {
            "value": "Geographic subdivision (R)",
            "term": CMT._SFCat_Location,
        },
        "0": {
            "value": "Authority record control number or standard number (R)",
            "term": CMT._SFCat_ExternalID,
        },
        "1": {
            "value": "Real World Object URI (R)",
            "term": CMT._SFCat_ExternalID,
        },
        "2": {
            "value": "Source of heading or term (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "3": {
            "value": "Materials specified (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "4": {
            "value": "Relationship (R)",
            "term": CMT._SFCat_Relator,
        },
        "6": {
            "value": "Linkage (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "7": {
            "value": "Control subfield (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        # / "0": "Type of record",
        # / "1": "Bibliographic level",
        "8": {
            "value": "Field link and sequence numb",
            "term": CMT._SFCat_Part,
        },
    },
}

SEVENHUNDRED_CODES = {
    "class": CMO.Person,
    "first-indicator": {
        "0": {
            "value": "Forename",
            "term": CMT._NameType_Forename,
        },
        "1": {
            "value": "Surname",
            "term": CMT._NameType_Surname,
        },
        "3": {
            "value": "Family name",
            "term": CMT._NameType_FamilyName,
        }
    },
    "second-indicator": {
        "#": "No information provided",
        "2": "Analytical entry",
    },
    "subfield-codes": {
        "0": {
            "value": "Standard Number",
            "term": CMT._SFCat_ExternalID,
        },
        "1": {
            "value": "VIAF Number",
            "term": CMT._SFCat_ExternalID,
        },
        "4": {
            "value": "Relations",
            "term": CMT._SFCat_Relator,
        },
        "5": {
            "value": "Institution to which field applies",  # we may want save this one
            "term": CMT._SFCat_MiscInfo,
        },
        "a": {
            "value": "Name",
            "term": CMT._SFCat_Name,
        },
        "b": {
            "value": "Numeration",
            "term": CMT._SFCat_Appelation,
        },
        "c": {
            "value": "Associated Works",
            "term": CMT._SFCat_Title,
        },
        "d": {
            "value": "Dates",
            "term": CMT._SFCat_AgentDate,
        },
        "e": {
            "value": "Relator Term",
            "term": CMT._SFCat_Relator,
        },
        "f": {
            "value": "Date of a work",
            "term": CMT._SFCat_WorkDate,
        },
        "h": {
            "value": "Medium",
            "term": CMT._SFCat_MiscInfo,
        },
        "i": {
            "value": "relationship",
            "term": CMT._SFCat_Appelation,
        },
        "k": {
            "value": "Form Subheading",
            "term": CMT._SFCat_Subtitle,
        },
        "l": {
            "value": "Language of a work",
            "term": CMT._SFCat_language,
        },
        "m": {
            "value": "Medium of Performance",
            "term": CMT._SFCat_MiscInfo,
        },
        "n": {
            "value": "Number or Part",
            "term": CMT._SFCat_Part,
        },
        "o": {
            "value": "Arranged Statement",
            "term": CMT._SFCat_MiscInfo,
        },
        "p": {
            "value": "Name of part/section",
            "term": CMT._SFCat_Part,
        },
        "q": {
            "value": "Alt Name",
            "term": CMT._SFCat_AltName,
        },
        "r": {
            "value": "Key for Music",
            "term": CMT._SFCat_MiscInfo,
        },
        "t": {
            "value": "Title",
            "term": CMT._SFCat_Title,
        },
    },
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
SIXHUNDREDTEN_CODES = {
    "class": CMO.Organization,
    "first-indicator": {
        "0": {
            "value": "Inverted name",
            "term": CMT._SFCat_InvertedName,
        },
        "1": {
            "value": "Jurisdiction name",
            "term": CMT._SFCat_JurisdictionName,
        },
        "2": {
            "value": "Name in direct order",
            "term": CMT._NameInDirectOrder,
        }
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
        "a": {
            "value": "Corporate name or jurisdiction name as entry element (NR)",
            "term": CMT._SFCat_Name,
        },
        "b": {
            "value": "Subordinate unit (R)",
            "term": CMT._SFCat_SubordinateUnit,
        },
        "c": {
            "value": "Location of meeting (R)",
            "term": CMT._SFCat_Location,
        },
        "d": {
            "value": "Date of meeting or treaty signing (R)",
            "term": CMT._SFCat_AgentDate,
        },
        "e": {
            "value": "Relator term (R)",
            "term": CMT._SFCat_Relator,
        },
        "f": {
            "value": "Date of a work (NR)",
            "term": CMT._SFCat_WorkDate,
        },
        "g": {
            "value": "Miscellaneous information (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "h": {
            "value": "Medium (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "k": {
            "value": "Form subheading (R)",
            "term": CMT._SFCat_Subtitle,
        },
        "l": {
            "value": "Language of a work (NR)",
            "term": CMT._SFCat_Language,
        },
        "m": {
            "value": "Medium of performance for music (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "n": {
            "value": "Number of part / section/meeting(R)",
            "term": CMT._SFCat_Part,
        },
        "o": {
            "value": "Arranged statement for music (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "p": {
            "value": "Name of part / section of a work(R)",
            "term": CMT._SFCat_Part,
        },
        "r": {
            "value": "Key for music (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "s": {
            "value": "Version (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "t": {
            "value": "Title of a work (NR)",
            "term": CMT._SFCat_Title,
        },
        "u": {
            "value": "Affiliation (NR)",
            "term": CMT._SFCat_Affiliation,
        },
        "v": {
            "value": "Form subdivision (R)",
            "term": CMT._SFCat_Subtitle,
        },
        "x": {
            "value": "General subdivision (R)",
            "term": CMT._SFCat_Subdivision,
        },
        "y": {
            "value": "Chronological subdivision (R)",
            "term": CMT._SFCat_WorkDate,
        },
        "z": {
            "value": "Geographic subdivision (R)",
            "term": CMT._SFCat_Location,
        },
        "0": {
            "value": "Authority record control number or standard number (R)",
            "term": CMT._SFCat_ExternalID,
        },
        "1": {
            "value": "Real World Object URI (R)",
            "term": CMT._SFCat_ExternalID,
        },
        "2": {
            "value": "Source of heading or term (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "3": {
            "value": "Materials specified (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "4": {
            "value": "Relationship (R)",
            "term": CMT._SFCat_Relator,
        },
        "6": {
            "value": "Linkage (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "7": {
            "value": "Data provenance (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "8": {
            "value": "Field link and sequence number (R)",
            "term": CMT._SFCat_MiscInfo,
        },
    },
}

SIXHUNDREDELEVEN_CODES = {
    "class": CMO.Meeting,
    "first-indicator": {

        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order",
    },
    "second-indicator": {
        "0": "Library of Congress Subject Headings",
        "1": "Library of Congress Childrens and Young Adults Subject Headings",
        "2": "Medical Subject Headings",
        "3": "National Agricultural Library subject authority file",
        "4": "Source not specified",
        "5": "Canadian Subject Headings",
        "6": "Répertoire de vedettes-matière",
        "7": "Source specified in subfield $2"

    },
    "subfield-codes": {

        "a": {
            "value": "Meeting name or jurisdiction name as entry element (NR)",
            "term": CMT._SFCat_Name,
        },
        "c": {
            "value": "Location of meeting (R)",
            "term": CMT._SFCat_Location,
        },
        "d": {
            "value": "Date of meeting or treaty signing (R)",
            "term": CMT._SFCat_Date,
        },
        "e": {
            "value": "Subordinate unit (R)",
            "term": CMT._SFCat_SubordinateUnit,
        },
        "f": {
            "value": "Date of a work (NR)",
            "term": CMT._SFCat_WorkDate,
        },
        "g": {
            "value": "Miscellaneous information (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "h": {
            "value": "Medium (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "j": {
            "value": "Relator term (R)",
            "term": CMT._SFCat_Relator,
        },
        "k": {
            "value": "Form subheading (R)",
            "term": CMT._SFCat_Subtitle,
        },
        "l": {
            "value": "Language of a work (NR)",
            "term": CMT._SFCat_Language,
        },
        "n": {
            "value": "Number of part/section/meeting (R)",
            "term": CMT._SFCat_Part,
        },
        "p": {
            "value": "Name of part/section of a work (R)",
            "term": CMT._SFCat_Part,
        },
        "q": {
            "value": "Name of meeting following jurisdiction name entry element (NR)",
            "term": CMT._SFCat_JurisdictionName,
        },
        "s": {
            "value": "Version (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "t": {
            "value": "Title of a work (NR)",
            "term": CMT._SFCat_Title,
        },
        "u": {
            "value": "Affiliation (NR)",
            "term": CMT._SFCat_Affiliation,
        },
        "v": {
            "value": "Form subdivision (R)",
            "term": CMT._SFCat_Subtitle,
        },
        "x": {
            "value": "General subdivision (R)",
            "term": CMT._SFCat_Subdivision,
        },
        "y": {
            "value": "Chronological subdivision (R)",
            "term": CMT._SFCat_WorkDate,
        },
        "z": {
            "value": "Geographic subdivision (R)",
            "term": CMT._SFCat_Location,
        },
        "0": {
            "value": "Authority record control number or standard number (R)",
            "term": CMT._SFCat_ExternalID,
        },
        "1": {
            "value": "Real World Object URI (R)",
            "term": CMT._SFCat_ExternalID,
        },
        "2": {
            "value": "Source of heading or term (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "3": {
            "value": "Materials specified (NR)",
            "term": CMT._SFCat__MiscInfo,
        },
        "4": {
            "value": "Relationship (R)",
            "term": CMT._SFCat_Relator,
        },
        "6": {
            "value": "Linkage (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "7": {
            "value": "Data provenance (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "8": {
            "value": "Field link and sequence number (R)",
            "term": CMT._SFCat_MiscInfo,
        }
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
#
# Manuscripts are loacated in 710 field, but they have an $a, $k, and ($l or $n)
#
SEVENHUNDREDTEN_CODES = {
    "class": CMO.Organization,
    "first-indicator": {
        # Type of corporate name element
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
        "a": {
            "value": "Corporate name or jurisdiction name as entry element (NR)",
            "term": CMT._SFCat_Name,
        },
        "b": {
            "value": "Subordinate unit (R)",
            "term": CMT._SFCat_SubordinateUnit,
        },
        "c": {
            "value": "Location of meeting (R)",
            "term": CMT._SFCat_Location,
        },
        "d": {
            "value": "Date of meeting or treaty signing (R)",
            "term": CMT._SFCat_AgentDate,
        },
        "e": {
            "value": "Relator term (R)",
            "term": CMT._SFCat_Relator,
        },
        "f": {
            "value": "Date of a work (NR)",
            "term": CMT._SFCat_WorkDate,
        },
        "g": {
            "value": "Miscellaneous information (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "h": {
            "value": "Medium (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "i": {
            "value": "Relationship information (R)",
            "term": CMT._SFCat_Relator,
        },
        "k": {
            "value": "Form subheading (R)",
            "term": CMT._SFCat_Subtitle,
        },
        "l": {
            "value": "Language of a work (NR)",
            "term": CMT._SFCat_Language,
        },
        "m": {
            "value": "Medium of performance for music (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "n": {
            "value": "Number of part/section/meeting (R)",
            "term": CMT._SFCat_Part,
        },
        "o": {
            "value": "Arranged statement for music (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "p": {
            "value": "Name of partsection of a work (R)",
            "term": CMT._SFCat_Part,
        },
        "r": {
            "value": "Key for music (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "s": {
            "value": "Version (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "t": {
            "value": "Title of a work (NR)",
            "term": CMT._SFCat_Title,
        },
        "u": {
            "value": "Affiliation (NR)",
            "term": CMT._SFCat_Affiliation,
        },
        "x": {
            "value": "International Standard Serial Number (NR)",
            "term": CMT._SFCat_ExternalID,
        },
        "0": {
            "value": "Authority record control number or standard number (R)",
            "term": CMT._SFCat_ExternalID,
        },
        "1": {
            "value": "Real World Object URI (R)",
            "term": CMT._SFCat_ExternalID,
        },
        "2": {
            "value": "Source of heading or term (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "3": {
            "value": "Materials specified (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "4": {
            "value": "Relationship (R)",
            "term": CMT._SFCat_Relator,
        },
        "5": {
            "value": "Institution to which field applies (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "6": {
            "value": "Linkage(NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "7": {
            "value": "Data provenance (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "8": {
            "value": "Field link and sequence number (R)",
            "term": CMT._SFCat_MiscInfo,
        },
    },
}

# 711
# Added entry in which the entry element is a meeting name.
#
# Added entries are assigned according to various cataloging rules to give
# access to the bibliographic record from meeting or conference name headings
# which may not be more appropriately assigned as 611 (Subject Added Entry-
# Meeting Name) or 811 (Series Added Entry-Meeting Name) fields.

SEVENHUNDREDELEVEN_CODES = {
    "class": CMO.Meeting,
    "first-indicator": {

        "0": "Inverted name",
        "1": "Jurisdiction name",
        "2": "Name in direct order",
    },
    "second-indicator": {
        "#": "No information provided",
        "2": "Analytical Entry",

    },
    "subfield-codes": {

        "a": {
            "value": "Meeting name or jurisdiction name as entry element (NR)",
            "term": CMT._SFCat_Name,
        },
        "c": {
            "value": "Location of meeting (R)",
            "term": CMT._SFCat_Location,
        },
        "d": {
            "value": "Date of meeting or treaty signing (R)",
            "term": CMT._SFCat_Date,
        },
        "e": {
            "value": "Subordinate unit (R)",
            "term": CMT._SFCat_SubordinateUnit,
        },
        "f": {
            "value": "Date of a work (NR)",
            "term": CMT._SFCat_WorkDate,
        },
        "g": {
            "value": "Miscellaneous information (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "h": {
            "value": "Medium (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "i": {
            "value": "Relationship information",
            "term": CMT._SFCat_Relator
        },
        "j": {
            "value": "Relator term (R)",
            "term": CMT._SFCat_Relator,
        },
        "k": {
            "value": "Form subheading (R)",
            "term": CMT._SFCat_Subtitle,
        },
        "l": {
            "value": "Language of a work (NR)",
            "term": CMT._SFCat_Language,
        },
        "n": {
            "value": "Number of part/section/meeting (R)",
            "term": CMT._SFCat_Part,
        },
        "p": {
            "value": "Name of part/section of a work (R)",
            "term": CMT._SFCat_Part,
        },
        "q": {
            "value": "Name of meeting following jurisdiction name entry element (NR)",
            "term": CMT._SFCat_JurisdictionName,
        },
        "s": {
            "value": "Version (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "t": {
            "value": "Title of a work (NR)",
            "term": CMT._SFCat_Title,
        },
        "u": {
            "value": "Affiliation (NR)",
            "term": CMT._SFCat_Affiliation,
        },
        "x": {
            "value": "General subdivision (R)",
            "term": CMT._SFCat_Subdivision,
        },
        "0": {
            "value": "Authority record control number or standard number (R)",
            "term": CMT._SFCat_ExternalID,
        },
        "1": {
            "value": "Real World Object URI (R)",
            "term": CMT._SFCat_ExternalID,
        },
        "2": {
            "value": "Source of heading or term (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "3": {
            "value": "Materials specified (NR)",
            "term": CMT._SFCat__MiscInfo,
        },
        "4": {
            "value": "Relationship (R)",
            "term": CMT._SFCat_Relator,
        },
        "5": {
            "value": "Institution to which field applies (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "6": {
            "value": "Linkage (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "7": {
            "value": "Data provenance (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "8": {
            "value": "Field link and sequence number (R)",
            "term": CMT._SFCat_MiscInfo,
        }
    }

}
# 800
# FIELD DEFINITION AND SCOPE
# Author/title series added entry in which the author portion is a personal
# name.
#
# An 800 field is usually justified by a series statement (field 490) or a
# general note (field 500) relating to the series. For reproductions, it may be
# justified by a series statement in subfield $f of field 533 (Reproduction
# Note).
EIGHTHUNDRED_CODES = {
    "class": CMO.Person,
    "first-indicator": {
        "0": {
            "value": "Forename",
            "term": CMT._NameType_Forename,
        },
        "1": {
            "value": "Surname",
            "term": CMT._NameType_Surname,
        },
        "3": {
            "value": "Family name",
            "term": CMT._NameType_FamilyName,
        }
    },
    "second-indicator": {
        " ": "Undefined",
        "#": "Undefined",
    },
    "subfield-codes": {
        "a": {
            "value": "Personal name (NR)",
            "term": CMT._SFCat_Name,
        },
        "b": {
            "value": "Numeration (NR)",
            "term": CMT._SFCat_Appelation,
        },
        "c": {
            "value": "Titles and other words associated with a name (R)",
            "term": CMT._SFCat_Appelation,
        },
        "d": {
            "value": "Dates associated with a name (NR)",
            "term": CMT._SFCat_AgentDate,
        },
        "e": {
            "value": "Relator term (R)",
            "term": CMT._SFCat_Relator,
        },
        "f": {
            "value": "Date of a work (NR)",
            "term": CMT._SFCat_WorkDate,
        },
        "g": {
            "value": "Miscellaneous information (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "h": {
            "value": "Medium (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "j": {
            "value": "Attribution qualifier (R)",
            "term": CMT._SFCat_Appelation,
        },
        "k": {
            "value": "Form subheading (R)",
            "term": CMT._SFCat_Subtitle,
        },
        "l": {
            "value": "Language of a work (NR)",
            "term": CMT._SFCat_Language,
        },
        "m": {
            "value": "Medium of performance for music (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "n": {
            "value": "Number of part/ section of a work(R)",
            "term": CMT._SFCat_Part,
        },
        "o": {
            "value": "Arranged statement for music (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "p": {
            "value": "Name of part/section of a work(R)",
            "term": CMT._SFCat_Part,
        },
        "q": {
            "value": "Fuller form of name (NR)",
            "term": CMT._SFCat_AltName,
        },
        "r": {
            "value": "Key for music (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "s": {
            "value": "Version (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "t": {
            "value": "Title of a work (NR)",
            "term": CMT._SFCat_Title,
        },
        "u": {
            "value": "Affiliation (NR)",
            "term": CMT._SFCat_Affiliation,
        },
        "v": {
            "value": "Volume/sequential designation(NR)",
            "term": CMT._SFCat_Part,
        },
        "w": {
            "value": "Bibliographic record control number (R)",
            "term": CMT._SFCat_ExternalID,
        },
        "x": {
            "value": "International Standard Serial Number (NR)",
            "term": CMT._SFCat_ExternalID,
        },
        "y": {
            "value": "Data provenance (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "0": {
            "value": "Authority record control number or standard number (R)",
            "term": CMT._SFCat_ExternalID,
        },
        "1": {
            "value": "Real World Object URI (R)",
            "term": CMT._SFCat_ExternalID,
        },
        "2": {
            "value": "Source of heading or term (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "3": {
            "value": "Materials specified (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "4": {
            "value": "Relationship (R)",
            "term": CMT._SFCat_Relator,
        },
        "5": {
            "value": "Institution to which field applies (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "6": {
            "value": "Linkage (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "7": {
            "value": "Control subfield (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        # / "0": "Type of record",
        # / "1": "Bibliographic level",
        "8": {
            "value": "Field link and sequence numb",
            "term": CMT._SFCat_Part,
        },
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
    "class": CMO.Organization,
    "first-indicator": {
        "0": {
            "value": "Inverted name",
            "term": CMT._SFCat_InvertedName,
        },
        "1": {
            "value": "Jurisdiction name",
            "term": CMT._SFCat_JurisdictionName,
        },
        "2": {
            "value": "Name in direct order",
            "term": CMT._NameInDirectOrder,
        }
    },
    "second-indicator": {
        "#": "Undefined",
    },
    "subfield-codes": {
        "a": {
            "value": "Corporate name or jurisdiction name as entry element (NR)",
            "term": CMT._SFCat_Name,
        },
        "b": {
            "value": "Subordinate unit (R)",
            "term": CMT._SFCat_SubordinateUnit,
        },
        "c": {
            "value": "Location of meeting (R)",
            "term": CMT._SFCat_Location,
        },
        "d": {
            "value": "Date of meeting or treaty signing (R)",
            "term": CMT._SFCat_AgentDate,
        },
        "e": {
            "value": "Relator term (R)",
            "term": CMT._SFCat_Relator,
        },
        "f": {
            "value": "Date of a work (NR)",
            "term": CMT._SFCat_WorkDate,
        },
        "g": {
            "value": "Miscellaneous information (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "h": {
            "value": "Medium (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "i": {
            "value": "Relationship information (R)",
            "term": CMT._SFCat_Relator,
        },
        "k": {
            "value": "Form subheading (R)",
            "term": CMT._SFCat_Subtitle,
        },
        "l": {
            "value": "Language of a work (NR)",
            "term": CMT._SFCat_Language,
        },
        "m": {
            "value": "Medium of performance for music (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "n": {
            "value": "Number of part/section/meeting (R)",
            "term": CMT._SFCat_Part,
        },
        "o": {
            "value": "Arranged statement for music (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "p": {
            "value": "Name of partsection of a work (R)",
            "term": CMT._SFCat_Part,
        },
        "r": {
            "value": "Key for music (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "s": {
            "value": "Version (R)",
            "term": CMT._SFCat_MiscInfo,
        },
        "t": {
            "value": "Title of a work (NR)",
            "term": CMT._SFCat_Title,
        },
        "u": {
            "value": "Affiliation (NR)",
            "term": CMT._SFCat_Affiliation,
        },
        "v": {
            "value": "Volume/sequential designation (NR)",
            "term": CMT._SFCat_Part,
        },
        "w": {
            "value": "Bibliographic record control number (R)",
            "term": CMT._SFCat_ExternalID,
        },
        "x": {
            "value": "International Standard Serial Number (NR)",
            "term": CMT._SFCat_ExternalID,
        },
        "y": {
            "value": "Data provenance (R",
            "term": CMT._SFCat_MiscInfo,
        },
        "0": {
            "value": "Authority record control number or standard number (R)",
            "term": CMT._SFCat_ExternalID,
        },
        "1": {
            "value": "Real World Object URI (R)",
            "term": CMT._SFCat_ExternalID,
        },
        "2": {
            "value": "Source of heading or term (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "3": {
            "value": "Materials specified (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "4": {
            "value": "Relationship (R)",
            "term": CMT._SFCat_Relator,
        },
        "5": {
            "value": "Institution to which field applies (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "6": {
            "value": "Linkage(NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "7": {
            "value": "Control subfield (NR)",
            "term": CMT._SFCat_MiscInfo,
        },
        "8": {
            "value": "Field link and sequence number (R)",
            "term": CMT._SFCat_MiscInfo,
        },
    },
}
