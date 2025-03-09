from flask import Flask, render_template, render_template_string, make_response, request, redirect, flash
import psycopg2
import db
import os
import jwt
from config import Config
# todo: ssti
app = Flask(__name__, template_folder="templates")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 28800
with open('app/static/key.txt') as keyfile:
	jwt_key = keyfile.read().replace('\n', '')


def generate_jwt(user_id):
	return jwt.encode({"user_id": user_id}, jwt_key, algorithm="HS256")


def get_db_connection():
	conn = psycopg2.connect(host=Config.DB_HOST,
	                        port=5432,
	                        database='unpleasant_db',
	                        user='postgres',
	                        password='postgres')
	return conn


@app.route('/')
def get_index():
	return render_template("index.html"), 200


@app.route('/register')
def get_register():
	return render_template("register.html"), 200


@app.route('/register', methods=["POST"])
def register():
	username, password = request.form["username"], request.form["password"]
	id = db.register_user(username, password)
	if id is False:
		error = f'Error: bad login'
		return render_template("register.html", error=error), 400
	resp = make_response(redirect("login"))
	return resp


@app.route('/login')
def get_login():
	return render_template("login.html"), 200


@app.route('/login', methods=["POST"])
def login():
	username, password = request.form["username"], request.form["password"]
	user_id = db.login_user(username, password)
	if user_id is False:
		error = f'Error: invalid credentials'
		return render_template("login.html", error=error), 400
	resp = make_response(redirect("feed"))
	resp.set_cookie("diy_session", generate_jwt(user_id))
	return resp


@app.route('/feed')
def get_feed():
	id_owner = jwt.decode(request.cookies['diy_session'], jwt_key, algorithms='HS256')['user_id']
	feed = db.feed(id_owner)
	return render_template("feed.html", feed=feed), 200


@app.route('/create_abomination')
def get_create_abomination():
	heads, eyes, bodies, arms, legs = db.get_implants()
	return render_template("create_abomination.html", heads=heads, eyes=eyes, bodies=bodies, arms=arms, legs=legs), 200


@app.route('/create_abomination', methods=["POST"])
def create_abomination():
	user_id = jwt.decode(request.cookies['diy_session'], jwt_key, algorithms='HS256')['user_id']
	name, gender, is_private, head, eye, body, arm, leg = \
		str(request.form["name"]), str(request.form["gender"]), request.form.get('is_private'), request.form['head'], \
		request.form['eye'], request.form['body'], request.form['arm'], request.form['leg']
	if is_private:
		is_private = True
	else:
		is_private = False
	new_abomination = db.create_abomination(user_id, name, gender, is_private, head, eye, body, arm, leg)
	resp = make_response(redirect(f"/abomination/{new_abomination}"))
	return resp


@app.route('/abomination/<int:abom_id>')
def get_abomination(abom_id):
	user_id = jwt.decode(request.cookies['diy_session'], jwt_key, algorithms='HS256')['user_id']
	abomination = db.abomination(abom_id, user_id)
	if abomination is False:
		return 'anti-piracy ascii art', 404
	head = db.get_implant_name('head', abomination[5])
	eye = db.get_implant_name('eye', abomination[6])
	body = db.get_implant_name('body', abomination[7])
	arm = db.get_implant_name('arm', abomination[8])
	leg = db.get_implant_name('leg', abomination[9])
	detalized_abomination = (abomination[2], abomination[3], head, eye, body, arm, leg)
	pic = (abomination[5], abomination[6], abomination[7], abomination[8], abomination[9])
	return render_template("abomination.html", abom=detalized_abomination, pic=pic), 200


@app.route('/api/abomination/<int:abom_id>')
def api_get_abomination(abom_id):
	user_id = jwt.decode(request.cookies['diy_session'], jwt_key, algorithms='HS256')['user_id']
	abomination = db.abomination(abom_id, user_id)
	if abomination is False:
		return 'anti-piracy ascii art', 404  # TODO
	head = db.get_implant_name('head', abomination[5])
	eye = db.get_implant_name('eye', abomination[6])
	body = db.get_implant_name('body', abomination[7])
	arm = db.get_implant_name('arm', abomination[8])
	leg = db.get_implant_name('leg', abomination[9])
	detalized_abomination = (abomination[2], abomination[3], head, eye, body, arm, leg)
	return list(detalized_abomination), 200


@app.route('/my_abominations')
def get_my_abominations():
	user_id = jwt.decode(request.cookies['diy_session'], jwt_key, algorithms='HS256')['user_id']
	feed = db.my_abominations(user_id)
	return render_template("my_abominations.html", feed=feed), 200


@app.route('/api/my_abominations')
def api_my_abominations():
	user_id = jwt.decode(request.cookies['diy_session'], jwt_key, algorithms='HS256')['user_id']
	feed = db.my_abominations(user_id)
	return feed, 200


@app.route('/logout', methods=["GET"])
def logout():
	resp = make_response(redirect('/'))
	resp.delete_cookie("diy_session")
	return resp


if __name__ == '__main__':
	app.run(host="0.0.0.0")
