#Respuesta
suma = 0

#Usar bucle for para definir el final de la secuencia a sumar
num = int(input('Íngrese el numero a sumar en secuencia: '))

for i in range(0,num + 1): #Llaegar a llimete que se ingreso en el input
    suma = suma + i #Sumo el valor de  cada iteración
    
print(f'La suma de los numero del 1 al {num} es: {suma}')