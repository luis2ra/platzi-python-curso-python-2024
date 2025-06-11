def my_generator():
    print("Generador iniciado")
    yield 1
    print("Generador en pausa")
    yield 2
    print("Generador en pausa")
    yield 3
    print("Generador finalizado")


for value in my_generator():
    print("Valor generado:", value)
