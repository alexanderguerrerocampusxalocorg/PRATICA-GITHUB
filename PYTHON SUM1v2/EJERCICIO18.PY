#18. Cines Paradiso celebran su decimo aniversario y por ser un dia especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.
numero_menores = int(input("INTRODUCE EL NUMERO DE MENORES: "))
numero_adultos = int(input("INTRODUCE EL NUMERO DE ADULTOS: "))
precio_entrada = 12
total_menores = numero_menores * precio_entrada * 0.5
total_adultos = numero_adultos * precio_entrada * 0.9
total_pagar = total_menores + total_adultos
print("EL TOTAL A PAGAR ES:", total_pagar)  