import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_suma(self):
        self.assertEqual(self.calc.sumar(10, 5), 15)

    def test_resta(self):
        self.assertEqual(self.calc.restar(10, 5), 5)

    def test_multiplicacion(self):
        self.assertEqual(self.calc.multiplicar(10, 5), 50)

    def test_division(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()