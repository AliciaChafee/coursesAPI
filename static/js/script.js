$(document).ready(function() {


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

	$('#submitBook').on('click', function() {
		var bookTitle = $('#newBookTitle').val().toUpperCase();
		var bookAuthor = $('#author').val().toUpperCase();
		var bookYear = $('#yearPublished').val();

		$.ajax({
			data: { title : bookTitle, author: bookAuthor, year: bookYear },
			type: 'GET',
			url: 'addBook',
			dataType: 'json',
			success: function(response){
				console.log("Success adding book");
				$('#book-added-response').show();


			},
			error: function(error) {
				console.log("Error adding book: " + error);
			}
		});
		
	});


});