from rest_framework import serializers

class Comentario:
    def __init__(self, correo, mensaje, autor):
        self.correo = correo
        self.mensaje = mensaje
        self.autor = autor


class ComentarioSerializador(serializers.Serializer):
    correo = serializers.EmailField()
    mensaje = serializers.CharField(max_length=200)
    autor = serializers.CharField(max_length=30)


def print_name():
    print(__name__)


if __name__ == '__main__':
    comentario = Comentario('usuario@gmail.com', 'Hola mundo', 'usuario')
    print(comentario)