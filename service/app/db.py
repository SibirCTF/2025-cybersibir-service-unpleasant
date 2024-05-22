import psycopg2
# TODO: Feed
# TODO: Create-abomination

# TODO: sqlescape


# TODO: copy to .env or .config file
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
	cursor.execute(f"SELECT * FROM abominations WHERE is_private = False")  # todo: check for user_id ( * or * )
	_abominations = cursor.fetchall()
	conn.commit()
	conn.close()
	return _abominations


def abomination(abom_id, user_id):
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute(f"SELECT * FROM abominations WHERE id = {abom_id}")
	_abomination = cursor.fetchall()
	if not abomination:
		return False
	# TODO: parse json, get user_id, check
	conn.commit()
	conn.close()
	return _abomination


def my_abominations(user_id):
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute(f"SELECT * FROM abominations WHERE id = {user_id}")
	_my_abominations = cursor.fetchall()
	conn.commit()
	conn.close()
	return _my_abominations


def create_abomination(id_owner, name, gender, is_private, head, eye, body, arm, leg):  # TODO
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute(f"INSERT INTO abominations"
	               f"(id_owner, name, gender, is_private, head, eye, body, arm, leg) VALUES "
	               f"({id_owner}, {name}, {gender}, {is_private}, {head}, {eye}, {body}, {arm}, {leg});")
	# todo как айдишник постать) есть идея через my_abominations. Или ваще хуй забить.
	conn.commit()
	conn.close()
	return abomination
