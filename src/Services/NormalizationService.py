def normalizeResults(results):
    for test in results["tests"]:
        for param in test["parameters"]:
            if param["result"] is not None:
                lower_limit = param["lowerLimit"]
                upper_limit = param["upperLimit"]
                value = param["result"]
                if lower_limit in [-1, None] and upper_limit in [-1, None]:
                    continue
                while upper_limit not in [-1, None] and abs(upper_limit - value) > abs((value * 10) - upper_limit):
                    value *= 10
                while lower_limit not in [-1, None] and abs(lower_limit - value) > abs((value * 10) - lower_limit):
                    value *= 10
                param["result"] = value
                if param["result"]<lower_limit:
                    param["remarks"]="Deficient"
                elif param["result"]>upper_limit:
                    param["remarks"]="Excess"
                else:
                    param["remarks"]="Normal"


