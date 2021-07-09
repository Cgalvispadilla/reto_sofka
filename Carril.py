class Carril():

    def __init__(self, carro, posicion, tamanio):
        self.__carro = carro
        self.__posicion=posicion
        self.__tamanio=tamanio*1000

    def get_carro(self):
        return self.__carro
    def set_carro(self, value):
        self.__carro = value
    def get_posicion(self):
        return self.__posicion
    def set_posicion(self, value):
        self.__posicion = value
    def get_tamanio(self):
        return self.__tamanio
    def set_tamanio(self, value):
        self.__tamanio = value    

    carro = property(get_carro, set_carro, None, None)
    posicion = property(get_posicion, set_posicion, None, None)
    tamanio = property(get_tamanio, set_tamanio,None,None)