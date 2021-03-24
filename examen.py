


def get_list(palabras):
    resultado = {}
    listaP = palabras.split(" ")
    for size in 1, 2, 3:
        theWords = []
        for palabra in listaP:
            if(len(palabra) == size):
                theWords.append(palabra)
        resultado[size] = theWords
    return resultado
        
            
        





#main---
f = open("palabras.txt", mode="rt", encoding="utf-8")
lasPalabras = f.read()
#print(lasPalabras)
res = get_list(lasPalabras)