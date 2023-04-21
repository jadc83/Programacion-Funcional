"""
10. La función cuantos tiene la siguiente especificación:

Pre : True
cuantos(e, t: tuple) -> int
Post : cuantos(e, t) = el número de veces que aparece e en t
Escribir una función recursiva que satisfaga dicha especificación 
y que genere un proceso:

a) recursivo.
b) iterativo.

"""

cuantos = lambda elemento, tupla, contador: contador if len(tupla) == 0 else \
    cuantos(elemento, tupla[1:], contador + 1) if elemento == tupla[0] else \
        cuantos(elemento, tupla[1:], contador)
        
def cuenta(elemento, tupla, contador):
    if len(tupla) == 0:
        return contador
    else:
        if elemento == tupla[0]:
            return cuenta(elemento, tupla[1:], contador + 1)
        else:
            return cuenta(elemento, tupla[1:], contador)

