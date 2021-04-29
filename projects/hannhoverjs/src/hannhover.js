$('#hannhover-result').hide();
$('#hannhover-container .hannhover-link').mouseenter(function (e){$('#hannhover-result').load($(e.target).attr('hh-location'))});
$('#hannhover-container .hannhover-link').mouseleave((function (e){$('#hanhover-result').hide(500)}));

		
