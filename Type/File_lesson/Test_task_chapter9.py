import copy  # Модуль copy позволяет сделать копию всех вложений

x = [1, [1, dict(v='v', n='n'), 4], 3]
t = ('x', x[:], 'z')  # При копировании списка при помощи среза или copy(x) созданется копия верхнего уровня
d = dict(x=copy.deepcopy(x), y='y', z='z')
zz = d.copy()
print(x)
print(t)
print(d)
print(zz)
x[1][1] = 5555
print(x)
print(t)
print(d)
print(zz)
