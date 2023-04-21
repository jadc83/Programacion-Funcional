"""
1. Dada la siguiente función matemática:
f (n) =
(
0 si n = 0
1 + 2 · f (n - 1) si n > 0
calcular el valor de f (3).

"""

f = lambda n: 0 if n == 0 else \
    1 + 2 * f(n - 1)
    
def funcion(n):
    if n == 0:
        return 0
    else:
        return 1 + 2 * funcion(n - 1)