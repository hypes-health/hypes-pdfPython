from Services.ReportService import ExtractReport
from Services.GenderService import getGender
from Services.AgeService import getAge
from Entity.ParametersList import parameters
from Entity.limits import limits
from Services.NormalizationService import normalizeResults

def pdf(pdf_path):
    try:
        response=ExtractReport(pdf_path)
        if "gender" not in response:
            response["gender"]='M'
        if "age" not in response:
            response["age"] = "N/A"
        if "name" not in response:
            response["name"] = "N/A"
        if "reportedOn" not in response:
            response["reportedOn"] = 'N/A'
        results = {
            "name": response["name"],
            "sex": response["gender"][0].upper(),
            "age": response["age"],
            "reportedOn": response["reportedOn"],
            "tests": []
        }
        testParameters=[]
        cn=0;
        for test in parameters:
            result = {}
            result_temp={"name": test, "parameters": []}
            for key in parameters[test]:
                if (key in limits) and (key in response) and (type(response[key]) != type("abcd")):
                    cn=cn+1
                    result_temp["parameters"].append({
                    "name":key,
                    "unit": limits[key]["unit"],
                    "upperLimit": limits[key][results["sex"]]["upper"],
                    "lowerLimit": limits[key][results["sex"]]["lower"],
                    "result": response[key],
                    "remarks": None
                })
            if len(result_temp["parameters"])>0:
                testParameters.append(result_temp)
        results["tests"] = testParameters
        normalizeResults(results)
        if results["sex"].upper()== 'M':
            results["sex"]="Male"
        else:
            results["sex"]="Female"
        print(results,cn)
        return results
    except Exception as e:
        print(e)