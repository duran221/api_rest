#Import connector for Postgre SQL.
import psycopg2

def crear_conexion():
    conn = psycopg2.connect(database="students",
                            user="postgres",
                            password="6885",
                            host="localhost", port="5432")
    # create a cursor
    cur = conn.cursor()
    return conn, cur