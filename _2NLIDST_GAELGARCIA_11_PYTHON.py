def sumaIterativa(n):
    suma = 0
    while n > 9:
        suma += n % 10
        n //= 10
    return suma + n

def sumaRecursiva(n):
    if n <= 9:
        return n
    else:
        return sumaRecursiva(n // 10) + n % 10

cantidad = int(input("Ingrese la cantidad de numeros: "))

for i in range(cantidad):
    n = int(input(f"Ingrese el numero {i + 1}: "))
    print("Suma iterativa:", sumaIterativa(n))
    print("Suma recursiva:", sumaRecursiva(n))