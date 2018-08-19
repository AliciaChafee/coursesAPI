import sqlite3
import json

def create_connection(db_file):
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error:
		print(Error)
	return None

def create_table(conn, create_table_sql):
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
	except Error:
		print(Error)

def addBook(conn, log):
	sql = ''' INSERT INTO BOOKS(TITLE, AUTHOR, PUBLISHED) VALUES(?,?,?)'''
	cur = conn.cursor()
	cur.execute(sql, log)
	conn.commit()

def addMovie(conn, log):
	sql = ''' INSERT INTO MOVIES(TITLE, DIRECTOR, RELEASED) VALUES(?,?,?)'''
	cur = conn.cursor()
	cur.execute(sql, log)
	conn.commit()

def allBooks():
	database = 'library.db'
	conn = create_connection(database)
	cur = conn.cursor()
	if conn is not None:
		cur.execute('SELECT Title, Author, Published FROM BOOKS')
		library = cur.fetchall()
		library = json.dumps(library)
	return library




def allMovies():
	database = 'library.sql'
	conn = create_connection(database)
	cur = conn.cursor()
	if conn is not None:
		cur.execute('SELECT Title, Director, Released FROM MOVIES')
		library = cur.fetchall()
		library = json.dumps(library)
	return library


def mainBook(title, author, published):
	database = 'library.sql'
	sql_create_book_table = '''CREATE TABLE IF NOT EXISTS BOOKS (
								ID PRIMARY KEY,
								TITLE TEXT NOT NULL UNIQUE,
								AUTHOR TEXT NOT NULL,
								PUBLISHED INT NOT NULL);'''
	
	conn = create_connection(database)
	if conn is not None:
		create_table(conn, sql_create_book_table)
	else:
		print("Error! Cannot create the database connection.")
	with conn:
		log = (title, author, published)
		addBook(conn, log)
	conn.close()
	return "book added"


def mainMovie(title, director, released):
	database = 'library.sql'
	sql_create_movie_table = '''CREATE TABLE IF NOT EXISTS MOVIES (
								ID PRIMARY KEY,
								TITLE TEXT NOT NULL UNIQUE,
								DIRECTOR TEXT NOT NULL,
								RELEASED INT NOT NULL);'''
	
	conn = create_connection(database)
	if conn is not None:
		create_table(conn, sql_create_movie_table)
	else:
		print("Error! Cannot create the database connection.")
	with conn:
		log = (title, director, released)
		addMovie(conn, log)
	conn.close()
	return "movie added"

#mainMovie('jaws', 'steven spielberg', '1975')
