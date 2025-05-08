import unittest
from Personaje import inputs_personaje, Personaje

class TestPersonaje(unittest.TestCase):
    def setUp(self):
        self.perso = Personaje()
        self.perso.