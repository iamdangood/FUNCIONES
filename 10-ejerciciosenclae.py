def es_primo(numero):
    if numero < 2:
        return False
    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False
    return True

# Ejemplo de uso
numero = int(input("Ingrese un número entero positivo: "))

if es_primo(numero):
    print("El número", numero, "es primo.")
else:
    print("El número", numero, "no es primo.")
