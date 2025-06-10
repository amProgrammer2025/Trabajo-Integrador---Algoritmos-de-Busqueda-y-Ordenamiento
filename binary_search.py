def binary_search(arr, x):
    limite_inferior = 0
    limite_superior = len(arr) - 1
    mid = 0

    while limite_inferior <= limite_superior:

        mid = (limite_superior + limite_inferior) // 2

        # Si x es mayor, ignoramos la mitad izquierda
        if arr[mid] < x:
            limite_inferior = mid + 1

        # Si x es menor, ignoramos la mitad derecha
        elif arr[mid] > x:
            limite_superior = mid - 1

        # El elemento esta en el medio
        else:
            return mid

    # Si salimos del ciclo while, el elemento no se encontro
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = int(input("Ingrese el elemento a buscar: "))

resultado = binary_search(arr, x)

if resultado != -1:
    print(f"El elemento esta presente en la posicion {str(resultado)}")
else:
    print("El elemento no esta presente en el arreglo")