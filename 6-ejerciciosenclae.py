def calcular_factorial(numero):
    factorial = 1
    # Verificar si el número es negativo
    if numero < 0:
        return "El factorial no está definido para números negativos."
    # Calcular el factorial
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número entero no negativo para calcular su factorial: "))

# Llamar a la función y mostrar el resultado
print("El factorial de", numero, "es:", calcular_factorial(numero))
