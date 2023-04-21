"""
11. La función quita tiene la siguiente especificación:

Pre : True
quita(e, t: tuple) -> tuple
Post : quita(e, t) = una tupla igual que t pero sin los e
Escribir una función recursiva que satisfaga dicha especificación 
y que genere un proceso:

a) recursivo.
b) iterativo.

"""

quita = lambda elemento, tupla, tupla1: "".join(tupla1) if len(tupla) == 0 else \
    quita(elemento, tupla[1:], tupla1) if elemento == tupla[0] else \
        quita(elemento, tupla[1:], tupla1 + (tupla[0],))
        
def quitar(elemento, tupla, tupla1):
    if len(tupla) == 0:
        return "".join(tupla1)
    else:
        if elemento == tupla[0]:
            return quitar(elemento, tupla[1:], tupla1)
        else:
            return quitar(elemento, tupla[1:], tupla1 + (tupla[0],))