$(document).ready(function() {
	$.ajax({
		url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
		method: 'GET',
		success: function(data) {
			const movies = data.results;
			movies.forEach(function(movie) {
				$('UL#list_movie').append(`<li>${movie.title}</li>`);
			});
		});
	});
});

