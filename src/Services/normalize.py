def normalizeResults(results):
    for param in results["parameters"]:
        if results["parameters"][param]["value"] is not None:
            lower_limit = results["parameters"][param]["lower_limit"]
            upper_limit = results["parameters"][param]["upper_limit"]
            value = results["parameters"][param]["value"]
            if lower_limit in [-1, None] and upper_limit in [-1, None]:
                continue
            while upper_limit not in [-1, None] and abs(upper_limit - value) > abs((value * 10) - upper_limit):
                value *= 10
            while lower_limit not in [-1, None] and abs(lower_limit - value) > abs((value * 10) - lower_limit):
                value *= 10
            results["parameters"][param]["value"] = value
