class Jugador():

    def __init__(self, nombre, puntos=0):
        self.__nombre = nombre
        self.__puntos=puntos

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, value):
        self.__nombre = value
    def get_puntos(self):
            return self.__puntos
    def set_puntos(self, value):
        self.__puntos = value

    nombre = property(get_nombre, set_nombre, None, None)
    puntos = property(get_puntos, set_puntos, None, None)
