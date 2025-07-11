import csv

# Leer un archivo
with open("class31_products.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)  # El tipo de cada fila es un diccionario

# Mostrar la información por columnas
# with open("class31_products.csv", mode="r") as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         print(f"Producto: {row['name']}, Precio: {row['price']}")
