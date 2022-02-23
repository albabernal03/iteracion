
import tabulate
def descomposicion():
    caden = cadena.split(separador)
    lista = []
    for i in range(0, len(caden)):
        lista.append(list(caden[i: i+1]))
    tabla = lista
    print(tabulate.tabulate(tabla, tablafmt = "", showindex = True))
