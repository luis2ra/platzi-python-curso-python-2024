import json

# Lectura del archivo
with open("class32_products.json", mode="r") as file:
    products = json.load(file)

# Mostrar el contenido
for product in products:
    print(product)
    # print(f"Product: {product['name']}, Price: {product['price']}")
