import unittest
from libro import *
from autor import *
class Pruebas(unittest.TestCase):

    def test_mas_antiguo(self):
        librosall = mas_antiguos(losLibros, 2021)
        librosEmpty = mas_antiguos([], 2021)
        #identifcar que se filtra por anyo
        self.assertEqual(len(libros21), 2)

        #si se le pasa el anyo actual se devuelven todos
        self.assertEqual(len(librosall), 3)

        #si se da una lista vacia salta error
        self.assertRaisesRegex(ValueError, "Ningun pasajero", flight2.reallocate_passenger, "5B", "12G" )

