from projeto2 import *
import unittest

class TextoTest(unittest.TestCase):
  def imprime_test(self):
    texto = Texto()
    assert texto.font == "Kingthings Trypewriter.ttf"
    assert not texto.t == 10
    assert texto.tempo == 8000
  def imprime_texto_test(self):
    assert texto.t == 100

class PersonagemTest(unittest.TestCase):
  person = Personagem()





if __name__ == "__main__":
    unittest.main()
