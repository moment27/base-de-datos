import pymongo
import pymongo.errors

MONGO_HOST="localhost"
PUERTO="27017"
TIEMPO_ESPERA=1000
MONGO_URI="mongodb://"+MONGO_HOST+":"+PUERTO+"/"


try:
    cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=TIEMPO_ESPERA)
    cliente.server_info()
    print("Conexión exitosa")
    cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as error:
    print("Tiempo exedido "+error)
except pymongo.errors.ConnectionFailure as error2:
    print("Fallo al conectarse a mongodb"+error2)
