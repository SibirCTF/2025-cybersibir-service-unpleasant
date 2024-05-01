import psycopg2


conn = psycopg2.connect(host='localhost',
                        port=5432,
                        database='flask_test',  # TODO: database name
                        user='postgres',
                        password='postgres')

cursor = conn.cursor()

