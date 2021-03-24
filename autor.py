class Autor:

  def __init__(self, i, n, a):
    self.__id_autor = i
    self.__nombre = n 
    self.__anyo = a

  def mostrar(self): #público
    print("El nombre es ",self.nombre, " y la edad es ",self.__edad)
