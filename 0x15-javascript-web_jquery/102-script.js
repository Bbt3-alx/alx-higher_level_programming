$(document).ready(function() {
	$('INPUT#btn_translate').click(function() {
		const langcode = $('INPUT#language_code').val();
		const url = `https://www.fourtonfish.com/hellosalut/hello/${langcode}`;
		$.ajax({
			url: url,
			method: 'GET',
			success: function(data) {
				$('#hello').html(data.hello);
			}
		});
	});
});

