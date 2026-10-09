#10. Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar. 
dividendo = int(input("INTRODUCE EL DIVIDENDO: "))
divisor = int(input("INTRODUCE EL DIVISOR: "))
cociente = dividendo // divisor
resto = dividendo % divisor
if dividendo % 2 == 0:
    par_impar = "par"
else:
    par_impar = "impar"
print("EL COCIENTE ES:", cociente)
print("EL RESTO ES:", resto)
print("EL DIVIDENDO ES:", par_impar)