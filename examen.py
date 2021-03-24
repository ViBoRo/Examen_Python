

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



            
    


#main---
f = open("palabras.txt", mode="rt", encoding="utf-8")
#print(lasPalabras)
res = get_list(f)
print(res)