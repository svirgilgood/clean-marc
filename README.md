# clean-marc

[![PyPI - Version](https://img.shields.io/pypi/v/clean-marc.svg)](https://pypi.org/project/clean-marc)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/clean-marc.svg)](https://pypi.org/project/clean-marc)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)
- [Usage](#usage)
- [Additions](#additions)

## Installation

1. Clone the repository and navigate into the directory

2. Create a virtual environment

```console
python3.13 -m venv .clean-venv
```

3. Source the virtual environment

```cosnole
source .clean_venv/bin/activate
```
4. Install the dependencies and the package
```console
pip install .
```
Or, use this command to make the package more reliably upgradable
```console
pip install -e .
```

## Usage


The command works by taking either a MARCXML file as an argument,  or a spread
sheet that has a column `OCLC number` where the MARCXML can be downloaded from
a file.

### Configuration

Create a file `.env` in the root of the project with the format:
```
NAME = "SomeName"
KEY = "SomeKey"
SECRET = "SomeSecret"
```
These secrets will be used to authenticate against OCLC to retrieve Marc Records.

### Basic Usage

```console
usage: clean-marc [-h] {init,sparql-anything,records} ...

options:
  -h, --help            show this help message and exit

subcommands:
  subcommands

  {init,sparql-anything,records}
                        find out more about each of the subcommands by passing -h/--help flag to them
    init                1. init: This command runs the initial import of the xml or worldcat oclc numbers creates a bibframe turtle file that has some additional cleaning and initial step and creates some
                        inference for new classes, and generates the associated data for import. (Agents, Locations, Topics).
    sparql-anything     2. sparql-anything subcommand takes arguments based on the agents, places, or topics that were created by the init command. The output is a set of turtle files that can then be added to
                        the data sources for the records subcommand that can be integrated into how the records and bibliography are created.
    records             3. records: This produces the final export of the record items to be imported. These are the main records for the items (either resources or bibliographic records) which link to the values
                        and have the import metadata from the bibliographic records.

The commands are intended to be run in the following order: 1. init; 2. sparql-anything; 3. records
usage: clean_marc [-h] [-o [OUTPUT]] [-w [WORLDCAT]] [-x [SAVE_XML]] [-q [QUERY]] [--include-closures] [marc_files ...]
```

### Downloading from Worldcat

If the Worldcat spreadsheet has a column `UUID`, a UUID column will be added
to the bibliographic resource spreadsheet.

The `--save-xml` option is helpful for storing the XML file downloaded from
Worldcat so that a fresh request is not required on every attempt, and to
verify the output.

To specify the column in the worldcat spreadsheet that has the OCLC numbers, pass
the column header in with the `-n|--oclc-numbers` flag. The default is "OCLC Number
(digital)"

### Extracting from an MARCXML Files

To extract from a single MarcXML file, or a set of MarcXML files, add them as
arguments.

## Additions

To expand and adapt the script to a new set of data, one can leverage and
expand the queries and cleaning functions.

### Queries

The script converts the MARCXML into Bibframe RDF, which is then queried
against the `rdflib` triple store.

Additional queries can be added in the `src/clean-marc/queries` directory. The
queries are SPARQL Select queries, and a spreadsheet file will be generated in
the directory with the same base name as the query.

### Processing Functions

In some cases, additional functions are useful for processing certain columns.

By convention these will begin with an underscore in the sparql query, and then
will be added to the `cleaning_functions` dictionary in the
`src/clean_marc/utils.py` file.

Functions in the `cleaning_functions` object need to take a `pd.Series`
argument, and return a `pd.Series`.

There is also a `**kwargs` argument. Currently all that is passed in as a
`kwarg` is the worldcat spreadsheet.

## License

`clean-marc` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

