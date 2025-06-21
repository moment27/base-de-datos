from Conexion_MySQL import *

class L_Categoria:

    def Lista_Categoria(self) :
        try:
            con=Conexion().ConexionBD()
            cursor=con.cursor()
            sql="select * FROM categoria"
            #abreviatura de parámetros
            cursor.execute(sql)
            resultado=cursor.fetchall()
            cursor.close()
            con.close()

            return resultado
        
        except mysql.connector.Error as error:
            print(f"Error al obtener categoria {error}")
            return None
        
    def Lista_Categoria_Personalizada(self,offset=0, limit=12):
        try:
            con = Conexion().ConexionBD()
            cursor = con.cursor()
            sql = "SELECT * FROM categoria LIMIT %s OFFSET %s;"
            cursor.execute(sql, (limit, offset))
            resultado = cursor.fetchall()
            cursor.close()
            con.close()

            return resultado
        
        except mysql.connector.Error as error:
            print(f"Error al obtener categoria personalizada {error}")
            return []
        
    def Cantidad_Categoria(self):
        try:
            con = Conexion().ConexionBD()
            cursor = con.cursor()
            sql = "SELECT COUNT(*) FROM categoria;"
            cursor.execute(sql)
            resultado = cursor.fetchone()[0]
            cursor.close()
            con.close()

            return resultado
        
        except mysql.connector.Error as error:
            print(f"Error al obtener cantidad de categorias {error}")
            return 0

    def Crear_Categoria(self, nombre):
        try:
            con = Conexion().ConexionBD()
            cursor = con.cursor()
            sql = "INSERT INTO categoria (nombre) VALUES (%s);"
            cursor.execute(sql, (nombre,))
            con.commit()
            cursor.close()
            con.close()

            return True
        
        except mysql.connector.Error as error:
            print(f"Error al crear categoria {error}")
            return False
        except mysql.connector.IntegrityError as error:
            print(f"Error de integridad al crear categoria: {error}")
            return False            