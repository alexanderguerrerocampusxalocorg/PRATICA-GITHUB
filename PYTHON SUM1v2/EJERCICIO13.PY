#13. Realiza un programa que, a partir introducir el lado de un cubo, presente por pantalla el área y para calcular el volumen utiliza el operador de exponente.
lado = int(input("INTRODUCE EL VALOR DEL LADO DEL CUBO: "))
area = 6 * (lado ** 2)
volumen = lado ** 3
print("EL AREA DEL CUBO ES:", area)
print("EL VOLUMEN DEL CUBO ES:", volumen)   