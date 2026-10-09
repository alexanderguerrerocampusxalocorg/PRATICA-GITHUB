#12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro. 
lado = int(input("INTRODUCE EL VALOR DEL LADO DEL TRAPECIO: "))
base_menor = int(input("INTRODUCE EL VALOR DE LA BASE MENOR DEL TRAPECIO: "))
base_mayor = int(input("INTRODUCE EL VALOR DE LA BASE MAYOR DEL TRAPECIO: "))
altura = int(input("INTRODUCE EL VALOR DE LA ALTURA DEL TRAPECIO: "))
area = ((base_mayor + base_menor) * altura) / 2
perimetro = 2 * lado + base_mayor + base_menor
print("EL ÁREA DEL TRAPECIO ES:", area)
print("EL PERÍMETRO DEL TRAPECIO ES:", perimetro)