import unittest
from calculadora import Calculadora


class CalculadoraTestCase(unittest.TestCase):
    # setUp se ejecuta antes de cada prueba
    def setUp(self) -> None:
        self.calculadora = Calculadora()

    def test__instancia_calculadora(self):
        self.assertIsInstance(self.calculadora, Calculadora)
        self.assertEqual(self.calculadora.valor, 0)

    def test_suma(self):
        self.calculadora.suma(1, 2)
        self.assertEqual(self.calculadora.valor, 3)

    def test_multiplicacion(self):
        self.calculadora.multiplica(3, 2)
        self.assertEqual(self.calculadora.valor, 6)

    def test_numtiplicacion_cero(self):
        self.assertRaises(ValueError, self.calculadora.multiplica, 0, 1)
