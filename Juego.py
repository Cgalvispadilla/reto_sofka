from Jugador import *
from Conductor import *
from Carro import *
from Carril import *
from Pista import *
import random
class Juego():
    def __init__(self) -> None:
        self.__id=(random.randint(1, 100000))
    def get_id(self):
        return self.__id
    def min_jugadores(self,num:int):
        if num>=3:
            return True
        else:
            return False  
    def cant_jugadores(self):
        n = input(f'Ingrese la el numero de jugadores (debe ser mayor a 3): ') 
        while(not n.isdigit()):
            print(f"el dato {n} ingresado no es un numero")
            n = input(f'Ingrese la el numero de jugadores (debe ser mayor a 3): ')
        while self.min_jugadores(int(n))==False:
            n = input('Ingrese la cantidada de jugadores (minimo deben ser 3): ')
        return int(n)
         
    def crear_jugadores(self,cant_jugadores:int):
        lista_jugadores=[]
        for i in range(cant_jugadores):
            nombre="jugador "+str(i+1)
            j=Jugador(nombre)
            lista_jugadores.append(j) 
        return lista_jugadores
    
    def crear_pista(self,cantidad_jugadores: int):
        n = input(f'Ingrese la el numero de Kilometros de la pista: ') 
        while(not n.isdigit()):
            print(f"el dato {n} ingresado no es un numero")
            n = input(f'Ingrese la el numero de Kilometros de la pista: ') 
        p = Pista(random.randint(1, 100),cantidad_jugadores, int(n))
        return p
    
    def crear_carros(self,jugadores: list,pista: Pista):
        lista_carros=[]
        for i in range(len(jugadores)):
            c = conductor(jugadores[i].get_nombre())
            carro= Carro(c.getNombre())   
            carril= Carril(carro,(i+1),pista.kilometros)
            #el antepenultimo cero hace referencia a la distancia que ha recorrido el carro
            lista_carros.append([pista.get_id(),carro,carril.get_posicion(),carril.get_tamanio(),0])
        return lista_carros    
    
    def movimiento_del_carro(self, carro):
        movimiento= random.randint(1, 6)*100
        
        return movimiento
    def info_carro(self, carro):
        texto=f" Pista: {carro[0]}, Conductor: {str(carro[1].get_conductor())}, Carril: {carro[2]},distacia recorrida: {carro[4]}"
        print(texto)       
        
    def configurar_juego(self):
        cant= self.cant_jugadores()
        lista_jugadores=self.crear_jugadores(cant)
        pista=self.crear_pista(len(lista_jugadores))
        carros= self.crear_carros(lista_jugadores,pista)
        return carros
        
    def iniciar_juego(self):
        carros=self.configurar_juego()
        cont,cont2=0,1
        listaGanadores=[]
        while True:
            for carro in carros:
                if carro[-1]>=carro[-2]:
                    cont+=1
                    listaGanadores.append(carro)
                    carros.remove(carro)
                carro[-1]+= self.movimiento_del_carro(carro)  
                print(f"-----movimiento {cont2}-----")
                self.info_carro(carro)
                cont2+=1
                if cont==3:
                    break
            if cont==3:
                    break              
        return listaGanadores         
   