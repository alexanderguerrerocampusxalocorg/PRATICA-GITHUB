#6. A partir del programa 5. Haz que se muestre por pantalla también la frase en el orden inverso en que se han introducido las palabras.
palabra1 = input("INTRODUCE LA PRIMERA PALABRA: ")
palabra2 = input("INTRODUCE LA SEGUNDA PALABRA: ")
palabra3 = input("INTRODUCE LA TERCERA PALABRA: ")
palabra4 = input("INTRODUCE LA CUARTA PALABRA: ")
palabra5 = input("INTRODUCE LA QUINTA PALABRA: ")

frase = palabra1 + ", " + palabra2 + ", " + palabra3 + ", " + palabra4 + ", " + palabra5
print("LA FRASE ES:", frase)

frase_inversa = palabra5 + ", " + palabra4 + ", " + palabra3 + ", " + palabra2 + ", " + palabra1
print("LA FRASE EN ORDEN INVERSO ES:", frase_inversa)
