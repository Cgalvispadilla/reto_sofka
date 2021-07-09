import Juego as j
import Podio as p
import DB.funciones_db as fun
#import DB.eliminar_datos as dele

def pedirNumeroEntero():
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')
    return num

salir = False
opcion = 0
sol = None

while not salir:
    
    print("1. Jugar")
    print("2. Ver Resultados")
    print("3. Borras todos los resultados")
    print("4. Salir")
  

    print("Elige una opcion")

    opcion = pedirNumeroEntero()

    if opcion == 1:
        juego= j.Juego()
        ganadores=juego.iniciar_juego()
        gan=""
        num=1
        for i in ganadores:
            gan+=str(i[1].get_conductor()+"#") 
        podio =p.Podio(gan.split("#")[0],gan.split("#")[1],gan.split("#")[2])
        info = fun.mostrarInfo()
        if len(info)>0:
            for x in info:
                if x[1]==podio.get_primer_lugar():
                    num+=1       
            else:
                fun.agregar_podio(podio.get_primer_lugar(),podio.get_segundo_lugar(),podio.get_tercer_lugar(),num)
        else:
            fun.agregar_podio(podio.get_primer_lugar(), podio.get_segundo_lugar(), podio.get_tercer_lugar(),1)         
        print(podio.mostrar_podio())
        podio.limpiar_podio()
    if opcion==2:
        info = fun.mostrarInfo()
        if len(info)>0:
            for i in info:
                print(i)
        else:
            print('no hay registros')            
    if opcion==3:
        delete=input("Si esta seguro en eliminar todos los registros escriba 'Si' de lo contrario 'No'")
        if delete=="SI" or delete=="Si" or delete=="sI" or delete=="si":
            fun.eliminar_todo()
        else:
            print("No se elimino nada")    
    if opcion==4:
        fun.cerrar_conexion()
        salir=True
        
                    
    
    
    
    