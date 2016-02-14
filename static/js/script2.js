$(function(){
	$('button').click(function(){
		$.ajax({
			url: '/x_decrease',
			data: $('form2').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
