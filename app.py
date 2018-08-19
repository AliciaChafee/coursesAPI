from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps




db_connect = create_engine('sqlite:///library.db')
app = Flask(__name__)
api = Api(app)



class AllBooks(Resource):
	def get(self):
		conn = db_connect.connect()
		query = conn.execute("select * from books")
		return {'Books': [i[0] for i in query.cursor.fetchall()]}

	

class AllMovies(Resource):
	def get(self):
		conn = db_connect.connect()
		query = conn.execute("select * from movies")
		return {'Movies': [i[0] for i in query.cursor.fetchall()]}

class Book_Title(Resource):
	def get(self, book_title):
		conn = db_connect.connect()
		query = conn.execute("select * from books where Book_Title ='" + book_title + "'")
		result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
		return jsonify(result)

class Movie_Title(Resource):
	def get(self, movie_title):
		conn = db_connect.connect()
		query = conn.execute("select * from movies where Movie_Title ='" + movie_title + "'")
		result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
		return jsonify(result)


api.add_resource(AllBooks, '/allBooks') # Route_1
api.add_resource(AllMovies, '/allMovies') # Route_2
api.add_resource(Book_Title, '/book/<book_title>') # Route_3
api.add_resource(Movie_Title, '/movie/<movie_title>') # Route_3



# Routes ***************

@app.route('/home')
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/moviesPage')
def moviesPage():
	return render_template('movies.html')

@app.route('/booksPage')
def booksPageboo():
	return render_template('books.html')



if __name__ == '__main__':
	app.run(debug=True)
	