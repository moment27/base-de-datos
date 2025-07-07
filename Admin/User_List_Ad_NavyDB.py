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
    
    def Crear_Usuario(self,usuario,password,categoria):
        try:
            con = Conexion().ConexionBD()
            cursor = con.cursor()
            sql = "INSERT INTO usuario (nombre,password,categoria) VALUES (%s,%s,%s);"
            cursor.execute(sql, (usuario,password,categoria))
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

    def Eliminar_Usuario(self,id_usuario):
        conn=Conexion().ConexionBD()
        cursor=conn.cursor()
        sql="DELETE FROM usuario WHERE id_user=%s;"
        cursor.execute(sql, (id_usuario,))
        conn.commit()
        conn.close()

    def Obtener_Cat_Usuario(self,nombre,usuario):
        try:
            con = Conexion().ConexionBD()
            cursor = con.cursor()
            sql = "SELECT categoria FROM usuario WHERE nombre=%s AND password=%s;"
            cursor.execute(sql, (nombre,usuario))
            resultado = cursor.fetchone()
            cursor.close()
            con.close()

            if resultado:
                return resultado[0]
            else:
                return None
        
        except mysql.connector.Error as error:
            print(f"Error al verificar categoria/usuario {error}")
            return None     

    def Editar_Usuario(self, id_usuario, nuevo_usuario, nueva_password, nueva_categoria):
        try:
            con = Conexion().ConexionBD()
            cursor = con.cursor()
            sql = "UPDATE usuario SET nombre=%s, password=%s, categoria=%s WHERE id_user=%s;"
            cursor.execute(sql, (nuevo_usuario, nueva_password, nueva_categoria, id_usuario))
            con.commit()
            cursor.close()
            con.close()

            return True
        
        except mysql.connector.Error as error:
            print(f"Error al editar el usuario {error}")
            return False
        except mysql.connector.IntegrityError as error:
            print(f"Error de integridad al editar el usuario: {error}")
            return False

    def Actualizar_Contraseña(self,nombre_usuario,new_passwd):
        try:
            con=Conexion().ConexionBD()
            cursor=con.cursor()
            sql="UPDATE usuario SET password=%s WHERE nombre=%s;"
            cursor.execute(sql,(new_passwd,nombre_usuario))
            con.commit()
            cursor.close()
            con.close()

            return True
        except mysql.connector.Error as error:
            print(f"Error al actualizar {error}")
            return False