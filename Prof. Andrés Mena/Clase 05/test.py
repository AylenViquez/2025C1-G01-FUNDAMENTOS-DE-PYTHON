# Función para verificar si un número es par
def es_par(pnum):
    return numero % 2 == 0


numero = int(input('Ingrese un número por favor:'))
print('Es un número par: ',es_par(numero))