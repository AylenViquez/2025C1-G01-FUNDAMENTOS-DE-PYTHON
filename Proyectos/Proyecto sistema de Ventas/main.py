
"""
Autor: Aylen Viquez
Fecha: 2025-04-16
Version: 0.1
Sistema de Gestion de Ventas

"""
import os
from modulo import ingresar_ventas
from modulo import guardar_ventas
from modulo import analisis_ventas
###########

def pausar():
    input('\nPresione Enter para continuar....')
    
############
def limpiar_pantalla():
       """Limpia la pantalla de la terminal en ejecución"""
       os.system('cls' if os.name == 'nt' else 'clear')
    

#Menu Principal
def menu():
    ventas = []
    while True:
        print('\n-----Menu Principal-----')
        print('1.Ingresar ventas de cursos UMCA')
        print('2.Guardar datos en un archivo cvs')
        print('3.Analizar Ventas')
        print('4.Salir')
        
        opcion = input('Seleccione una opcion: ')
        if opcion == "1":
            limpiar_pantalla()
            print('\n ====ingresar Ventas de Cursos====')
            ingresar_ventas(ventas)
            pausar()
            
        elif opcion == "2":
            limpiar_pantalla()
            print('\n ====Guardar datos en un archivo cvs====')
            guardar_ventas(ventas)
            pausar()
            
        elif opcion == "3":
            limpiar_pantalla()
            print("Analizar Ventas")
            analisis_ventas()
            pausar()
        elif opcion == "4":
            limpiar_pantalla()
            print("Gracias por usar el sistema, hasta pronto")
            pausar()
            break
        else:
            limpiar_pantalla()
            print("Opción no válida. Intenta de nuevo.")
            pausar()
            
        
                       

#Ejecucion del sistema si solo si el archivo es el main

if __name__ == '__main__':
    print('Bienvenido al sistema de Gestion de Ventas')
    menu()
    
    