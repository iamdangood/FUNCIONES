def en_rango(rango_inicio, numero, rango_final):
    return rango_inicio <= numero <= rango_final

inicio = int(input("Ingrese el inicio del rango: "))
final = int(input("Ingrese el final del rango: "))
numero_a_verificar = int(input("Ingrese el número a verificar: "))

if en_rango(inicio, numero_a_verificar, final):
    print("El número está dentro del rango.")
else:
    print("El número está fuera del rango.")
