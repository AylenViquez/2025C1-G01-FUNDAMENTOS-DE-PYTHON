#               Lu  Ma  Mi  Ju  Vi  Sa  Do
temperaturas = [22, 24, 19, 23, 25, 20, 21]

promedio = sum(temperaturas) / len(temperaturas)

dia = 0
while dia < len (temperaturas):
    if temperaturas[dia] > promedio:
        print(f' El día {dia} es cálido, con una temperatura de {temperaturas[dia]}')
    dia += 1