def completar():
    """Completar"""
    linea = "loquesea"
    resultado = []
    archivo = open("datos.txt", "r")
    while linea != '':
        linea = archivo.readline().strip()
        l1 = list(linea)
        guion = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        noestan = []
        for x in guion:
            if x not in l1:
                noestan.append(x)
        for x in l1:
            if x == "*":
                l1[l1.index(x)] = noestan[0]
                noestan.pop(0)
        resultado.append("".join(l1))
    resultado.pop(-1)
    archivo.close()

    archivo = open("resultados.txt", "w")
    for x in resultado:
        archivo.write(x)
        archivo.write("\n")
    archivo.close()