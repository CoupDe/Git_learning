input = [x for x in open('test.txt', encoding='utf8')] # Создание списка из строк файла
alltext = (open('test.txt', 'r', encoding='utf8')).read() # Чтение всего фала как текст
with open('writefile.txt', 'a') as newfile:  # Запись в файл из списка
    for item in input[:3]:
        newfile.write(item)
newfile.close()
print(input)
print()