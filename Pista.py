class Pista():
    def __init__(self, id,carriles,kilometros):
        self.__id=id
        self.__carriles = carriles
        self.__kilometros=kilometros
    def get_id(self):
        return self.__id
    def set_id(self, value):
        self.__id=value
    def get_carriles(self):
        return self.__carriles
    def set_carriles(self, value):
        self.__carriles = value
    
    def get_kilometros(self):
        return self.__kilometros
    def set_kilometros(self, value):
        self.__kilometros = value    

    carriles = property(get_carriles, set_carriles, None, None) 
    kilometros = property(get_kilometros,set_kilometros,None,None)