# Definimos las preguntas y sus respuestas correctas
preguntas = [
    ("Al evaluar la expresión 2 < 1 or 2 != 1, el resultado es:", "c", "a. 1.\nb. 2.\nc. True.\nd. False.\n"),
    ("¿Qué instrucción es equivalente a i += 1?", "a", "a. i = i + 1.\nb. i + 1.\nc. 1 += i.\nd. i = i + i.\n"),
    ("¿Qué valor devuelve la siguiente expresión: 3 if 1 < 2 else 4?", "c", "a. 1.\nb. 2.\nc. 3.\nd. 4.\n"),
    ("Selecciona la expresión cuya evaluación resulta 3:", "c", "a. 3 + 2 * 6 / 5.\nb. (3 + 2) * 6 / 5.\nc. (3 + 2 * 6) / 5.\nd. 3 + 2 * (6 / 5).\n"),
    ("Los operadores lógicos operan con valores booleanos, resultando:", "d", "a. Valores enteros.\nb. Valores enteros y booleanos.\nc. Otros tipos de valores.\nd. Sólo valores booleanos.\n")
]

puntuacion = 0 # Inicializamos la puntuación del jugador

# Recorremos cada pregunta y la presentamos al jugador
for pregunta, respuesta, opciones in preguntas:
    print(pregunta)
    print(opciones)
    # Pedimos al jugador que introduzca su respuesta
    respuesta_jugador = input("Respuesta: ")
    # Comprobamos si la respuesta es correcta y actualizamos la puntuación
    if respuesta_jugador == respuesta:
        print("¡Correcto!")
        puntuacion += 1
    else:
        print("Incorrecto.")
    
    print("") # Dejamos un espacio en blanco entre cada pregunta

# Mostramos la puntuación final al jugador
print("Tu puntuación final es:", puntuacion, "de", len(preguntas))

