from flask import Flask, request,render_template

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1> Hello World: %s</h1>' % request.method

@app.route('/profile/<username>',methods=['GET'])
def profile(username):
	return render_template("profile.html", name=username)





if __name__ == '__main__':
	app.run(debug=True)
