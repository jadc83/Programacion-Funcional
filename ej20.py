"""
20. La función mayor tiene la siguiente especificación:



Pre : 𝑡 ≠ ()
mayor(𝑡: tuple[𝛼]) -> 𝛼
Post : mayor(𝑡) = el mayor elemento de 𝑡
Por ejemplo: mayor((3, 2, 5, 7)) == 7.
Escribir una función recursiva que satisfaga dicha especificación

"""

mayor = lambda tupla: tupla[0] if len(tupla) == 1 else \
    mayor(tupla[1:]) if tupla[1] > tupla[0] else \
        mayor( (tupla[0],) + tupla[2:])