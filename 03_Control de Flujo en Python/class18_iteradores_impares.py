# Crear un iterador para los numeros impares

#Limite
limit = 10

#Crear iterador
odd_itter = iter(range(1,limit+1,2))


print("checking iterador")
print(type(odd_itter))


#Usar el iterador
for num in odd_itter:
    print(num)