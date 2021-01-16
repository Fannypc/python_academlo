class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f'La informacion del usuario es: ')
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')


class Alumno(Persona):
    def __init__(self, nombre, edad, calificacion):
        super().__init__(nombre, edad)
        self.calificacion=calificacion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Calificacion: {self.calificacion}')
        print('************************************')


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Sueldo: {self.sueldo}')
        print('************************************')


alumno_1 = Alumno('Juan', 13, 10)
alumno_1.mostrar_informacion()
alumno_2 = Alumno ('Pedro', 20, 9)
alumno_2.mostrar_informacion()
empleado_1 = Empleado('Carlos', 30, 100)
empleado_1.mostrar_informacion()