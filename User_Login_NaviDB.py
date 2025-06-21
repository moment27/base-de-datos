from Conexion_MySQL import *

class LoginUsuario:

    def IngresarUsuario(self,Nombre,Password) :
        try:
            con=Conexion().ConexionBD()
            cursor=con.cursor()
            sql="select * FROM usuario WHERE Nombre=%s AND Password=%s"
            #abreviatura de parámetros
            prm=(Nombre,Password)
            cursor.execute(sql,prm)
            resultado=cursor.fetchone()
            cursor.close()
            con.close()

            if resultado:
                print("Inicio de Sesión exitoso")
                return True
            else:
                print("Error al iniciar sesión")
                return False

        except mysql.connector.Error as error:
            print(f"Error de intento de sesion {error}")