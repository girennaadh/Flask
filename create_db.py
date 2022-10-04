import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from utils import postgres_host, postgres_port, postgres_user, postgres_pwd, database


def create_database():
    print("Creating Database..")
    conn = None
    try:
        conn = psycopg2.connect(host=postgres_host, user=postgres_user, password=postgres_pwd, port=postgres_port)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        exist = ""
        cur = conn.cursor()
        commands = ["SELECT datname FROM pg_catalog.pg_database WHERE datname = '%s';" %database]
        for command in commands:
            cur.execute(command)
            exist = cur.fetchone()
            cur.close()
        if exist:
            conn.commit()
        else:
            cur = conn.cursor()
            commands = ["create database %s;"%database]
            for command in commands:
                cur.execute(command)
                cur.close()
                conn.commit()
        print("Created Database..")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()