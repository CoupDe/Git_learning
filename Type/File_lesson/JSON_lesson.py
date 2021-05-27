import json

employee = dict(name='Artem', age=35, child=['Eva', 'Artemovna'], wife=dict(
    name='Daria', secondname='Sergeevna', lastname='Alekseeva'))

with open('JSON.json', 'w') as newJson:
    if newJson.closed:
        print('is closed')  # Диспетчер контекста гарантирует закрыте файла
    else:
        print('no close')
    json.dump(employee, newJson, indent=4)  # indent - создает отступы

if newJson.closed:
    print('is closed')
loadDB = json.load(open('JSON.json'))
print(loadDB['wife']['lastname'])
