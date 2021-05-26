import json

employee = dict(name='Artem', age=35, child=['Eva', 'Artemovna'], wife=['Daria', 'Sergeevna', 'Alekseeva'])

with open('JSON.json', 'w') as newJson:  # Диспетчер контекста гарантирует закрыте файла
    json.dump(employee, newJson, indent=4)  # indent - создает отступы

if newJson.closed:
    print('is closed')
print(json.load(open('JSON.json')))
