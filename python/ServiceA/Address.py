import uuid

import psycopg2
import json

class Address:
    def __init__(self,id,databaseId,country,city,street,zipcode):
        self.id = id
        self.databaseId = databaseId
        self.country = country
        self.city = city
        self.street = street
        self.zipcode = zipcode


    @staticmethod
    def fromDb(dbRes):
        (id, databaseId, country, city, street, zipcode) = dbRes
        return Address(id,databaseId,country,city,street,zipcode)

    @staticmethod
    def get(id,conn):
        with conn.cursor() as curs:
            curs.execute("SELECT * FROM address WHERE id = %s", (id,))
            res = curs.fetchone()
            if res == None:
                print("Oops!, no such address ")
            else:
                addr = Address.fromDb(res)
                print(str(addr.toJSON()))
                return addr
        return None

    def store(self,conn):
        with conn.cursor() as curs:
            try:
                curs.execute("""
                INSERT INTO address (id, database_id, country, city, street, zipcode)
                VALUES (%s, %s, %s, %s, %s, %s);
                """,self.toTupl())

            # a more robust way of handling errors
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
                print(str(self.toJSON()))

        conn.commit()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def toTupl(self):
        return (self.id, self.databaseId, self.country, self.city, self.street, self.zipcode )

    @staticmethod
    def fetch_all(conn):
        result = []
        with conn.cursor() as curs:
            curs.execute("SELECT * FROM address")

            rows = curs.fetchall()

            for row in rows:
                addr = Address.fromDb(row)
                result.append(addr)

        return result