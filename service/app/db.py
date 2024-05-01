import psycopg2
# TODO: Feed
# TODO: Create-abomination

# TODO: sqlescape


def get_db_connection():
	conn = psycopg2.connect(host='localhost',
	                        port=5432,
	                        database='flask_test',  # TODO: database name
	                        user='postgres',
	                        password='postgres')
	return conn


def register_user(username, password):
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute(f"SELECT id FROM users WHERE username='{username}'")
	username_exists = cursor.fetchall()
	if len(username_exists) > 0:
		return False
	cursor.execute(f"INSERT INTO users(username, password) VALUES ('{username}','{password}')")
	cursor.execute(f"SELECT id FROM users WHERE username='{username}'")
	id = cursor.fetchall()
	conn.commit()
	conn.close()
	return id


def login_user(username, password):
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute(f"SELECT id FROM users WHERE username='{username}' AND password='{password}'")
	user = cursor.fetchall()
	if not user:
		return False
	conn.commit()
	conn.close()
	return user[0][0]


def feed():  # TODO: Test
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute(f"SELECT * FROM abominations WHERE is_private = False")
	abominations = cursor.fetchall()
	conn.commit()
	conn.close()
	return abominations