import unittest
from src.desafio_4 import calcular_percentual

class TestDesafio4(unittest.TestCase):
    def test_calcular_percentual(self):
        percentuais = calcular_percentual()
        
        self.assertAlmostEqual(percentuais['SP'], 37.53, places=2)
        self.assertAlmostEqual(percentuais['RJ'], 20.33, places=2)
        self.assertAlmostEqual(percentuais['MG'], 16.23, places=2)
        self.assertAlmostEqual(percentuais['ES'], 15.10, places=2)
        self.assertAlmostEqual(percentuais['Outros'], 10.98, places=2)

if __name__ == '__main__':
    unittest.main()
