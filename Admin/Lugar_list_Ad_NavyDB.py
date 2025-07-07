from Conexion_MySQL import *

class L_Lugar:

    def Lista_Lugar(self) :
        try:
            con=Conexion().ConexionBD()
            cursor=con.cursor()
            sql="select * FROM lugares;"
            #abreviatura de parámetros
            cursor.execute(sql)
            resultado=cursor.fetchall()
            cursor.close()
            con.close()

            return resultado
        
        except mysql.connector.Error as error:
            print(f"Error al obtener lugar {error}")
            return None

    def Lista_Lugar_Personalizada(self,offset=0, limit=12):
        try:
            con = Conexion().ConexionBD()
            cursor = con.cursor()
            sql = "SELECT * FROM lugares ORDER BY id_lugar LIMIT %s OFFSET %s;"
            cursor.execute(sql, (limit, offset))
            resultado = cursor.fetchall()
            cursor.close()
            con.close()

            return resultado
        
        except mysql.connector.Error as error:
            print(f"Error al obtener lugar personalizado {error}")
            return []
        
    def Cantidad_Lugar(self):
        try:
            con = Conexion().ConexionBD()
            cursor = con.cursor()
            sql = "SELECT COUNT(*) FROM lugares;"
            cursor.execute(sql)
            resultado = cursor.fetchone()[0]
            cursor.close()
            con.close()

            return resultado
        
        except mysql.connector.Error as error:
            print(f"Error al contar lugares {error}")
            return 0    

    def Lugares_por_Distrito(self,nombre_distrito):
        try:
            con=Conexion().ConexionBD()
            cursor=con.cursor()
            sql="SELECT l.* from lugares l join distrito d on l.distrito_id_distrito = d.id_distrito WHERE d.nombre=%s";
            cursor.execute(sql,(nombre_distrito,))
            resultado=cursor.fetchall()
            cursor.close()
            con.close()

            return resultado
        except mysql.connector.Error as error:
            print(f"Error al obtener lugares {error}")      
            return []