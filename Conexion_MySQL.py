import mysql.connector

usuario="root"
pswd=""
host="localhost"
bd="navigo"

class Conexion:
    
    def ConexionBD(self):
        try:
            conexion=mysql.connector.connect(user=usuario,password=pswd,
                                             host=host,database=bd,port=3306)
            print("Conexión exitosa")
            return conexion

        except mysql.connector.Error as error:
            print(f"Error exitoso {error}")

            return conexion
          