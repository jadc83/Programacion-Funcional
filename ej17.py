"""
17. La función rota tiene la siguiente especificación:



Pre : 𝑛 ≥ 0
rota(𝑛: int, 𝑡: tuple) -> tuple
Post : rota(𝑛, 𝑡) = la tupla obtenida poniendo los 𝑛 primeros
elementos de 𝑡 al final
Por ejemplo:
rota(1, (3, 2, 5, 7)) == (2, 5, 7, 3)
rota(2, (3, 2, 5, 7)) == (5, 7, 3, 2)
rota(3, (3, 2, 5, 7)) == (7, 3, 2, 5)
Escribir una función recursiva que satisfaga dicha especificación.

"""

rotame = lambda n, tupla, contador: tupla if n == contador else \
    rotame(n, (tupla[1:] + (tupla[0],) ), contador + 1 )
    
rota = lambda n, tupla: rotame(n, tupla, 0)