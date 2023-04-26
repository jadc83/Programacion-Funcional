"""
Escribir en Python una función recursiva llamada unicos(secuencia) que reciba 
una secuencia de números enteros en la que todos aparecen dos o más veces, excepto
dos de ellos que aparecen exactamente una vez. La función deberá devolver un conjunto
de tipo set que contenga sólo esos dos elementos únicos.

Importante:

La función debe ser pura.
La llamada a la función debe provocar la ejecución de una función recursiva que genere un proceso iterativo.
No se puede usar ningún bucle while, for, definiciones por comprensión ni expresiones generadoras.

Por ejemplo:

unicos([1, 9, 8, 8, 7, 6, 1, 6]) == {7, 9}
"""

def contar(secuencia):
    lista = []
    if secuencia.count(secuencia[0]) > 1:
        print(secuencia[0])
        return contar(secuencia[1:].append(secuencia[0]))
    return lista