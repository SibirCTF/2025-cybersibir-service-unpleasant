from flask import Flask, render_template, render_template_string, make_response, request, redirect

app = Flask(__name__, template_folder="templates")


# TODO: PostgreSQL DB
@app.route('/')
def get_index():
	return render_template("index.html")


@app.route('/register')
def get_register():
	return render_template("register.html")


@app.route('/register', methods=["POST"])
def register():
	username, password = request.form["username"], request.form["password"]
	return 'register_post'  # TODO: business logic


@app.route('/login')
def get_login():
	return render_template("login.html")


@app.route('/login', methods=["POST"])
def login():
	username, password = request.form["username"], request.form["password"]
	return 'login_post'  # TODO: business logic


@app.route('/feed')
def get_feed():
	return render_template("feed.html")


@app.route('/create_abomination')
def get_create_abomination():
	return render_template("create_abomination.html")


@app.route('/create_abomination', methods=["POST"])
def create_abomination():
	return 'create_abomination_post'  # TODO: business logic


@app.route('/abomination/<int:id>')
def get_abomination(id):
	return f'abomination-{id}'  # TODO: render_template  # TODO: business logic


@app.route('/my_abominations')
def get_my_abominations():
	return render_template("my_abominations.html")  # TODO: business logic


@app.route('/logout', methods=["GET"])
def logout():
	return redirect("/")  # TODO: business logic


if __name__ == '__main__':
	app.run(host="0.0.0.0")
