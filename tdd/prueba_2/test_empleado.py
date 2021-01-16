import unittest

from prueba_2.empleado import Empleado


class EmpleadoTestCase(unittest.TestCase):
    def test__instancia_calculadora(self):
        empleado = Empleado(100)
        self.assertIsInstance(empleado, Empleado)

    def test__prestamo_no_aplica(self):
        empleado = Empleado(100)
        self.assertRaises(ValueError, empleado.solicita_prestamo, 101)

    def test__prestamo_aplica(self):
        empleado = Empleado(100)
        empleado.solicita_prestamo(30)

        self.assertEqual(empleado.sueldo, 70)