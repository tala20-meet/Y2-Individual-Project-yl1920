from model import *
from sqlalchemy.pool import SingletonThreadPool

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///users.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def login_user(username,password):
	all_users = session.query(User).all()
	all_usernames = []
	for u in all_users:
		all_usernames.append(u.name)
	if username in all_usernames:
		user = session.query(User).filter_by(name=username)
		if user.Password == password:
			#do the login
			print("Logged in")
		else:
			print("Password incorrect")
	else:
		print("No user with this username")


def add_user(name,password,Email):
	User_object = User(
		name=name,
		password=password,
		Email=Email)
	session.add(User_object)
	session.commit()



#def update_user()

#def delete_user()
def delete_user(name):
   
   session.query(User).filter_by(
       name=name).delete()
   session.commit()



#def get_user()
#def get_all()
   
def add_movie(name,genre,release_date,img_link):
	Movie_object= Movie(
		name= name,
		Genre=genre,
		release_date=release_date,
		img_link=img_link)
	session.add(Movie_object)
	session.commit()

def delete_movie(name):
   session.query(Movie).filter_by(
       name=name).delete()
   session.commit()



#def edit_movie():

def get_movie(name):
	movies = session.query(Movie).filter_by(name=name).first()
	return Movie

def get_movie_by_date(release_date):
	movies = session.query(Movie).filter_by(release_date=release_date).first()
	return Movie

def get_movie_by_genre(movies,genre):
	final_list = movies.query(Movie).filter_by(Genre=genre).first()
	# movies = session.query(Movie).filter_by(genre=genre).first()
	return Movie


def get_all():
	movies = session.query(Movie).all()
	return movies



# add_movie("Glass","Drama", 2019 ,"static/img/glass.jpg") 
# add_movie("Harry Potter & the Philosopher's Stone" , "Fantasy" , 2001 ,"static/img/harry potter 1.jpg")
# add_movie("Harry Potter & the Chamber of Secrets" , "Fantasy" , 2002 ,"static/img/harry potter 2.png")
# add_movie("Harry Potter & the Prisoner of Azkaban" , "Fantasy" , 2004 , "static/img/harry potter 3.jpeg")
# add_movie("Harry Potter & the Goblet of Fire", "Fantasy" , 2005,"static/img/harry potter 4.jpg" )
# add_movie("The Avengers", "Sci-Fi", 2012 , "static/img/avengers 1.jpg")
# add_movie("Frozen 2","Animation",2019, "static/img/frozen2.jpg")
# add_movie("Frozen" , "Animation", 2013 ,"static/img/frozen1.jpeg")
# add_movie("Doctor sleep", "Horror", 2019 , "static/img/doctorsleep.jpg")
# add_movie("The Guilty", "Crime" , 2018, "static/img/theguilty.jpg")
# add_movie("Mission: Impossible - Fallout", "Action", 2018, "static/img/mission-impossible-fallout.jpg")
# add_movie("A Star IS Born", "Romance" , 2018, "static/img/a star is born.jpg")
# add_movie(" Blindspotting " , "Comedy", 2018, "static/img/blindspotting.jpg")
# add_movie("Avengers: Age of Ultron","Action", 2015,"static/img/avengers2.jpeg")
# add_movie(" Avengers: Infinity War ", "Action", 2018,"static/img/avengers3.jpg")
# add_movie("Deadpool 2" , "Action", 2018 ,"static/img/deadpool2.jpg")
# add_movie("Overlord" , "Action" , 2018 ,"static/img/overload.jpg")
# add_movie("Revenge", "Action" , 2018 ,"static/img/revenge.jpg")
# add_movie(" Mowgli: Legend of the Jungle" , "Adventure", 2018 ,"static/img/mowglie.jpg")
# add_movie("Monsters and Men " , "Crime" , 2018, "static/img/monsters&men.jpg")
# add_movie("Black Panther" , "Action" , 2018 ,"static/img/blackpanther.jpeg")
# add_movie(" Get Out" , "Horror" , 2017 ," static/img/Get_Out_poster.png")
# add_movie(" Jumanji: Welcome to the Jungle", "Action ", 2017 ,"static/img/jumanji.jpg")
