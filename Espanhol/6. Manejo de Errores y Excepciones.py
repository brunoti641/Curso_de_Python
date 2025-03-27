# 6. Manejo de Errores y Excepciones
# Al escribir programas, es común encontrarnos con situaciones inesperadas o errores durante la ejecución. Python proporciona un mecanismo para manejar estos errores de manera controlada utilizando el manejo de excepciones. Esto nos permite capturar y manejar errores específicos sin que el programa se detenga abruptamente.

# Errores comunes en Python
# Antes de profundizar en el manejo de excepciones, veamos algunos errores comunes que puedes encontrar en Python.

# Ocurre cuando el código no sigue las reglas de sintaxis de Python, como olvidar dos puntos después de una declaración de función o un bucle.

def mi_funcion() # Faltan los dos puntos
    print("Hola")
    
# Ocurre cuando se hace referencia a una variable o función que no ha sido definida.

print(variable_no_definida)

# Ocurre cuando se realiza una operación con tipos de datos incompatibles, como intentar sumar un número y una cadena.
resultado = 5 + "10"

# Ocurre cuando se intenta acceder a un índice fuera del rango válido de una lista o secuencia.

mi_lista = [1, 2, 3]
print(mi_lista[3])  # El índice 3 está fuera de rango

# Estos son solo algunos ejemplos de errores comunes. Cuando ocurre un error, Python genera una excepción y muestra un mensaje de error que incluye el tipo de excepción y una descripción del problema.