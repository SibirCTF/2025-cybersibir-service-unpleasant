import psycopg2
from config import Config


def get_db_connection():
	conn = psycopg2.connect(host=Config.DB_HOST,  # unpleasant_db
	                        port=5432,
	                        database='unpleasant_db',
	                        user='postgres',
	                        password='postgres')
	return conn


def escape(parameter):
	return parameter.replace("'", "''").replace("\\", "\\\\").replace("\"", "\\\"").replace(";", "\\;").replace("--", "\\--").replace("#", "\\#").replace("%", "\\%").replace("_", "\\_")


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
	cursor.execute(f"SELECT id FROM users WHERE username='{escape(username)}' AND password='{password}'")
	user = cursor.fetchall()
	if not user:
		return False
	conn.commit()
	cursor.close()
	conn.close()
	return user[0][0]


def feed(user_id):
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
	id_owner = specific_abomination[0][1]
	is_private = specific_abomination[0][4]
	if is_private and (user_id != id_owner):
		conn.commit()
		cursor.close()
		conn.close()
		return False
	conn.commit()
	cursor.close()
	conn.close()
	return specific_abomination[0]


def my_abominations(user_id):
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute(f"SELECT * FROM abominations WHERE id_owner = {user_id}")
	user_abominations = cursor.fetchall()
	conn.commit()
	cursor.close()
	conn.close()
	return user_abominations


def get_implant_name(bodypart, id):
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute(f"SELECT name FROM implants where bodypart = '{bodypart}' and id = {id};")
	name = cursor.fetchall()
	conn.commit()
	cursor.close()
	conn.close()
	return name[0][0]


def get_implants():
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute(f"SELECT * FROM implants where bodypart = 'head';")
	head = cursor.fetchall()
	cursor.execute(f"SELECT * FROM implants where bodypart = 'eye';")
	eye = cursor.fetchall()
	cursor.execute(f"SELECT * FROM implants where bodypart = 'body';")
	body = cursor.fetchall()
	cursor.execute(f"SELECT * FROM implants where bodypart = 'arm';")
	arm = cursor.fetchall()
	cursor.execute(f"SELECT * FROM implants where bodypart = 'leg';")
	leg = cursor.fetchall()
	conn.commit()
	cursor.close()
	conn.close()
	return head, eye, body, arm, leg


def create_abomination(id_owner, name, gender, is_private, head, eye, body, arm, leg):
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute(f"INSERT INTO abominations"
	               f"(id_owner, name, gender, is_private, head, eye, body, arm, leg) VALUES "
	               f"({id_owner}, '{name}', '{gender}', {is_private}, {head}, {eye}, {body}, {arm}, {leg});")
	cursor.execute(f"SELECT id FROM abominations WHERE id_owner = {id_owner} ORDER BY id DESC LIMIT 1;")
	new_abomination = cursor.fetchall()
	conn.commit()
	cursor.close()
	conn.close()
	return new_abomination[0][0]
