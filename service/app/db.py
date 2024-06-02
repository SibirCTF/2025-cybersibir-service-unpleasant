import psycopg2
import json

# TODO: sqlescape?

# json_raw = """ {
# 	"id"	: 12,
# 	"name"	: name
# } """
# jsondata = json.loads(json_raw)


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
	cursor.close()
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
	cursor.close()
	conn.close()
	return user[0][0]


def feed(user_id):  # TODO: Test
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute(f"SELECT * FROM abominations WHERE is_private = False OR id_owner = {user_id}")
	feed_abominations = cursor.fetchall()
	conn.commit()
	cursor.close()
	conn.close()
	return feed_abominations


def abomination(abom_id, user_id):
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute(f"SELECT * FROM abominations WHERE id = {abom_id}")
	specific_abomination = cursor.fetchall()
	if not specific_abomination:
		conn.commit()
		cursor.close()
		conn.close()
		return False
	# todo: test
	id_owner = specific_abomination[0][1]
	if user_id != id_owner:
		conn.commit()
		cursor.close()
		conn.close()
		return False

	conn.commit()
	cursor.close()
	conn.close()
	return specific_abomination


def my_abominations(user_id):
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute(f"SELECT * FROM abominations WHERE id_owner = {user_id}")
	user_abominations = cursor.fetchall()
	conn.commit()
	cursor.close()
	conn.close()
	return user_abominations


def create_abomination(id_owner, name, gender, is_private, head, eye, body, arm, leg):
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute(f"INSERT INTO abominations"
	               f"(id_owner, name, gender, is_private, head, eye, body, arm, leg) VALUES "
	               f"({id_owner}, {name}, {gender}, {is_private}, {head}, {eye}, {body}, {arm}, {leg});")
	cursor.execute(f"SELECT id FROM abominations WHERE id_owner = {id_owner} ORDER BY id DESC LIMIT 1;")
	new_abomination = cursor.fetchall()
	conn.commit()
	cursor.close()
	conn.close()
	return new_abomination[0][0]
