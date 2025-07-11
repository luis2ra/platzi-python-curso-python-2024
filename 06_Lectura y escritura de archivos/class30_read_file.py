# Leer un archivo línea por línea
with open("class30_cuento-caperucita.txt", "r") as file:
    for lineas in file:
        print(lineas.strip())

# Leer todas las líneas en una lista
# with open("class30_cuento-caperucita.txt", "r") as file:
#     lines = file.readlines()
#     print(lines)

# Añadir texto
# with open("class30_cuento-caperucita.txt", "a") as file:
#     file.write("\n\nBy:ChatGPT")

# Sobreescribir el texto
# with open("class30_cuento-caperucita2.txt", "w") as file:
#     file.write("\n\nBy:ChatGPT")


# El reto de contar las lineas del archivo
with open("class30_cuento-caperucita.txt", "r") as file:
    contador = 0
    for lineas in file:
        contador += 1
    print(f"El archivo tiene {contador} líneas.")

# Otra forma de contar las líneas
with open("class30_cuento-caperucita.txt", "r") as file:
    lines = file.readlines()
    print(f"El archivo tiene {len(lines)} líneas.")

# Otra forma de contar las líneas con list comprehension
with open("class30_cuento-caperucita.txt", "r") as file:
    contador = sum(1 for _ in file)
    print(f"El archivo tiene {contador} líneas.")
