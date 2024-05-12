def es_palindromo(cadena):
    # Eliminar los espacios en blanco y convertir la cadena a minúsculas
    cadena = cadena.lower()
    # Verificar si la cadena es igual a su reverso
    return cadena == cadena[::-1]

# Ejemplo de uso
cadena = input("Ingrese una palabra o frase: ")
if es_palindromo(cadena):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
