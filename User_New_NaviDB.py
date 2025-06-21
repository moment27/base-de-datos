from Conexion_MySQL import *

class Usuarios:

    def ingresarUsuarios(Nombre,Password):

        try:
            con=Conexion().ConexionBD()
            cursor=con.cursor()
            sql="insert into usuario values(null,%s,%s);"
            #abreviatura de parámetros
            prm=(Nombre,Password)
            cursor.execute(sql,prm)
            con.commit()
            print(cursor.rowcount,"Usuario Creado")
            cursor.close()

        except mysql.connector.Error as error:
            print(f"Error de ingreso de datos {error}")