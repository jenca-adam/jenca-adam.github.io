$('#hannhover-result').hide();
$('#hannhover-container .hannhover-link').mouseenter(function (e){$('#hannhover-result').load($(e.target).attr('hh-location'));$('#hannhover-result').show()});
$('#hannhover-container .hannhover-link').mouseleave((function (e){console.log('test');$('#hanhover-result').hide()}));

		
