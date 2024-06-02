import psycopg2
# launch in dockerfile? (command = [python, init_db.py])

conn = psycopg2.connect(host='localhost',
                        port=5432,
                        database='flask_test',  # TODO: database name
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
