from Services.ValueService import getValues
from Services.GenderService import getGender
from Services.AgeService import getAge
from Entity.ParametersList import parameters
from Entity.limits import limits
from Services.NormalizationService import normalizeResults

def pdf(pdf_path):
    results = {
        "name": "N/A",
        "sex": getGender(pdf_path),
        "age": getAge(pdf_path),
        "reportedOn": "N/A",
        "tests": []
    }

    for test in parameters:
        result = {}
        for key in parameters[test]["parameters"]:
            result[key]=None
        getValues(
            pdf_path, parameters[test]["names"],
            parameters[test]["parameters"],
            parameters[test]["pages"],result)
        result_temp={"name": test, "parameters": []}
        for key in parameters[test]["parameters"]:
            result_temp["parameters"].append({
                "name":key,
                "unit": limits[key]["unit"],
                "upperLimit": limits[key][results["sex"]]["upper"],
                "lowerLimit": limits[key][results["sex"]]["lower"],
                "result": result[key],
                "remarks": None
            })
        results["tests"].append(result_temp)
    normalizeResults(results)
    if results["sex"]== 'M':
        results["sex"]="Male"
    else:
        results["sex"]="Female"
    return results
