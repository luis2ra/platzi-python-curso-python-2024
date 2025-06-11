numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    print("Aquí i es igual a:",i+1)

for i in range(3,10):
    print(i)

print("Rango de 12 a 2, el step es -2")
for i in range(12,2,-2):
    print(i)

fruits = ["Manzana", "Pera", "Uva", "Naranja", "Tomate"]
for fruit in fruits:
    print(fruit)
    if fruit == "Naranja":
        print("Naranja encontrada")

x = 0
while x<5:
    if x ==3:
        break
    print(x) 
    x +=1

numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    if i ==3:
        continue
    print("Aquí i es igual a:",i)