#Capitulo 3. Ejercicio propuesto 21

import math

def calcular_datos_triangulo(ladoa, ladob, ladoc):
    perimetro = ladoa + ladob + ladoc
    semiperimetro = perimetro / 2
    area = math.sqrt(semiperimetro * (semiperimetro - ladoa) * (semiperimetro - ladob) * (semiperimetro - ladoc))
    return perimetro, semiperimetro, area

ladoa = float(input("Ingrese la longitud del lado a: "))
ladob = float(input("Ingrese la longitud del lado b: "))
ladoc = float(input("Ingrese la longitud del lado c: "))

perimetro, semiperimetro, area = calcular_datos_triangulo(ladoa, ladob, ladoc)

print(f"El perímetro del triángulo es: {perimetro}")
print(f"El semiperímetro del triángulo es: {semiperimetro}")
print(f"El área del triángulo es: {area}")
