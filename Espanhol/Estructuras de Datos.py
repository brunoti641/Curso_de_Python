# Las estructuras de datos nos permiten organizar y almacenar datos de manera eficiente en nuestros programas. Python proporciona varias estructuras de datos integradas, como listas, tuplas, diccionarios y conjuntos, cada una con sus propias características y usos.

# Listas
# Una lista es una estructura de datos mutable y ordenada que permite almacenar una colección de elementos. Los elementos de una lista pueden ser de diferentes tipos de datos y se encierran entre corchetes [], separados por comas.

# Creación y acceso
# Para crear una lista, simplemente encierra los elementos entre corchetes:

frutas = ["manzana", "plátano", "naranja"]
# Para acceder a los elementos de una lista, utiliza el índice del elemento entre corchetes. Los índices comienzan desde 0.

print(frutas[0])  # Imprime "manzana"
print(frutas[1])  # Imprime "plátano"
print(frutas[2])  # Imprime "naranja"

# También puedes acceder a los elementos desde el final de la lista utilizando índices negativos. El índice -1 representa el último elemento, -2 el penúltimo, y así sucesivamente.

print(frutas[-1])  # Imprime "naranja"
print(frutas[-2])  # Imprime "plátano"
print(frutas[-3])  # Imprime "manzana"

# Métodos de listas
# Las listas en Python tienen varios métodos incorporados que nos permiten manipular y modificar los elementos de la lista. Algunos métodos comunes son:

# append(elemento): añade un elemento al final de la lista.
# insert(índice, elemento): inserta un elemento en una posición específica de la lista.
# remove(elemento): elimina la primera ocurrencia de un elemento en la lista.
# pop(índice): elimina y devuelve el elemento en una posición específica de la lista.
# sort(): ordena los elementos de la lista en orden ascendente.
# reverse(): invierte el orden de los elementos en la lista.
# Ejemplo:

frutas = ["manzana", "plátano", "naranja"]

frutas.append("pera")
print(frutas)  # Imprime ["manzana", "plátano", "naranja", "pera"]

frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "plátano", "naranja", "pera"]

frutas.remove("plátano")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]

fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"

frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]

frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]

# Listas por comprensión
# Las listas por comprensión son una forma concisa de crear nuevas listas basadas en una secuencia existente. Permiten filtrar y transformar los elementos de una lista en una sola línea de código.

# nueva_lista = [expresión for elemento in secuencia if condición]
# Ejemplo:

números = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in números if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16]

# En este ejemplo, se crea una nueva lista llamada cuadrados, que contiene los cuadrados de los números pares de la lista números. La expresión x ** 2 eleva cada elemento al cuadrado, y la condición if x % 2 == 0 filtra solo los números pares.