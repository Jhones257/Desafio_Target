import unittest
from src.desafio_2 import pertence_fibonacci

class TestDesafio2(unittest.TestCase):
    def test_pertence_fibonacci(self):
        self.assertTrue(pertence_fibonacci(21)) 
        self.assertFalse(pertence_fibonacci(22))  
        self.assertTrue(pertence_fibonacci(0))  

if __name__ == '__main__':
    unittest.main()
