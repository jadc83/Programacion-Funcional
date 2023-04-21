"""
6. La función voltea le da la vuelta a un número entero:
voltea(423) = 324
voltea(7) = 7
Se pide:
a) Escribir su especificación.
b) Implementar una función recursiva que satisfaga dicha especificación.
Indicación: Usar la función digitos que devuelve la cantidad de dígitos que tiene un
entero. Usar además la indicación del ejercicio anterior.
"""

digitos = lambda numero, contador: contador if numero == 0 else \
    digitos(numero // 10, contador + 1)
    
    
voltea = lambda numero: numero if digitos(numero, 0) == 1 else \
    int(str(numero % 10) + str(voltea(numero // 10)))
    
def voltear(numero):
    if digitos(numero, 0) == 1:
        return numero
    else:
        return int(str(numero % 10) + str(voltea(numero // 10)))