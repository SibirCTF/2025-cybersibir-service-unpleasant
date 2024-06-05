import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# launch in dockerfile? (command = [python, init_db.py])

# create_db
conn = psycopg2.connect(host='localhost',
                        port=5432,
                        # database='flask_test',  # database name
                        user='postgres',
                        password='postgres')

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS flask_db;")  # more friendly solution?
cursor.execute("CREATE DATABASE flask_db;")

conn.commit()
cursor.close()
conn.close()

# create_tables
conn = psycopg2.connect(host='localhost',
                        port=5432,
                        database='flask_test',  # database name
                        user='postgres',
                        password='postgres')

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS abominations;")
cursor.execute("DROP TABLE IF EXISTS implants;")
cursor.execute("DROP TABLE IF EXISTS users;")

cursor.execute("CREATE TABLE IF NOT EXISTS users("
               "id SERIAL PRIMARY KEY, "
               "username character varying(50) NOT NULL, "
               "password character varying(50) NOT NULL);"
               )

cursor.execute("CREATE TABLE IF NOT EXISTS implants("
               "bodypart character varying(50) NOT NULL,"
               "name character varying(50) NOT NULL,"
               "id integer NOT NULL);"
               )

cursor.execute(f"INSERT INTO implants"
               f"(bodypart, name, id) VALUES "
               f"('head', 'carbon skull', 1),"
               f"('head', 'cosmic antenn', 2),"
               f"('head', 'integrated makarov', 3),"
               f"('eye', 'laser pointer', 1),"
               f"('eye', 'y-ray vision', 2),"
               f"('eye', 'x10 zoom', 3),"
               f"('body', 'civilian camouflage', 1),"
               f"('body', 'visibility suit', 2),"
               f"('body', 'nirvana t-shirt', 3),"
               f"('arm', 'bazooka', 1),"
               f"('arm', 'another bazooka', 2),"
               f"('arm', 'can-closer', 3),"
               f"('leg', 'six-fingered foot', 1),"
               f"('leg', 'small pocket (can fit 0,331% of phone)', 2),"
               f"('leg', 'default leg', 3);")

cursor.execute("CREATE TABLE IF NOT EXISTS abominations("
               "id SERIAL NOT NULL PRIMARY KEY,"
               "id_owner integer NOT NULL REFERENCES users (id),"
               "name character varying(50) NOT NULL,"
               "gender character varying(50) NOT NULL,"
               "is_private boolean NOT NULL,"
               "head integer NOT NULL,"
               "eye integer NOT NULL,"
               "body integer NOT NULL,"
               "arm integer NOT NULL,"
               "leg integer NOT NULL);"
               )

conn.commit()
cursor.close()
conn.close()
