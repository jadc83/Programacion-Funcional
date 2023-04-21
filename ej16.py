"""
16. La función palindromo tiene la siguiente especificación:

Pre : True
palindromo(t: tuple) -> bool
Post : palindromo(t) =

True si t es un palíndromo
(se lee igual en un sentido que en otro)
False en caso contrario
Por ejemplo: palindromo((1, 2, 3, 4, 3, 2, 1)) == True.
Escribir una función recursiva que satisfaga dicha especificación
"""
invertir = lambda tupla: tupla if len(tupla) == 1 else \
    invertir(tupla[1:]) + (tupla[0],)

palindromo = lambda tupla: (len(tupla) <= 1) or (tupla[0] == tupla[-1] and palindromo(tupla[1:len(tupla)-1]))

