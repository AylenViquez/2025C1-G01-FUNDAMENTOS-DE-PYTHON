#### Los imports se sugiere que vayan al inicio del sistema
import csv
import pandas as pd



### Aca van a estar todas las funnciones


def ingresar_ventas(lista_ventas):

    while True:
        try:
            curso = input ('Íngrese el nombre del curso: ').upper()
            cantidad = int (input('Ingrese la cantidad de curso vendidos: '))
            fecha = input('Íngrese la fecha de la venta (AAAA-MM-DD): ')
            precio = float(input('Íngrese el precio del curso: '))
            cliente = input('Ingrese el nombre del cliente: ').upper()
        except ValueError:
            print('Entradas no validas, por favor intentelo de nuevo')
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
            limpiar_pantalla()
            print('\n---- Ingresando otra venta ----')
        elif continuar == 'n':
            break
        else: 
            print ('Opción no valida') 
            
            
def guardar_ventas(ventas):
    if not ventas:
        print('No hay ventas que guardar en el CSV')
    else:
        if os.path.exists('ventas.csv'):
            #si el archivo existe agrego Append  'A'
            with open('ventas.csv','a',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['curso','cantidad','precio','fecha','cliente'])
                guardar.writerows(ventas)        
        else: #Si no existe abro en modo escritura 'W'
            with open('ventas.csv','w',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['curso','cantidad','precio','fecha','cliente'])
                guardar.writeheader()
                guardar.writerows(ventas)
                
        #Limpio las ventas en memoria y muestro el guardado exitoso                
        ventas = []
        print('Datos guardados exitosamente!')   

def analisis_ventas():
    df = pd.read_csv('ventas.csv')
    print('\n======== Resumen de Ventas========')
    df['subtotal'] = df['cantidad'] * df['precio']
    total_ingresos = df['subtotal'].sum()
    
    #Total de Ventas
    print(f'Total de Ventas{total_ingresos:2f}')
    
    #Curso mas vendido 
    
    curso_top = df.groupby("curso")['cantidad'].sum().idxmax()
    print('El curso mas vendido es: ', curso_top)
    
    #Cliente mas Top
    
    cliente_top = df.groupby("cliente")['subtotal'].sum().idxmax()
    total_cliente_top = df.groupby("cliente")['subtotal'].sum().max()
    print(f'El cliente que más ha comprado es: {cliente_top} (${total_cliente_top:.2f})')
    
    #Ventas por fecha
    ventas_fecha = df.groupby(df['fecha'])['subtotal'].sum().reset_index()
    ventas_fecha.columns = ['fecha', 'Total Vendido']
    print('\nLos dias con mas ventas son\n', ventas_fecha)
    