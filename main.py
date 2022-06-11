import os
import psycopg2

from datetime import datetime




def exec_statement(conn, stmt):

    try:
        with conn.cursor() as cur:
            cur.execute(stmt)
            row = cur.fetchone()
            conn.commit()
            if row: print(row[0])
    except psycopg2.ProgrammingError:
        return


def database():
    counter = 0

    # Connect to CockroachDB
    connection = psycopg2.connect(os.environ['DATABASE_URL'])
    #if label is a knife or gun, insert timestamp into database
    #if label == 'knife' or label == 'gun':
        #exec_statement(connection, "INSERT INTO timestamps (timestamp) VALUES (now())")
        
    statements = [
        # CREATE the timestamp table
        "CREATE TABLE test IF NOT EXISTS (a INT PRIMARY KEY, b TIMESTAMPTZ)",

        #remove previous data
        #"DELETE FROM timestamps VALUES *",
        # SELECT a row from the messages table
        f"INSERT INTO test VALUES ({counter}, '{datetime.now()}')",
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
