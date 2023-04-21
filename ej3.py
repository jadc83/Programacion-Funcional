"""
3. La función repite tiene la siguiente especificación:

Pre : n ≥ 0
repite(s: str, n: int) -> str
Post : repite(s, n) = s * n

Implementar la función de forma recursiva.
"""

repite = lambda s, n: s if n <= 1 else \
    s + repite(s, n - 1)
    
def repetir(palabra, cantidad):
    if cantidad <= 1:
        return palabra
    else:
        return palabra + repetir(palabra, cantidad - 1)
