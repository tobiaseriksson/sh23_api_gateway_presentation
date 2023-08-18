import uuid
import json
import uuid
import psycopg2

class Customer:
    def __init__(self,id,databaseId,email,individual_id,address_id):
        self.id = id
        self.databaseId = databaseId
        self.email = email
        self.individual_id = individual_id
        self.address_id = address_id

    @staticmethod
    def fromDb(dbRes):
        (id, databaseId, email, individual_id, address_id) = dbRes
        return Customer(id,databaseId,email,individual_id,address_id)

    @staticmethod
    def get(id,conn):
        with conn.cursor() as curs:
            curs.execute("SELECT * FROM customer WHERE id = %s", (id,))
            res = curs.fetchone()
            if res == None:
                print("Oops!, no such customer ")
            else:
                cust = Customer.fromDb(res)
                print(str(cust.toJSON()))
                return cust
        return None


    @staticmethod
    def get_by_email(email, conn):
        with conn.cursor() as curs:
            curs.execute("SELECT * FROM customer WHERE email = %s", (email,))
            res = curs.fetchone()
            if res == None:
                print("Oops!, no such customer ")
            else:
                cust = Customer.fromDb(res)
                print(str(cust.toJSON()))
                return cust
        return None


    def store(self,conn):
        with conn.cursor() as curs:
            try:
                curs.execute("""
                INSERT INTO customer (id, database_id, email, individual_id, address_id)
                VALUES (%s, %s, %s, %s, %s);
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
        return (self.id, self.databaseId, self.email, self.individual_id, self.address_id )


    @staticmethod
    def fetch_all(conn):
        result = []
        with conn.cursor() as curs:
            curs.execute("SELECT * FROM customer")

            rows = curs.fetchall()

            for row in rows:
                cust = Customer.fromDb(row)
                result.append(cust)

        return result