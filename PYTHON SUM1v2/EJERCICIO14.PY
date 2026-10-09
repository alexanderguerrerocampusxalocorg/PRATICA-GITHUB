#14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería math y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.
import math
diametro = float(input("INTRODUCE EL VALOR DEL DIÁMETRO DEL CÍRCULO: "))
radio = diametro / 2
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio
print("EL ÁREA DEL CÍRCULO ES:", round(area, 1))
print("EL PERÍMETRO DEL CÍRCULO ES:", round(perimetro, 1))