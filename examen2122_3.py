def intercambiar(cadena):
    "intercambiar"
    nombre = cadena.split("  ")[::-1]
    if len(nombre) == 2:
        return nombre[0] + ", " + nombre[1]
    else:
        return cadena