"""
22. La función finales tiene la siguiente especificación:



Pre : n ≥ 0
finales(n: int, t: tuple) -> tuple
Post : finales(n, t) = la tupla que contiene los n elementos finales de t
Por ejemplo: finales(2, (1, 2, 3, 4)) == (3, 4).
Escribir una función recursiva que satisfaga dicha especificación
"""

final = lambda cantidad, tupla, contador: tupla if cantidad == contador else \
    final(cantidad, tupla[1:], len(tupla) - 1)

finales = lambda cantidad, tupla : final(cantidad, tupla, 0)