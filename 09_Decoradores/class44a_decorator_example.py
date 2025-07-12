def mi_decorador(funcion):
    def nueva_funcion(parametro):
        # Código que se ejecuta antes de llamar a la función original
        print("Antes de ejecutar la función")

        # Llamada a la función original con el parámetro recibido
        funcion(parametro)

        # Código que se ejecuta después de llamar a la función original
        print("Después de ejecutar la función")

    return nueva_funcion


@mi_decorador  # Aplicamos el decorador usando @
def mi_funcion(parametro):
    # Función original que será decorada
    print(f"Ejecutando la función con el parámetro: {parametro}")


# Ejemplo de uso
mi_funcion("Ejemplo")
