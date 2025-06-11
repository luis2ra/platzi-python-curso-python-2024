def factorial(n):
    """
    Calcula el factorial de un número entero n utilizando recursión.

    :param n: Número entero no negativo
    :return: Factorial de n
    """
    if n < 0:
        raise ValueError("El número debe ser no negativo")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Ejemplo de uso
try:
    num = int(input("Ingrese un número entero no negativo: "))
    result = factorial(num)
    print(f"El factorial de {num} es {result}")
except ValueError as e:
    print(f"Error: {e}")
