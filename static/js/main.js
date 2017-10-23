// Responsive Navigation
(function () {
	$('.hamburger-menu').on('click', function() {
		$('.bar').toggleClass('animate');
		$('.home-header__navigation').fadeToggle( "fast", "linear" );
		$('.inner-header__navigation').fadeToggle( "fast", "linear" );
	})
})();

$(".login__form-row input").focus(function(){
  $(this).parent().addClass("is-active is-completed");
});

$(".login__form-row input").focusout(function(){
  if($(this).val() === "")
    $(this).parent().removeClass("is-completed");
  $(this).parent().removeClass("is-active");
});