from Conexion_MySQL import *

class L_Tiempo:

    def Lista_Tiempo(self) :
        try:
            con=Conexion().ConexionBD()
            cursor=con.cursor()
            sql="select * FROM tiempo;"
            #abreviatura de parámetros
            cursor.execute(sql)
            resultado=cursor.fetchall()
            cursor.close()
            con.close()

            return resultado
        
        except mysql.connector.Error as error:
            print(f"Error al obtener tiempo {error}")
            return None
        
       