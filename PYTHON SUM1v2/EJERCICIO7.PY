#7. programa que calcule dos operandos con los 7 operadores vistos en clase. Como puedes forzar que el resultado de la division tenga 2 decimales? 
operando1 = float(input("INTRODUCE EL PRIMER OPERANDO: "))
operando2 = float(input("INTRODUCE EL SEGUNDO OPERANDO: "))
suma = operando1 + operando2
resta = operando1 - operando2
multiplicacion = operando1 * operando2
division = operando1 / operando2
potencia = operando1 ** operando2
modulo = operando1 % operando2
division_entera = operando1 // operando2

print("LA SUMA ES:", suma)
print("LA RESTA ES:", resta)
print("LA MULTIPLICACION ES:", multiplicacion)
print("LA DIVISION ES:", division)
print("LA POTENCIA ES:", potencia)
print("EL MODULO ES:", modulo)
print("LA DIVISION ENTERA ES:", division_entera)