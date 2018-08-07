from flask import Flask, render_template, jsonify, json, request, url_for
from flask_restful import Api, Resource, reqparse
import database



app = Flask(__name__)
api = Api(app)


class Books(Resource):
	def get(self, name):
		for book in books:
			if(name == book['title']):
				return book, 200
		return "Book {} not found".format(name), 404

	def post(self, name):
		parser = reqparse.RequestParser()
		parser.add_argument("author")
		parser.add_argument("published")
		args = parser.parse_args()
		newBook = database.mainBook(name, args['author'], args['published'])
		return newBook

class Movies(Resource):
	def get(self, name):
		for movie in movies:
			if(name == movie['title']):
				return movie, 200
		return "Movie {} not found".format(name), 404

	def post(self, name):
		parser = reqparse.RequestParser()
		parser.add_argument("director")
		parser.add_argument("released")
		args = parser.parse_args()
		newMovie = database.mainMovie(name, args['director'], args['released'])
		return json.dumps(newMovie)


class AllMovies(Resource):
	def get(self):
		movies = database.allMovies();
		return movies, 200

class AllBooks(Resource):
	def get(self):
		books = database.allBooks();
		return books, 200


api.add_resource(Books, "/book/<string:name>")
api.add_resource(Movies, "/movie/<string:name>")
api.add_resource(AllBooks, "/books")
api.add_resource(AllMovies, "/movies")


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
	