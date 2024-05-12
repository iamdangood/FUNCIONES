def contar_letras(cadena):
    return cadena.count('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), cadena.count('abcdefghijklmnopqrstuvwxyz')

# Ejemplo de uso
cadena = input("Ingrese una cadena de texto: ")
mayusculas, minusculas = contar_letras(cadena)
print(f"Número de letras mayúsculas: {mayusculas}")
print(f"Número de letras minúsculas: {minusculas}")
