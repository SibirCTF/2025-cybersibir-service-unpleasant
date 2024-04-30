from flask import Flask, render_template, render_template_string, make_response, request, redirect

app = Flask(__name__, template_folder="templates")


# TODO: PostgreSQL DB
@app.route('/')
def get_index():
	return 'index'  # TODO: render_template


@app.route('/register')
def get_register():
	return 'register'  # TODO: render_template


@app.route('/register', methods=["POST"])
def register():
	username, password = request.form["username"], request.form["password"]
	return 'register_post'  # TODO: business logic


@app.route('/login')
def get_login():
	return 'login'  # TODO: render_template


@app.route('/login', methods=["POST"])
def login():
	username, password = request.form["username"], request.form["password"]
	return 'login_post'  # TODO: business logic


@app.route('/feed')
def get_feed():
	return 'feed'  # TODO: render_template


@app.route('/create_abomination')
def get_create_abomination():
	return 'create_abomination'  # TODO: render_template


@app.route('/create_abomination', methods=["POST"])
def create_abomination():
	return 'create_abomination_post'  # TODO: business logic


@app.route('/abomination/<int:id>')
def get_abomination(id):
	return f'abomination-{id}'  # TODO: render_template  # TODO: business logic


@app.route('/my_abominations/')
def get_my_abominations():
	return 'my_abominations'  # TODO: render_template  # TODO: business logic


if __name__ == '__main__':
	app.run()
