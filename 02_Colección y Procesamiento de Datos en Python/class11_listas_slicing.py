a = [1, 2, 3, 4, 5]
b = a  # esta es una asignación por referencia, apuntan a la misma dirección de memoria
print(a)
print(b)
del a[0]
print(id(a))
print(id(b))

print()

c = a[:]  # esta es una asignación por valor, se crea una copia de la lista
print(id(a))
print(id(b))
print(id(c))
a.append(6)
print(a)
print(b)
print(c)
