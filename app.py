from flask import Flask, jsonify, render_template, request, json, url_for
import database



app = Flask(__name__)




@app.route('/home')
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/movies')
def movies():
	return render_template('movies.html')

@app.route('/books')
def books():
	return render_template('books.html')

@app.route('/Allbooks')
def allBooks():
	cursor = conn.execute


@app.route('/addBook', methods=['GET', 'POST'])
def addBook():
	title = request.args.get('title')
	author = request.args.get('author')
	year = request.args.get('year')

	newBook = database.mainBook(title, author, year)
	return newBook



if __name__ == '__main__':
	app.run(debug=True)
	