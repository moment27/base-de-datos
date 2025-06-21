from Conexion_MySQL import *

class L_Usuario:

    def Lista_Usuario(self) :
        try:
            con=Conexion().ConexionBD()
            cursor=con.cursor()
            sql="select * FROM usuario;"
            #abreviatura de parámetros
            cursor.execute(sql)
            resultado=cursor.fetchall()
            cursor.close()
            con.close()

            return resultado
        
        except mysql.connector.Error as error:
            print(f"Error al obtener usuarios {error}")
            return None
    def Cantidad_Usuarios(self):
        try:
            con = Conexion().ConexionBD()
            cursor = con.cursor()
            sql = "SELECT COUNT(*) FROM usuario;"
            cursor.execute(sql)
            resultado = cursor.fetchone()[0]
            cursor.close()
            con.close()

            return resultado
        
        except mysql.connector.Error as error:
            print(f"Error al contar usuarios {error}")
            return 0 
    
    def Crear_Usuario(self,usuario,password):
        try:
            con = Conexion().ConexionBD()
            cursor = con.cursor()
            sql = "INSERT INTO categoria (nombre,password) VALUES (%s,%s);"
            cursor.execute(sql, (usuario,password))
            con.commit()
            cursor.close()
            con.close()

            return True
        
        except mysql.connector.Error as error:
            print(f"Error al crear el usuario {error}")
            return False
        except mysql.connector.IntegrityError as error:
            print(f"Error de integridad al crear el usuario: {error}")
            return False 

