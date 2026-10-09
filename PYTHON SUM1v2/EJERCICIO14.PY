#14. Realiza un programa que a partir de introducir el diametro de un circulo calcule el área y perímetro. Importa la librería math y utiliza el valor PI para hacer el calculo. Redondea el resultado a un decimal.
import math
diametro = float(input("INTRODUCE EL VALOR DEL DIAMETRO DEL CIRCULO: "))
radio = diametro / 2
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio
print("EL AREA DEL CIRCULO ES:", round(area, 1))
print("EL PERIMETRO DEL CIRCULO ES:", round(perimetro, 1))