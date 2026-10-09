#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales. 
import math
radio = float(input("INTRODUCE EL VALOR DEL RADIO DEL CILINDRO: "))
altura = float(input("INTRODUCE EL VALOR DE LA ALTURA DEL CILINDRO: "))
area = 2 * math.pi * radio * (radio + altura)
volumen = math.pi * (radio ** 2) * altura
print("EL ÁREA DEL CILINDRO ES:", round(area, 2))
print("EL VOLUMEN DEL CILINDRO ES:", round(volumen, 2))