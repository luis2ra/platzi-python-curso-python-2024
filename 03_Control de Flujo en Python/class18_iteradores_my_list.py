# Ejemplo de iterador

#Crear una lista
my_list = [1,2,3,4]

#Obtener el iterador
my_iter = iter(my_list)


print("checking iterador")
print(type(my_list))
print(type(my_iter))


#Usar el iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#print(next(my_iter))