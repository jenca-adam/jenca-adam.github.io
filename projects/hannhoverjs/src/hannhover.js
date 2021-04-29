$('#hannhover-result').hide();
$('#hannhover-container .hannhover-link').mouseenter(function (e){$('#hannhover-result').load($(e.target).attr('hh-location'));$('#hannhover-result').show()});
$('#hannhover-container .hannhover-link').mouseleave((function (){$('#hanhover-result').hide()}));

		
