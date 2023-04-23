"""
19. La función menor tiene la siguiente especificación:
Pre : t ≠ ()
menor(t: tuple[a]) -> a
Post : menor(t) = el menor elemento de t
Por ejemplo: menor((3, 2, 5, 7)) == 2. menor((2,3,5,7))
Escribir una función recursiva que satisfaga dicha especificación.
"""
menor = lambda tupla: tupla[0] if len(tupla) == 1 else \
    menor(tupla[1:]) if tupla[1] < tupla[0] else \
        menor( (tupla[0],) + tupla[2:])
