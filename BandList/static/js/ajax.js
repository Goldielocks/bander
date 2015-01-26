$(document).ready(function() {

});

$('.add_band').click(function(){
var id;
id = $(this).attr("data-id");
 $.get('/BandList/add_band/', {caseId: id}, function(data){
           $('#case').html(data.value);
		   $('#case').attr('data-id', id);
       });
})

$('.remove_band').click(function(){
var id;
id = $(this).attr("data-id");
 $.get('/BandList/remove_band/', {mapId: id}, function(data){
           $('#map').html(data.value);
       });
})