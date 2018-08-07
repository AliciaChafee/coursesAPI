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
	sql = ''' INSERT INTO MOVIE(TITLE, DIRECTOR, RELEASED) VALUES(?,?,?)'''
	cur = conn.cursor()
	cur.execute(sql, log)
	conn.commit()

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


def main_movie(title, director, released):
	database = 'library.sql'
	sql_create_movie_table = '''CREATE TABLE IF NOT EXISTS BOOKS (
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

#def searchBooks
#def searchMovies
# def viewBooks
# def viewMovies
