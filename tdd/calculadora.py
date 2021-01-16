class Calculadora:
    def __init__(self):
        self.valor = 0

    def suma(self, numero_1, numero_2):
        """Suma 2 valores"""
        self.valor = numero_1 + numero_2

    def multiplica(self, numero_1, numero_2):
        """multiplica 2 valores"""
        if numero_1 == 0 or numero_2 == 0:
            raise ValueError('No puedes multiplicar por cero')

        self.valor = numero_1 * numero_2
