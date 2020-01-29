from database import *
from flask import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=['GET' , 'POST'])
def login():
	if request.method == 'GET':
		return render_template("login.html")
	else:
		username= request.form['uname']
		password= request.form['psw']

		add_user(username, password)
		return redirect(url_for('mainpage'))

		

@app.route("/signup" , methods=['GET' , 'POST'])
def signup():
	if request.method == 'GET':
		return render_template("signup.html")
	else:
		Email=request.form['email']
		username= request.form['uname']
		Password= request.form['psw']

		add_user(Email,username, Password)
		return redirect(url_for('mainpage'))
	

@app.route("/mainpage")
def mainpage():
	return render_template("mainpage.html")

@app.route("/pickmovie", methods=['GET' , 'POST'])
def pickmovie():
	if request.method == 'GET':
		return render_template("pickmovie.html")
	else:
		genre=request.form['genre']
		year= request.form['year']
		movies=[]
		all_movies=get_all()
		print("---")
		print(genre)
		print(year)
		for movie in all_movies:
			if movie.release_date == int(year) and movie.Genre==genre:
				print("found and added movie")
				movies.append(movie)
		return render_template("pickmovie.html", movies=movies)
	
if __name__ == '__main__':
    app.run(debug=True,port=3000)
