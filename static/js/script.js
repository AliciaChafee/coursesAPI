$(document).ready(function() {

// Home Page ******************************

	$('#newBookForm').hide();
	$('#newMovieForm').hide();


	$('#addMovie').on('click', function() {
		$('#newBookForm').hide();
		$('#flash-messages').hide();
		$('#newMovieForm').show();
	});

	$('#addBook').on('click', function() {
		$('#newMovieForm').hide();
		$('#flash-messages').hide();
		$('#newBookForm').show();
	});






// Books Page *************************


	$("#bookTableDiv").hide();
	$('#bookSearchDiv').hide();
	$('#no-book-found').hide();

	// View all books in library database

	$("#viewBooks").on('click', function() {
		$('#bookSearchDiv').hide();
		$("#books-body").empty();
		$("#bookTableDiv").toggle();

		$.ajax({
			type: 'GET',
			url: 'api/v1/resources/books/all',
			dataType: 'json',
			success: function(response){
				td = "<td>";
				etd = "</td>";
				tr = "<tr>";
				etr = "</tr>";

				for (var i = 0; i < response.length; i++){
					rows = tr;
					rows += td + response[i].rowid + etd;
					rows += td + response[i].title + etd;
					rows += td + response[i].author + etd;
					rows += td + response[i].published + etd;
					rows += etr;
					
					$("#books-body").append(rows);
				}
			}
		});
	});

	// Search for book title

	$(".search-books").on('click', function() {
		$("#bookTableDiv").hide();
		$('#book-search-body').empty();

		var titleSearch = $('#titleSearch').val().toUpperCase();

		
		$.ajax({
			type: 'GET',
			data: { title : titleSearch },
			url: 'api/v1/resources/books',
			dataType: 'json',
			success: function(response){
				if(response.length > 0) {
					td = "<td>";
					etd = "</td>";
					tr = "<tr>";
					etr = "</tr>";

					for (var i = 0; i < response.length; i++){
						rows = tr;
						rows += td + response[i].title + etd;
						rows += td + response[i].author + etd;
						rows += td + response[i].published + etd;
						rows += etr;
						
						$("#book-search-body").append(rows);
						$('#bookSearchDiv').show();
						$('#no-book-found').hide();
					}
				} else {
					$('#no-book-found').show();
					$('#bookSearchDiv').hide();
				}

			}
		});
	});


// Movies Page ***************


	$("#moviesTableDiv").hide();
	$('#movieSearchDiv').hide();
	$('#no-movie-found').hide();

	// View all movies in library database

	$("#viewMovies").on('click', function() {
		$('#movieSearchDiv').hide();
		$("#movies-body").empty();
		$("#moviesTableDiv").toggle();

		$.ajax({
			type: 'GET',
			url: 'api/v1/resources/movies/all',
			dataType: 'json',
			success: function(response){
				td = "<td>";
				etd = "</td>";
				tr = "<tr>";
				etr = "</tr>";

				for (var i = 0; i < response.length; i++){
					rows = tr;
					rows += td + response[i].rowid + etd;
					rows += td + response[i].title + etd;
					rows += td + response[i].director + etd;
					rows += td + response[i].released + etd;
					rows += etr;
					
					$("#movies-body").append(rows);
				}
			}
		});
	});

	// Search for movie title

	$(".search-movies").on('click', function() {
		$("#moviesTableDiv").hide();
		$('#movie-search-body').empty();

		var movieTitleSearch = $('#movieTitleSearch').val().toUpperCase();

		
		$.ajax({
			type: 'GET',
			data: { title : movieTitleSearch },
			url: 'api/v1/resources/movies',
			dataType: 'json',
			success: function(response){
				if(response.length > 0) {
					td = "<td>";
					etd = "</td>";
					tr = "<tr>";
					etr = "</tr>";

					for (var i = 0; i < response.length; i++){
						rows = tr;
						rows += td + response[i].title + etd;
						rows += td + response[i].director + etd;
						rows += td + response[i].released + etd;
						rows += etr;
						console.log(rows);
						
						$("#movie-search-body").append(rows);
						$('#movieSearchDiv').show();
						$('#no-movie-found').hide();
					}
				} else {
					$('#no-movie-found').show();
					$('#movieSearchDiv').hide();
				}

			}
		});
	});



});