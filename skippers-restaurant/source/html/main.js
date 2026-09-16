$(document).ready(function(){
	var domain = 'skippersgoodfood.com';
		$('#site_rotate').append('<div><img src="templates/'+domain+'/images/home-photo.jpg" alt="Yellow Skipper\'s shirt with the text Got Fish?" width="570" height="250" draggable="false"></div>');
//	$('#site_rotate').append('<div><img src="templates/'+domain+'/images/rotate1.jpg" width="570" height="250" draggable="false"></div>');
//	$('#site_rotate').append('<div><img src="templates/'+domain+'/images/rotate2.jpg" width="570" height="250" draggable="false"></div>');
//	$('#site_rotate').append('<div><img src="templates/'+domain+'/images/rotate3.jpg" width="570" height="250" draggable="false"></div>');
//	$('#site_rotate').cycle();
//	$("ul.sf-menu").superfish(); 
	
	$(".colorbox").colorbox();
	$('img[src*="show_image"]').colorbox({photo:true,href:function(){return $(this).attr('src')}});
    $('img[src*="show_image"]').css('cursor','pointer');
	
	//youtube function
	$('.mceItem').replaceWith(function (){ 
        return '<iframe title="YouTube video player" width="100%" height="390" src="http://www.youtube.com/embed/'+$(this).attr('alt')+'" frameborder="0" allowfullscreen></iframe>'; 
	});
});