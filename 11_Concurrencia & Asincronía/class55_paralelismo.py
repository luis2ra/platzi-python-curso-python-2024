import multiprocessing
import time


# Función que calcule el cuadrado de un número
def calculate_square(n):
    print(f"Calculando el cuadrado de {n}")
    # Simular un cálculo intensivo
    time.sleep(n)
    return n * n


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    # crear un pool
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_square, numbers)

    print(f"Resultados: {results}")
