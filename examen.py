from autor import *
from libro import *


#1.-------------

def get_list(fichero):
    palabras = f.read()
    if len(palabras) != 0:
        resultado = {}
        listaP = palabras.split(" ")
        repetida = False
        for size in 1, 2, 3:
            theWords = []
            for palabra in listaP:

                if(len(palabra) == size):

                    for i in theWords:
                        if i == palabra:
                            repetida = True

                    if repetida == False: 
                        theWords.append(palabra)
                    repetida = False
        
            resultado[size] = theWords
        return resultado
    else: 
        raise ValueError("El fichero esta vacio")

#2.---------------------

def mas_antiguos(lista, anyo):
    for l in lista:
        if int(l.get_anyo()) > 2021 or int(l.get_anyo()) < 1900:
            raise ValueError("Año del libro no valido")

    titulos = []
    for libro in lista:
        if int(libro.get_anyo()) <= anyo:
            titulos.append(libro.get_titulo)
    return titulos
    


#main---
#1.1-----------

f = open("palabras.txt", mode="rt", encoding="utf-8")
#print(lasPalabras)
res = get_list(f)
print(res)

#1.2.------------------

libro1 = Libro("cervantes", "quixot", "1921")
libro2 = Libro("shakespeare", "r&j", "1955")
libro3 = Libro("aaa", "bbbb", "2001")
losLibros = [libro1, libro2, libro3]
libros21 = mas_antiguos(losLibros, 2000)
print(libros21)
