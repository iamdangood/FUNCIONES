def imprimir_pares(lista):
    print("Números pares:")
    for numero in lista:
        if numero % 2 == 0:
            print(numero)

# Ejemplo de uso
imprimir_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
