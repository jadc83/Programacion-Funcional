"""
12. La función sustituye tiene la siguiente especificación:

Pre : True
sustituye(a, b, t: tuple) -> tuple
Post : sustituye(a, b, t) = una tupla igual que t pero
sustituyendo los a por b
Escribir una función recursiva que satisfaga dicha especificación y que genere un
proceso:
a) recursivo.
b) iterativo.
"""

sustituye = lambda elemento1, elemento2, tupla, tupla1: "".join(tupla1) if len(tupla) == 0 else \
    sustituye(elemento1, elemento2, tupla[1:], tupla1 + (tupla[0],)) if elemento1 != tupla[0] else \
        sustituye(elemento1, elemento2, tupla[1:], tupla1 + (elemento2,))