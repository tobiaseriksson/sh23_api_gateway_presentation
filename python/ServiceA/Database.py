import uuid

import faker
import psycopg2
from Individual import Individual
from Address import Address
from Customer import Customer
from DataGenerator import DataGenerator
import random as rand
import psycopg2
from opentelemetry.instrumentation.psycopg2 import Psycopg2Instrumentor



def dump_db_info(conn):
    with conn.cursor() as curs:

        try:
            # simple single row system query
            curs.execute("SELECT version()")

            # returns a single row as a tuple
            single_row = curs.fetchone()

            # use an f-string to print the single tuple returned
            print(f"{single_row}")

            # simple multi row system query
            curs.execute("SELECT query, backend_type FROM pg_stat_activity")

            # a default install should include this query and some backend workers
            many_rows = curs.fetchmany(5)

            # use the * unpack operator to print many_rows which is a Python list
            print(*many_rows, sep="\n")

        # a more robust way of handling errors
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)



def fill_database(conn):
    print("Empty tables first")
    with conn.cursor() as curs:
        curs.execute("TRUNCATE individual;")
        curs.execute("TRUNCATE address;")
        curs.execute("TRUNCATE customer;")
    conn.commit()

    print("Fill database with fake data")
    data_generator = DataGenerator()
    number_of_customers = 100
    for id in range(number_of_customers):
        indv = data_generator.generate_individual(id)
        addr = data_generator.generate_address(id)
        cust = data_generator.generate_customer(id,indv,addr)
        indv.store(conn)
        addr.store(conn)
        cust.store(conn)


import os

DB_HOST = os.getenv("DB_HOST")
if( DB_HOST == None ):
    DB_HOST = 'localhost'
print("DB_HOST = "+DB_HOST)

DB_PORT = os.getenv("DB_PORT")
if( DB_PORT == None ):
    DB_PORT = 5432
else:
    DB_PORT = int(DB_PORT)
print("DB_PORT = "+str(DB_PORT))

DB = os.getenv("DB")
if( DB == None ):
    DB = 'sh23'
print("DB = "+DB)

DB_PASSWD = os.getenv("DB_PASSWD")
if( DB_PASSWD == None ):
    DB_PASSWD = 'sh2023'
print("DB_PASSWD = "+DB_PASSWD)

DB_USER = os.getenv("DB_USER")
if( DB_USER == None ):
    DB_USER = 'tobias'
print("DB_USER = "+DB_USER)


conn = None

def dbConn():
    Psycopg2Instrumentor().instrument( skip_dep_check=True )
    global conn
    if( conn == None ):
        conn = psycopg2.connect(host=DB_HOST,
                            port=DB_PORT,
                            database=DB,
                            user=DB_USER,
                            password=DB_PASSWD)
    else:
        # reusing conn object
        pass

    return conn

