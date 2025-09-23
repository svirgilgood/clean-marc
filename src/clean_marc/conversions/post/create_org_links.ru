PREFIX bf: <http://id.loc.gov/ontologies/bibframe/>
PREFIX bflc: <http://id.loc.gov/ontologies/bflc/>
PREFIX cc: <http://creativecommons.org/ns#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX madsrdf: <http://www.loc.gov/mads/rdf/v1#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX xs: <http://www.w3.org/2001/XMLSchema#>
PREFIX cmo: <http://svirgilgood.github.io/clean_marc/onto/>
PREFIX cmd: <http://svirgilgood.github.io/clean_marc/data/>



INSERT {
#CONSTRUCT {
  ?orgIRI
    a cmo:Agent , cmo:Organization ;
    rdfs:label ?organizationLabel ;
    .
  ?manuscript
    cmo:belongsTo ?orgIRI ;
  .
}
#SELECT ?manuscript ?fieldNumber ?organizationLabel
WHERE {
#  VALUES ?fieldNumber {
#    "710"
#    "810"
#  }
  ?manuscript
    a cmo:ManuscriptResource ;
      cmo:hasMarcField ?marcField ;
  .

  ?marcField
    cmo:fieldNumber ?fieldNumber ;
    cmo:hasPart [
      cmo:hasCode "a" ;
      cmo:hasValue ?organizationLabel ;
    ] ;
  .

  FILTER(REGEX(?fieldNumber, "710") || REGEX(?fieldNumber, "810"))
  BIND(IRI(CONCAT(str(cmd:), "_Agent_", SUBSTR(SHA256(?organizationLabel), 1, 18))) AS  ?orgIRI)

}
