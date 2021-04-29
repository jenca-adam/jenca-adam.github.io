$('#hannhover-result').hide();
$('#hannhover-container .hannhover-link').mouseenter(function (e){$('#hannhover-result').load($(e.target).attr('hh-location'));$('#hannhover-result').show(500)});
$('#hannhover-container .hannhover-link').mouseleave((function (e){$('#hanhover-result').hide(500)}));

		
