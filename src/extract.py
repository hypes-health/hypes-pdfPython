from Entity.ParametersList import parameters
from Entity.limits import limits
for key in parameters:
    for keyy in parameters[key]:
        if(len(limits[key][keyy])>0):
    print(f'"{key}",')