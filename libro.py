class Libro:

  def __init__(self, a, t, y):
    self.__autor = a
    self.__titulo = t
    self.__anyo = y


  def get_anyo(self):
    return self.__anyo

  def get_titulo(self):
    return self.__titulo