# Un conjunto es una estructura de datos mutable y no ordenada que permite almacenar una colección de elementos únicos. Los conjuntos se delimitan por llaves {} o se crean utilizando la función set().

# Creación y operaciones básicas
# Para crear un conjunto, utiliza llaves o la función set():

frutas = {"manzana", "plátano", "naranja"}
números = set([1, 2, 3, 4, 5])
# Los conjuntos soportan operaciones matemáticas de conjuntos, como la unión (|), la intersección (&), la diferencia (-) y la diferencia simétrica (^).

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

unión = conjunto1 | conjunto2
print(unión)  # Imprime {1, 2, 3, 4, 5}

intersección = conjunto1 & conjunto2
print(intersección)  # Imprime {3}

diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}

diferencia_simétrica = conjunto1 ^ conjunto2
print(diferencia_simétrica)  # Imprime {1, 2, 4, 5}

# Métodos de conjuntos
# Los conjuntos en Python tienen varios métodos incorporados para manipular y acceder a los elementos. Algunos métodos comunes son:

# add(elemento): añade un elemento al conjunto.
# remove(elemento): elimina un elemento del conjunto. Si el elemento no existe, genera un error.
# discard(elemento): elimina un elemento del conjunto si está presente. Si el elemento no existe, no hace nada.
# clear(): elimina todos los elementos del conjunto.
# Ejemplo:

frutas = {"manzana", "plátano", "naranja"}

frutas.add("pera")
print(frutas)  # Imprime {"manzana", "plátano", "naranja", "pera"}

frutas.remove("plátano")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.clear()
print(frutas)  # Imprime set()

# Las estructuras de datos en Python nos ofrecen gran flexibilidad y potencia para almacenar y manipular datos en nuestros programas. Las listas son útiles para colecciones ordenadas y mutables, las tuplas para colecciones ordenadas e inmutables, los diccionarios para almacenar pares de clave-valor y los conjuntos para colecciones no ordenadas de elementos únicos.