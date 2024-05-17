from flask import Flask, render_template, render_template_string, make_response, request, redirect
import psycopg2
import db
import os
import jwt

app = Flask(__name__, template_folder="templates")
jwt_key = os.urandom(64)



def generate_jwt(user_id):
	return jwt.encode({"user_id": user_id}, jwt_key, algorithm="HS256")


# TODO: copy to .env or .config file
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
	resp.set_cookie("session", generate_jwt(user_id).decode())
	return resp


@app.route('/feed')
def get_feed():  # TODO: business logic
	return db.feed()
	# return render_template("feed.html")


@app.route('/create_abomination')
def get_create_abomination():
	return render_template("create_abomination.html")


@app.route('/create_abomination', methods=["POST"])
def create_abomination():  # TODO: business logic
	return 'create_abomination_post / redirect abomination/{id}'


@app.route('/abomination/<int:id>')
def get_abomination(id):  # TODO: render_template  # TODO: business logic
	return f'abomination-{id}'


@app.route('/my_abominations/')
def get_my_abominations():  # TODO: business logic
	return render_template("my_abominations.html")


@app.route('/logout', methods=["GET"])  # TODO: session token/login
def logout():  # TODO: business logic
	return redirect("/")


if __name__ == '__main__':
	app.run(host="0.0.0.0")
