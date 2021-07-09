class Carro:

    def __init__(self, conductor):
        self.__conductor = conductor


    def get_conductor(self):
        return self.__conductor


    def set_conductor(self, value):
        self.__conductor = value

        
    conductor = property(get_conductor, set_conductor, None, None)
