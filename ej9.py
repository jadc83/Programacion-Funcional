"""
9. La función elem tiene la siguiente especificación:



Pre : True
elem(e, t: tuple) -> bool
Post : elem(e, t) =
(
True si e está en t
False en caso contrario
Escribir una función recursiva que satisfaga dicha especificación.
"""

elem = lambda e, t: False if len(t) == 0 else \
    True if e == t[0] else \
        elem(e, t[1:])

def elemento(elemento, tupla):
    if len(tupla) <= 0:
        return False
    else:
        if elemento == tupla[0]:
            return True
        else:
            return False