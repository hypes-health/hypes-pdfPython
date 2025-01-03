from openai import OpenAI
from Entity.params import prms
from Entity.params import prmss
client = OpenAI(
        api_key="<API-KEY>"
    )
def Gpt(message):
    try:
        message=f" take {prms} as new list and {prmss} as old list go through matching parameters with similar names full forms short forms and give me parameters which are in old list ut not in new list"
        print(message)
        completion = client.chat.completions.create(
            model="chatgpt-4o-latest",
            messages=[
                {"role": "user",
                 "content": f'{message}'}]

            # "content": f'{text} save this as blood report and after trying to orient in proper way search for all parameters which have values (there could be 2 values in single row check for everything using orientation, headings and subheadings), use sub headings to define parameter name clearly, show me which are found as single python list of names and no other text'}]
            # f'then search for every parameters one by one in sequence from parameters list in report if found parameter with same meaning, full form, short form and not null value found then give all that names from parameters list in json result ignoring all other text or char just the json'}]
            # f'add parameter in final result json with exact name as mentioned in parameters list, strictly dont add parameters which are not mentioned in parameters list carefully, ignoring all other text or char just the json'}]
        )
        demoo = completion.choices[0].message.content
        print(demoo)
        return demoo
    except Exception as e:
        return e.toString()


