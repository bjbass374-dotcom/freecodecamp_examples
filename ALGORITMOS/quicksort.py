def quicksort(lista):
    # Caso base: lista vacía o de un elemento ya está ordenada
    if len(lista) <= 1:
        return lista

    # Elegir el pivote (puedes cambiar a lista[0] para usar el primero)
    pivote = lista[-1]

    # Partición en tres sublistas
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]

    # Llamada recursiva y concatenación
    return quicksort(menores) + iguales + quicksort(mayores)


# --- Prueba rápida ---
if __name__ == "__main__":
    ejemplo = [3, 6, 8, 10, 1, 2, 1, 5, 4, 7, 9, 2]
    print("Original:", ejemplo)
    print("Ordenado :", quicksort(ejemplo))