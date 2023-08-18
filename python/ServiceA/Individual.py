import json
import uuid

import psycopg2


class Individual:
    def __init__(self,id,databaseId,firstName,lastName,dateOfBirth,job):
        self.id = id
        self.databaseId = databaseId
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = str(dateOfBirth)
        self.job = job

    @staticmethod
    def fromDb(dbRes):
        (id, databaseId, firstName, lastName, dateOfBirth, job) = dbRes
        return Individual(id,databaseId,firstName,lastName,dateOfBirth,job)

    @staticmethod
    def get(id,conn):
        with conn.cursor() as curs:
            curs.execute("SELECT * FROM individual WHERE id = %s", (id,))
            res = curs.fetchone()
            if res == None:
                print("Oops!, no such individual ")
            else:
                indv = Individual.fromDb(res)
                print(str(indv.toJSON()))
                return indv
        return None

    def store(self,conn):
        with conn.cursor() as curs:
            try:
                curs.execute("""
                INSERT INTO individual (id, database_id, first_name, last_name, date_of_birth, job)
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
        return (self.id, self.databaseId, self.firstName, self.lastName, self.dateOfBirth, self.job )

    @staticmethod
    def fetch_all(conn):
        result = []
        with conn.cursor() as curs:
            curs.execute("SELECT * FROM individual")

            rows = curs.fetchall()

            for row in rows:
                indv = Individual.fromDb(row)
                result.append(indv)

        return result