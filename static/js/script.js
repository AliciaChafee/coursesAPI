$(document).ready(function() {

// Home Page ******************************

	$('#newBookForm').hide();
	$('#newMovieForm').hide();
	$('#book-added-response').hide();
	$('#movie-added-response').hide();


	$('#addMovie').on('click', function() {
		$('#newBookForm').hide();
		$('#newMovieForm').show();
	});

	$('#addBook').on('click', function() {
		$('#newMovieForm').hide();
		$('#newBookForm').show();
	});


// Books Page *************************

	// Add new book to library database
	$("#bookTableDiv").hide();

	$('#submitBook').on('click', function() {
		var bookTitle = $('#newBookTitle').val().toUpperCase();
		var bookAuthor = $('#author').val().toUpperCase();
		var bookYear = $('#yearPublished').val();

		var url = "/book/" + bookTitle;

		$.ajax({
			data: { title : bookTitle, author: bookAuthor, published: bookYear },
			type: 'POST',
			url: url,
			dataType: 'json',
			success: function(response){
				console.log("response: " + response);
				console.log("Success adding book");
				//$('#book-added-response').show();


			},
			error: function(error) {
				console.log("Error adding book: " + error);
			}
		});
		
	});

	// View all books in library database

	$("#viewBooks").on('click', function() {

		$("#books-body").empty();
		$("#bookTableDiv").toggle();
		
			$.ajax({
				type: 'GET',
				url: 'books',
				dataType: 'json',
				success: function(response){
					console.log(response);
					for(var i = 0; i < response.data.length; i++) {
						console.log(response.data[i]);
					}
					$("#books-body").append(response);
				}
			});
	});


// Movies Page ***************

	// Add new movie to library database

	$('#submitMovie').on('click', function() {
		var movieTitle = $('#newMovieTitle').val().toUpperCase();
		var movieDirector = $('#director').val().toUpperCase();
		var movieYear = $('#yearReleased').val();

		console.log(movieTitle);
		console.log(movieDirector);
		console.log(movieYear);

		var url = "/movie/" + movieTitle;

		console.log(url);

		$.ajax({
			data: { title : movieTitle, director: movieDirector, released: movieYear },
			type: 'POST',
			url: url,
			dataType: 'json',
			success: function(response){
				console.log("response" + response);
				console.log("Success adding movie");
				$('#movie-added-response').show();


			},
			error: function(error) {
				console.log("Error adding movie: " + error);
			}
		});
		
	});

	// View all movies in library database

	$("#viewMovies").on('click', function() {
		$("#movies-body").empty();
		
			$.ajax({
				type: 'GET',
				url: 'movies',
				success: function(response){
					console.log(response);
					$("#movies-body").append(response);
				}
			});
	});


});