(function($) {
	"use strict"
	
	// Preloader
	$(window).on('load', function() {
		$("#preloader").delay(600).fadeOut();
	});

	// Mobile Toggle Btn
	$('.navbar-toggle').on('click',function(){
		$('#header').toggleClass('nav-collapse')
	});
	
})(jQuery);

function init() {
    let map = new.ymaps.Map('map-test', {
        center: [53.90513757067667,27.60035099999995],
        zoom: 16
    })
}

ymaps.ready(init);