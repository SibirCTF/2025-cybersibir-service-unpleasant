from flask import Flask, render_template, render_template_string, make_response, request, redirect
import psycopg2

app = Flask(__name__, template_folder="templates")


# TODO: session token/login

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


@app.route('/register', methods=["POST"])  # TODO: session token/login
def register():  # TODO: business logic
	username, password = request.form["username"], request.form["password"]
	return 'register_post / redirect '


@app.route('/login')
def get_login():
	return render_template("login.html")


@app.route('/login', methods=["POST"])  # TODO: session token/login
def login():  # TODO: business logic
	username, password = request.form["username"], request.form["password"]

	return 'login_post'


@app.route('/feed')
def get_feed():  # TODO: business logic
	return render_template("feed.html")


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
