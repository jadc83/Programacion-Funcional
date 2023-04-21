"""
18. La función rota1 tiene la siguiente especificación:
Pre : True
rota1(𝑡: tuple) -> tuple
Post : rota1(𝑡) = la tupla obtenida poniendo el primer
elemento de 𝑡 al final
5
Por ejemplo: rota1((3, 2, 5, 7)) == (2, 5, 7, 3).
Escribir una función recursiva que satisfaga dicha especificación.

"""

rotame = lambda n, tupla, contador: tupla if n == contador else \
    rotame(n, (tupla[1:] + (tupla[0],) ), contador + 1 )
    
rota1 = lambda tupla: rotame(1, tupla, 0)