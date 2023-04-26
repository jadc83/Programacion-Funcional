"""Escribir en python una funcion "mas_repetir(lista)
que reciba una lista de numeros y que devuelva un conjunto
que contenga el que mas se repite dentro de la lista

mas_repetir([1,2,3,2,4,5,5]) {5}

Si hay mas de un numero que se repita el numero maximo de veces,
debera devolver un conjunto de todos ellos

mas_repetir([1,2,3,2,4,5,5]) {2,5}
"""

def mas_repetir(lista):
    if lista == []:
        return {}
    else:
        resultado = set()
        juntos = dict(zip(lista, [lista.count(x) for x in lista]))
        for x, y in juntos.items():
            if y == max([lista.count(x) for x in lista]):
                resultado.update({x})
        return resultado