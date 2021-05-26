import json

employee = dict(name='Artem', age=35, child=['Eva', 'Artemovna'], wife=['Daria', 'Sergeevna', 'Alekseeva'])

with open('JSON.json', 'a') as newJson:
    json.dump(employee, newJson, indent=4)
