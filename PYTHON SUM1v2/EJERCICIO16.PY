#16. Utiliza el metodo sqrt de la libreria math para calcular la raiz cuadrada de un numero. El resultado de la raiz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos  resultados de todo el proceso (raiz y division).
import math
numero = float(input("INTRODUCE UN NUMERO PARA CALCULAR SU RAIZ CUADRADA: "))
raiz_cuadrada = math.sqrt(numero)
division = raiz_cuadrada // 2
print("LA RAIZ CUADRADA DEL NUMERO ES:", raiz_cuadrada)
print("EL RESULTADO DE LA DIVISION ENTRE 2 ES:", division)