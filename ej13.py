"""
13. La función ultimo tiene la siguiente especificación:

Pre : t ≠ ()
ultimo(t: tuple) -> Any
Post : ultimo(t) = el último elemento de t
Escribir una función recursiva que satisfaga dicha especificación.
"""

ultimo = lambda tupla: tupla if len(tupla) == 1 else \
    ultimo(tupla[1:])