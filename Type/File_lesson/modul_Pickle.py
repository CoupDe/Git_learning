import pickle
# Запись в файл структур объектов
d = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f'}
dstr = {'1', '2', '3', '4', '5', '6'}
l = [1, 2, 3, 4, 5, 6]
lstr = ['1', '2', '3', '4', '5', '6']
ll=[]
ll.append(d), ll.append(dstr), ll.append(l), ll.append(lstr)
with open('modul_Pickle.txt', 'wb') as newfile:
    for item in ll:
        pickle.dump(ll, newfile)

newfile.close()

fopenname = open('modul_Pickle.txt', 'rb')
E = pickle.load(fopenname)
print(E)