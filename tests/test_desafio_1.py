import unittest
from src.desafio_1 import calcular_soma

class TestDesafio1(unittest.TestCase):
    def test_calcular_soma(self):
        self.assertEqual(calcular_soma(), 91)

if __name__ == '__main__':
    unittest.main()
