import unittest
from src.desafio_5 import inverter_string

class TestDesafio5(unittest.TestCase):
    def test_inverter_string(self):
        self.assertEqual(inverter_string("python"), "nohtyp")
        self.assertEqual(inverter_string("abcde"), "edcba")
        self.assertEqual(inverter_string("12345"), "54321")
        self.assertEqual(inverter_string(""), "")

if __name__ == '__main__':
    unittest.main()
