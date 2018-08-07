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

		console.log(bookTitle);
		console.log(bookAuthor);
		console.log(bookYear);

		$.ajax({
			data: { title : bookTitle, author: bookAuthor, year: bookYear },
			type: 'POST',
			url: 'addBook',
			dataType: 'json',
			success: function(response){
				$('#book-added-response').show();


			},
			error: function(response) {
				console.log(response);
			}
		});
		
	});


});