import os
import psycopg2

from datetime import datetime

from sklearn.semi_supervised import LabelSpreading



def exec_statement(conn, stmt):

    try:
        with conn.cursor() as cur:
            cur.execute(stmt)
            row = cur.fetchone()
            conn.commit()
            if row: print(row[0])
    except psycopg2.ProgrammingError:
        return


def database(label):
    counter = 0
    frameCount = 0

    # Connect to CockroachDB
    connection = psycopg2.connect(os.environ['DATABASE_URL'])
    #if label is a knife or gun, insert timestamp into database
    if label == 'knife' or label == 'pistol':
        exec_statement(connection, f"INSERT INTO test VALUES ({counter}, '{datetime.now()}')",)
        counter += 1
        frameCount += 1

    if frameCount >= 10:
        print("severe threat")

    statements = [
        # CREATE the timestamp table
        "CREATE TABLE test IF NOT EXISTS (a INT PRIMARY KEY, b TIMESTAMPTZ)",

        "SELECT b FROM test"
    ]

    for statement in statements:
        try:
            exec_statement(connection, statement)
            counter = counter + 1
        except:
            exec_statement(connection, "rollback")
            exec_statement(connection, statement)
            counter = counter + 1

    # Close communication with the database
    
    return connection


if __name__ == "__main__":
    database()
