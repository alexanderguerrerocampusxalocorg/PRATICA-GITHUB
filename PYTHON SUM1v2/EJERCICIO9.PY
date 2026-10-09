#9. programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas
segundos = int(input("INTRODUCE EL NUMERO DE SEGUNDOS: "))
minutos = segundos // 60
horas = minutos // 60
print("EL NUMERO DE MINUTOS ES:", minutos)
print("EL NUMERO DE HORAS ES:", horas)