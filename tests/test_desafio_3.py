import unittest
from src.desafio_3 import calcular_faturamento
from unittest.mock import patch

class TestDesafio3(unittest.TestCase):
    @patch('src.desafio_3.open')
    @patch('src.desafio_3.json.load')
    def test_calcular_faturamento(self, mock_json_load, mock_open):
        mock_json_load.return_value = [
            {"dia": 1, "valor": 100},
            {"dia": 2, "valor": 200},
            {"dia": 3, "valor": 0},  
            {"dia": 4, "valor": 300}
        ]
        menor, maior, dias_acima_media = calcular_faturamento()
        
        self.assertEqual(menor, 100)
        self.assertEqual(maior, 300)
        self.assertEqual(dias_acima_media, 2) 

if __name__ == '__main__':
    unittest.main()
