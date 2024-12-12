from Services.ValueService import getValues
from Services.GenderService import getGender
from Services.AgeService import getAge
from Entity.ParametersList import parameters
from Entity.limits import limits
from Entity.result import results
from Services.NormalizationService import normalizeResults

def pdf(pdf_path):


    results["gender"]=getGender(pdf_path)
    results["age"]=getAge(pdf_path)
    for test in parameters:
        for key in parameters[test]["parameters"]:
            results["parameters"][key]={
                "value":None,
                "upperLimit":limits[key][results["gender"]]["upper"],
                "lowerLimit":limits[key][results["gender"]]["lower"],
                "unit":limits[key]["unit"]
            }
    for test in parameters:
        getValues(
            pdf_path, parameters[test]["names"],
            parameters[test]["parameters"],
            parameters[test]["pages"])
    normalizeResults(results)
    return results
