from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
import json
import sqlite3


database = 'library.db'
conn = sqlite3.connect(database)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS books  (title VARCHAR NOT NULL, author VARCHAR NOT NULL, published INT)')
cursor.execute('CREATE TABLE IF NOT EXISTS movies (title VARCHAR NOT NULL, director VARCHAR NOT NULL, released INT)')
conn.commit()
conn.close()



app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z/$nxechd5/'

# need help understanding this function
def make_dict(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d



@app.route('/api/v1/resources/books/all')
def all_books():
	conn = sqlite3.connect(database)
	conn.row_factory = make_dict
	cursor = conn.cursor()
	all_books = cursor.execute('SELECT *, rowid FROM books').fetchall()
	return jsonify(all_books)

@app.route('/v1/resources/books/all')
def view_all_books():
	conn = sqlite3.connect(database)
	conn.row_factory = make_dict
	cursor = conn.cursor()
	all_books = cursor.execute('SELECT *, rowid FROM books').fetchall()
	return jsonify(all_books)


@app.route('/api/v1/resources/movies/all')
def all_movies():
	conn = sqlite3.connect(database)
	conn.row_factory = make_dict
	cursor = conn.cursor()
	all_movies = cursor.execute('SELECT *, rowid FROM movies').fetchall()
	return jsonify(all_movies)
	



@app.route('/api/v1/resources/books')
def get_book():
	query_parameters = request.args
	published = query_parameters.get('published')
	author = query_parameters.get('author')
	title = query_parameters.get('title')
	query = "SELECT * FROM books WHERE"
	to_filter = []
	if title:
		query += ' title=? AND'
		to_filter.append(title)
	if published:
		query += ' published=? AND'
		to_filter.append(published)
	if author:
		query += ' author=? AND'
		to_filter.append(author)
	if not (title or published or author):
		return page_not_found(404)

	query = query[:-4] + ';'
	conn = sqlite3.connect(database)
	conn.row_factory = make_dict
	cursor = conn.cursor()

	results = cursor.execute(query, to_filter).fetchall()

	return jsonify(results)





@app.route('/api/v1/resources/movies')
def get_movie():
	query_parameters = request.args
	released = query_parameters.get('released')
	director = query_parameters.get('director')
	title = query_parameters.get('title')
	query = "SELECT * FROM books WHERE"
	to_filter = []
	if title:
		query += ' title=? AND'
		to_filter.append(title)
	if released:
		query += ' released=? AND'
		to_filter.append(request)
	if director:
		query += ' director=? AND'
		to_filter.append(director)
	if not (title or director or released):
		return page_not_found(404)

	query = query[:-4] + ';'
	conn = sqlite3.connect(database)
	conn.row_factory = make_dict
	cursor = conn.cursor()

	results = cursor.execute(query, to_filter).fetchall()

	return jsonify(results)



@app.route('/v1/resources/books/newbook', methods = ['POST', 'GET'])
def add_book():
	title = request.form['bookTitle']
	author = request.form['bookAuthor']
	published = request.form['bookPublished']
	published = int(published)
	conn = sqlite3.connect(database)
	cur = conn.cursor()
	cur.execute("INSERT INTO books (title,author,published) VALUES (?,?,?)",(title, author, published) )
	conn.commit()
	flash('New book added to library!')
	return redirect(url_for('home'))
	conn.close()

@app.route('/v1/resources/movies/newmovie', methods = ['POST', 'GET'])
def add_movie():
	title = request.form['movieTitle']
	director = request.form['movieDirector']
	released = request.form['yearReleased']
	conn = sqlite3.connect(database)
	cur = conn.cursor()
	cur.execute("INSERT INTO movies (title,director,released) VALUES (?,?,?)",(title, director, released) )
	conn.commit()
	flash('New movie added to library!')
	return redirect(url_for('home'))
	conn.close()


@app.route('/home')
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/moviesPage')
def moviesPage():
	return render_template('movies.html')

@app.route('/booksPage')
def booksPage():
	return render_template('books.html')

@app.errorhandler(404)
def page_not_found(e):
	return "<h1>404</h1><p>The resource could not be found.</p>", 404



if __name__ == '__main__':
	app.run(debug=True)
	