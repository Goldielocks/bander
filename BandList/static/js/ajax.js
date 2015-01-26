$(document).ready(function() {

});

$('.add').click(function(){
	var id = $(this).attr("data-id");
	$.get('/BandList/add/', {id:id, dataType:"band"}, function(data){
		var removedBand = $('#add' + id).remove().html();
		$('#current').append(removedBand);
	})
})

$('.remove').click(function(){
	var id = $(this).attr("data-id");
	$.get('/BandList/remove/', {id:id, dataType:"band"}, function(data){
		var removedBand = $('#remove' + id).remove().html();
		$('#unfollowed').append(removedBand);
	})
})
