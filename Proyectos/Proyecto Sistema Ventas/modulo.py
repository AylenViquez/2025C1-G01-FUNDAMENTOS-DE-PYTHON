import csv

def ingresar_ventas(lista_ventas):
    while True:
        try: 
            curso = input ('Íngrese el nombre del curso: ').upper()
            cantidad = int (input('Ingrese la cantidad de curso vendidos: '))
            fecha = input('Íngrese la fecha de la venta (AAAA-MM-DD): ')
            precio = float(input('Íngrese el precio del curso: '))
            cliente = input('Íngrese el nombre del cliente: ').upper()
        except ValueError:
            print('Entradas no validas, por favor intetenlo nuevamente!')
            continue
        
        venta = {
            'curso' : curso,
            'cantidad' : cantidad,
            'precio' : precio,
            'fecha' : fecha,
            'cliente' : cliente
        }
        lista_ventas.append(venta)
        
        
        continuar = input('Desea ingresar otra venta s/n :').lower()
        if continuar == 's':
            print('\n---- Ingresando otra venta ----')
        elif continuar == 'n':
            break
        else: 
            print ('Opción no valida')
        
def guardar_ventas(ventas):
    if not ventas:
        print('No hay ventas que guardar en el CSV')
    else:
        with open('ventas.csv','w',newline='',encoding='utf-8') as csv:
            guardar = csv.di (csv,fieldnames=['curso','cantidad','precio','fecha','cliente'])
            guardar.writeheader()
            guardar.writerows(ventas)
        print('Datos guardados exitosamente!')