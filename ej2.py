"""
2. La función potencia tiene la siguiente especificación:

Pre : b ≥ 0
potencia(a: int, n: int) -> int
Post : potencia(a, b) = a ** b


a) Implementar la función de forma no recursiva.
b) Implementar la función de forma recursiva
"""

potencia = lambda a, b: 1 if b <= 0 else \
    a ** b
    
potrec = lambda a, b: 1 if b <= 0 else \
    a * potrec(a, b - 1)
    
def potencia_rec(a, b):
    if b <= 0:
        return 1
    else:
        return a * potrec(a, b - 1)