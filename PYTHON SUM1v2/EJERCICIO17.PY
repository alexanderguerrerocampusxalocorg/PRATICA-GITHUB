#17. Calcula el indice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso. 
peso = float(input("INTRODUCE TU PESO EN KG: "))
estatura = float(input("INTRODUCE TU ESTATURA EN METROS: "))
imc = peso / (estatura ** 2)
if imc >= 25:
    print("TU INDICE DE MASA CORPORAL ES:", round(imc, 2))
    print("INFORME: ESTAS EN SOBREPOSO.")
else:
    print("TU INDICE DE MASA CORPORAL ES:", round(imc, 2))
    print("INFORME: NO ESTAS EN SOBREPOSO.")