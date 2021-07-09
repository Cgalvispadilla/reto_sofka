class Podio():

    def __init__(self, primer_lugar, segundo_lugar, tercer_lugar):
        self.__primer_lugar = primer_lugar
        self.__segundo_lugar = segundo_lugar
        self.__tercer_lugar = tercer_lugar

    def get_primer_lugar(self):
        return self.__primer_lugar


    def get_segundo_lugar(self):
        return self.__segundo_lugar


    def get_tercer_lugar(self):
        return self.__tercer_lugar


    def set_primer_lugar(self, value):
        self.__primer_lugar = value


    def set_segundo_lugar(self, value):
        self.__segundo_lugar = value


    def set_tercer_lugar(self, value):
        self.__tercer_lugar = value

    def limpiar_podio(self):
        self.set_primer_lugar("")
        self.set_segundo_lugar("")
        self.set_tercer_lugar("")
        
    def mostrar_podio(self):
        text=f" Primer lugar {self.get_primer_lugar()}, segundo lugar {self.get_segundo_lugar()}, tercer lugar {self.get_tercer_lugar()}" 
        return text  
    primer_lugar = property(get_primer_lugar, set_primer_lugar, None, None)
    segundo_lugar = property(get_segundo_lugar, set_segundo_lugar, None, None)
    tercer_lugar = property(get_tercer_lugar, set_tercer_lugar, None, None)
