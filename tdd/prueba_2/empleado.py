class Empleado:
    sueldo = 0

    def __init__(self, sueldo):
        self.sueldo = sueldo

    def solicita_prestamo(self, cantidad):
        if (cantidad > self.sueldo):
            raise ValueError('No puedes solicitar un prestamo mayor a tu sueldo')

        self.sueldo = self.sueldo - cantidad

    def get_sueldo(self):
        print(f'El sueldo del empleado es:', self.sueldo)

