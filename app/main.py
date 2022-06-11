import os
import psycopg2


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

    # Connect to CockroachDB
    connection = psycopg2.connect(os.environ['DATABASE_URL'])

    statements = [
        # CREATE the flags table

        #"CREATE TABLE timestamps IF NOT EXISTS (a INT PRIMARY KEY, b TIMESTAMPTZ)",
        # INSERT a row into the flag table
        #"SHOW COLUMNS FROM timestamps",
        #"INSERT INTO timestamps VALUES (4, TIMESTAMPTZ '2016-03-26 10:10:10-05:00'), (5, TIMESTAMPTZ '2016-03-26')",
        # SELECT a row from the messages table
        "SELECT b FROM timestamps"
    ]

    for statement in statements:
        exec_statement(connection, statement)

    # Close communication with the database
    
    return connection


if __name__ == "__main__":
    database()
