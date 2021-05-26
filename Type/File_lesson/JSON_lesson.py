import json

employee = dict(name='Artem', age=35, child=['Eva', 'Artemovna'], wife=['Daria', 'Sergeevna', 'Alekseeva'])

with open('JSON.json', 'w') as newJson:
    json.dump(employee, newJson, indent=4)  # indent - создает отступы
newJson.close()

print(json.load(open('JSON.json')))
