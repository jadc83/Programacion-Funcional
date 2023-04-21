"""
14. La función enesimo tiene la siguiente especificación:



Pre : t ≠ () ∧ 0 ≤ n < len(t)
enesimo(n: int, t: tuple) -> Any
Post : enesimo(n, t) = el n-ésimo elemento de t
Escribir una función recursiva que satisfaga dicha especificación.
"""

enesimo = lambda posicion, tupla, contador: tupla if len(tupla) == 1 else \
    tupla[0] if posicion == contador else \
        enesimo(posicion, tupla[1:], contador + 1)