def completar():
    archivo = open("numeros.txt", "r")
    linea = "a"
    res = []

    while linea != "":
        noestan = []
        guia = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        linea = archivo.readline()
        l1 = [ x.strip() for x in linea]
        for x in guia:
            if x not in l1:
                noestan.append(x)
        for x in l1:
            if x == "*":
                l1[l1.index(x)] = noestan[0]
                noestan.pop(0)
        res.append("".join(l1))

    res = [ str(x) + "\n" for x in res]
    res.pop(-1)
    archivo.close()
    archivo = open("numeros.txt", "w")
    archivo.writelines(res)
    archivo.close()