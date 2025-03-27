# 8. Importación y Creación de Módulos

# En Python, un módulo es un archivo que contiene definiciones de funciones, clases y variables que pueden ser utilizadas en otros programas. La importación de módulos nos permite acceder a la funcionalidad definida en otros archivos y reutilizar código de manera eficiente. Además, podemos crear nuestros propios módulos para organizar y modularizar nuestro código.

# Ten en cuenta
# Python viene con una amplia biblioteca estándar de módulos que proporcionan funcionalidades adicionales. Estos módulos están disponibles sin necesidad de instalarlos por separado.

# Importar módulos
# Para utilizar un módulo en nuestro programa, debemos importarlo utilizando la declaración import. Podemos importar un módulo completo o funciones específicas de un módulo.

import math

resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0
# En este ejemplo, se importa el módulo math utilizando la declaración import. Luego, se utiliza la función sqrt() del módulo math para calcular la raíz cuadrada de 25.

# También podemos importar funciones específicas de un módulo utilizando la sintaxis from módulo import función.

from math import sqrt

resultado = sqrt(25)
print(resultado)  # Imprime 5.0
# En este caso, se importa solo la función sqrt() del módulo math, lo que nos permite utilizarla directamente sin tener que precederla con el nombre del módulo.

# Funciones y clases de módulos estándar
# La biblioteca estándar de Python ofrece una amplia gama de módulos con funciones y clases útiles. Algunos ejemplos comunes incluyen:

import random
import datetime

número_aleatorio = random.randint(1, 10)
print(número_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10

fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual
# Estos son solo algunos ejemplos de los muchos módulos disponibles en la biblioteca estándar de Python. Puedes consultar la documentación oficial de Python para obtener más información sobre los módulos y sus funcionalidades.