from flask import Flask, render_template, render_template_string, make_response, request, redirect
import psycopg2
import db, db_init
import os
import jwt

app = Flask(__name__, template_folder="templates")
jwt_key = os.urandom(64)  # datetime vuln? known seed


def generate_jwt(user_id):
	return jwt.encode({"user_id": user_id}, jwt_key, algorithm="HS256")


def get_db_connection():
	conn = psycopg2.connect(host='localhost',
	                        port=5432,
	                        database='flask_test',  # TODO: database name
	                        user='postgres',
	                        password='postgres')
	return conn


@app.route('/dbtest')  # TODO: Remove
def get_db():
	conn = get_db_connection()
	cur = conn.cursor()
	cur.execute("SELECT current_database()")
	version = cur.fetchall()
	conn.commit()
	cur.close()
	conn.close()
	return version


@app.route('/')
def get_index():
	return render_template("index.html")


@app.route('/register')
def get_register():
	return render_template("register.html")


@app.route('/register', methods=["POST"])
def register():
	username, password = request.form["username"], request.form["password"]
	id = db.register_user(username, password)
	if id is False:
		return render_template("register.html", show_error=True)
	resp = make_response(redirect("login.html"))
	return resp


@app.route('/login')
def get_login():
	return render_template("login.html")


@app.route('/login', methods=["POST"])
def login():
	username, password = request.form["username"], request.form["password"]
	user_id = db.login_user(username, password)
	if user_id is False:
		return render_template("login.html", show_error=True)
	resp = make_response(redirect("feed.html"))
	resp.set_cookie("diy_session", generate_jwt(user_id))
	return resp


@app.route('/feed')
def get_feed():  # TODO: render_template / jinja pattern?
	id_owner = jwt.decode(request.cookies['diy_session'], jwt_key, algorithms='HS256')['user_id']
	return db.feed(id_owner)
	# return render_template("feed.html")


@app.route('/create_abomination')
def get_create_abomination():
	return render_template("create_abomination.html")


@app.route('/create_abomination', methods=["POST"])
def create_abomination():
	user_id = jwt.decode(request.cookies['diy_session'], jwt_key, algorithms='HS256')['user_id']
	name, gender, is_private, head, eye, body, arm, leg = \
		request.form["name"], request.form["gender"], request.form['is_private'], request.form['head'], \
		request.form['eye'], request.form['body'], request.form['arm'], request.form['leg']
	new_abomination = db.create_abomination(user_id, name, gender, is_private, head, eye, body, arm, leg)
	resp = make_response(redirect(f"/abomination/{new_abomination}"))
	return resp


@app.route('/abomination/<int:abom_id>')
def get_abomination(abom_id):
	user_id = jwt.decode(request.cookies['diy_session'], jwt_key, algorithms='HS256')['user_id']
	abomination = db.abomination(abom_id, user_id)
	if abomination is False:
		return '404'  # todo: 404
	return abomination
	# return render_template("abomination.html")  # todo: картинки?, render_template


@app.route('/my_abominations')
def get_my_abominations():
	user_id = jwt.decode(request.cookies['diy_session'], jwt_key, algorithms='HS256')['user_id']
	return db.my_abominations(user_id)
	# return render_template("my_abominations.html")  # todo render


@app.route('/logout', methods=["GET"])
def logout():
	resp = make_response(redirect('/'))
	resp.delete_cookie("diy_session")
	return resp


if __name__ == '__main__':
	app.run(host="0.0.0.0")
