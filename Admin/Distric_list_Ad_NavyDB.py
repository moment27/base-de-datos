from Conexion_MySQL import *

class L_Distrito:

    def Lista_Distrito(self) :
        try:
            con=Conexion().ConexionBD()
            cursor=con.cursor()
            sql="select * FROM distrito;"
            #abreviatura de parámetros
            cursor.execute(sql)
            resultado=cursor.fetchall()
            cursor.close()
            con.close()

            return resultado
        
        except mysql.connector.Error as error:
            print(f"Error al obtener distrito {error}")
            return None

    def Lista_Distrito_Personalizada(self,offset=0, limit=12):
        try:
            con = Conexion().ConexionBD()
            cursor = con.cursor()
            sql = "SELECT * FROM distrito LIMIT %s OFFSET %s;"
            cursor.execute(sql, (limit, offset))
            resultado = cursor.fetchall()
            cursor.close()
            con.close()

            return resultado
        
        except mysql.connector.Error as error:
            print(f"Error al obtener distrito personalizado {error}")
            return []

    def Cantidad_Distric(self):
        try:
            con = Conexion().ConexionBD()
            cursor = con.cursor()
            sql = "SELECT COUNT(*) FROM distrito;"
            cursor.execute(sql)
            resultado = cursor.fetchone()[0]
            cursor.close()
            con.close()

            return resultado
        
        except mysql.connector.Error as error:
            print(f"Error al contar distritos {error}")
            return 0

    def Crear_Distric(self, nombre):
        try:
            con = Conexion().ConexionBD()
            cursor = con.cursor()
            sql = "INSERT INTO distrito (nombre) VALUES (%s);"
            cursor.execute(sql, (nombre,))
            con.commit()
            cursor.close()
            con.close()

            return True
        
        except mysql.connector.Error as error:
            print(f"Error al crear distrito {error}")
            return False
        except mysql.connector.IntegrityError as error:
            print(f"Error de integridad al crear distrito: {error}")
            return False        