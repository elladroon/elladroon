print(" ".join(input("escribe una frase: ").split()[::-1]))


#código desarrollado:

"""
fraseinput = input("escriba una frase: ")
frasesplit = fraseinput.split()                       # separa las palabras por esppacios
frasereverse = frasesplit[::-1]                       # Le da la vuelta al orden de los elementos de la lista
frasefinal = " ".join(frasereverse)                   # Une los elementos de la lista con un espacio entre cada uno
print (frasefinal)                                    # Imprime el resultado
"""