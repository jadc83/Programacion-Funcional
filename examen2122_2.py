def diferencia_diagonales(matriz):
    diag1 = 0
    diag2 = 0

    for x,y in matriz.items():
        if x[0] == x[1]:
            diag1 += y
    for x,y in matriz.items():
        if x[0] + x[1] == 2:
            diag2 += y
            
    diferencia = abs(diag1 - diag2)
    print(diferencia)