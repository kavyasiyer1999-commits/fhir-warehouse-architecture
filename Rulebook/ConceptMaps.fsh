ConceptMap: GenderMap
Id: gender-map
Title: "Legacy Gender to FHIR Gender Mapping"
Source: http://legacy.codes/gender
Target: http://hl7.org/fhir/administrative-gender

* group[0].element[0].code = #M
* group[0].element[0].target.code = #male

* group[0].element[1].code = #F
* group[0].element[1].target.code = #female
