from database.DB_connect import DBConnect
from model.gene import Gene
class DAO:

    @staticmethod
    def get_geni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM gene """

        cursor.execute(query)

        for row in cursor:
            result.append(Gene(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_cromosomi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT cromosoma FROM gene WHERE cromosoma>0 """

        cursor.execute(query)

        for row in cursor:
            result.append(row['cromosoma'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_connessioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT g1.cromosoma as cromosoma1, g2.cromosoma as cromosoma2, sum(correlazione) as peso
                    FROM interazione i, 
                    (SELECT DISTINCT id, cromosoma FROM gene WHERE cromosoma > 0) g1,
                    (SELECT DISTINCT id, cromosoma FROM gene WHERE cromosoma > 0) g2
                    WHERE i.id_gene1 = g1.id and i.id_gene2=g2.id and g1.cromosoma<>g2.cromosoma 
                    GROUP BY g1.cromosoma, g2.cromosoma
 """
        cursor.execute(query)

        for row in cursor:
            result.append((row['cromosoma1'], row['cromosoma2'], row['peso']))

        cursor.close()
        conn.close()
        return result


