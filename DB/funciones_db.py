import psycopg2
conexion = psycopg2.connect(user="postgres", 
                            password="ADMIN", 
                            host="127.0.0.1", 
                            port="5432", 
                            database="reto_db")
def cerrar_conexion():
    conexion.close()  
def agregar_podio(primero,segundo,tercer,cantidad):
    try:
        with conexion:
            with conexion.cursor() as cursor:
                sentencia ="INSERT INTO podio (primero, segundo, tercero, cantidad) VALUES (%s, %s, %s, %s)"
                valores=(primero,segundo, tercer, cantidad)
                cursor.execute(sentencia,valores,)
    except Exception as e:
        print("ocurrio el siguiente error:",e)            

        
 
def mostrarInfo():
    info=None
    try:
        with conexion:
            with conexion.cursor() as cursor:
                sentencia ="SELECT * FROM podio"
                cursor.execute(sentencia)
                registro= cursor.fetchall()
                info= registro
    except Exception as e:
        print("ocurrio el siguiente error:",e)            
    return info

def eliminar_todo():
    try:
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = 'DELETE FROM podio'
                cursor.execute(sentencia)
                registros_eliminados = cursor.rowcount
                print(f'Registros Eliminados: {registros_eliminados}')
    except Exception as e:
        print(f'Ocurrió un error: {e}')
    finally:
        conexion.close()    