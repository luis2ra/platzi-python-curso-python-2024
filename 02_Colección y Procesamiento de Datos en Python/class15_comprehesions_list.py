squares = [x**2 for x in range(1, 11)]
print("Cuadrados del 1 al 10:", squares)

celsius = [0, 10, 20, 30, 40]
print("Temperaturas en °C:", celsius)
fahrenheit = [(temp * 9 / 5) + 32 for temp in celsius]
print("Temperaturas en °F:", fahrenheit)

# Numeros pares
evens = [x for x in range(1, 21) if x % 2 == 0]
print("Evens numbers: ", evens)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(matrix)
print(transposed)
print()

transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
