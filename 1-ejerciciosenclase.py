def encontrar_maximo():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))

    # Encontrar el máximo utilizando la función max()
    maximo = max(num1, num2, num3)
    
    # Mostrar el resultado
    print("El máximo de los tres números es:", maximo)

# Llamar a la función para probarla
encontrar_maximo()
