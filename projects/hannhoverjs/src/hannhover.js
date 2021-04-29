function hideResult(){
	$('#hanhover-result').delay(10).hide()
}
	
$('#hannhover-result').hide();
$('#hannhover-container .hannhover-link').mouseenter(function (e){$('#hannhover-result').delay(100).load($(e.target).attr('hh-location'));$('#hannhover-result').show()});
$('#hannhover-container .hannhover-link').mouseleave((function (){$('#hanhover-result').hide()}));

		
