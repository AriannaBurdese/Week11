from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.object import Object

class DAO():
    def __init__(self):
        pass


    @staticmethod #posso non mettere self, e non devo creare oggetto DAO
    def readObjects():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True) #cursore accessibile come dizionario
        query = "SELECT * FROM objects" #query per estrarre oggetti
        cursor.execute(query)
        for row in cursor:
            #result.append(Object(row["object_id"], row["object_name"]))
            result.append(Object(**row)) # ** fa l'unpacking del dizionario, tiriamo fuori tutte le coppie chiabi_dizionario

        def readConnessioni(objects_dict):
            conn = DBConnect.get_connection()
            result = []
            cursor = conn.cursor(dictionary=True)  # cursore accessibile come dizionario
            query = """select eo1.object_id, eo2.object_id
                    from exhibition_objects eo1, exhibition_objects eo2
                    where eo1.exhibition_id = eo2.exhibition_id 
                    and eo1.object_id < eo2.object_id 
                    group by eo1.object_id , eo2.object_id """
            cursor.execute(query)
            for row in cursor:
                o1 = objects_dict[row["o1"]]
                o2 = objects_dict[row["o2"]]
                peso = objects_dict[row["peso"]]
                result.append(Connessione(o1, o2, peso))


        cursor.close()
        conn.close()
        return result

