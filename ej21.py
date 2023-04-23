"""
21. La función menor_mayor tiene la siguiente especificación:

Pre : 𝑡 ≠ ()
menor_mayor(𝑡: tuple[𝛼]) -> tuple[𝛼]
Post : menor_mayor(𝑡) = una tupla con dos elementos
que contiene el menor y el mayor elemento de 𝑡,
en ese orden
Por ejemplo: menor_mayor((3, 2, 5, 7)) == (2, 7).
Escribir una función recursiva que satisfaga dicha especificación.

"""

from ej19 import menor
from ej20 import mayor

menor_mayor = lambda tupla: () + (menor(tupla),) + ( mayor(tupla), )