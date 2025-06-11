# Iterar en cadenas
#Creando la cadena
text = "Hola mundo"
#Creando el iterador
iter_text = iter(text)

print("checking iterador")
print(type(iter_text))

#Iterar en la cadena
for char in iter_text:
    print(char)

