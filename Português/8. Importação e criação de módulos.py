# 8. Importação e criação de módulos

# Em Python, um módulo é um arquivo que contém definições de funções, classes e variáveis que podem ser utilizadas em outros programas. A importação de módulos nos permite acessar a funcionalidade definida em outros arquivos e reutilizar código de maneira eficiente. Além disso, podemos criar nossos próprios módulos para organizar e modularizar nosso código.

# Tenha em mente
# Python vem com uma ampla biblioteca padrão de módulos que fornecem funcionalidades adicionais. Esses módulos estão disponíveis sem a necessidade de instalá-los separadamente.

# Importar módulos
# Para utilizar um módulo em nosso programa, devemos importá-lo utilizando a declaração import. Podemos importar um módulo completo ou funções específicas de um módulo.

import math


resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0
# Neste exemplo, importa-se o módulo math utilizando a declaração import. Em seguida, utiliza-se a função sqrt() do módulo math para calcular a raiz quadrada de 25.

# Também podemos importar funções específicas de um módulo utilizando a sintaxe from módulo import função.

from math import sqrt


resultado = sqrt(25)
print(resultado)  # Imprime 5.0
# Neste caso, importa-se apenas a função sqrt() do módulo math, o que nos permite utilizá-la diretamente sem ter que precedê-la com o nome do módulo.

 

# Funções e classes de módulos padrão
# A biblioteca padrão de Python oferece uma ampla gama de módulos com funções e classes úteis. Alguns exemplos comuns incluem:




import random
import datetime


numero_aleatorio = random.randint(1, 10)
print(numero_aleatório)  # Imprime um número inteiro aleatório entre 1 e 10


data_atual = datetime.datetime.now()
print(data_atual)  # Imprime a data e hora atual
# Estes são apenas alguns exemplos dos muitos módulos disponíveis na biblioteca padrão de Python. Você pode consultar a documentação oficial de Python para obter mais informações sobre os módulos e suas funcionalidades.

 