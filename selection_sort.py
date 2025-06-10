def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
      
        # Suponemos como elemento mas pequeño al que se encuentra en la posicion actual
        min_idx = i
        
        # Iteramos sobre la porcion desordenada del arreglo, buscando el elemento mas pequeño
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
              
                # Actualizamos la posicion del indice si encontramos un elemento mas pequeño
                min_idx = j
        
        # Movemos el elemento mas pequeño a su posicion
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def mostrar_array(arr):
    for val in arr:
        print(val, end=" ")
    print()

arr = [64, 25, 12, 22, 11]
    
print("Arreglo original: ", end="")
mostrar_array(arr)
    
selection_sort(arr)
    
print("Arrgelo ordenado: ", end="")
mostrar_array(arr)