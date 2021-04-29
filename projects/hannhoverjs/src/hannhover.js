function hideResult(){
	document.getElementById('hannhover-result').style.display='none';
}
	
$('#hannhover-result').hide();
$('#hannhover-container .hannhover-link').mouseenter(function (e){$('#hannhover-result').delay(100).load($(e.target).attr('hh-location'));$('#hannhover-result').show()});
$('#hannhover-container .hannhover-link').mouseleave((function (){hideResult()}));

		
