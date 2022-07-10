$(document).ready(function() {
	
    /* ===== Stickyfill ===== */
    /* Ref: https://github.com/wilddeer/stickyfill */
    // Add browser support to position: sticky
    var elements = $('.sticky');
    Stickyfill.add(elements);


    /* Activate scrollspy menu */
    $('body').scrollspy({target: '#doc-menu', offset: 100});
    
    /* Smooth scrolling */
	$('a.scrollto').on('click', function(e){
        //store hash
        var target = this.hash;    
        e.preventDefault();
		$('body').scrollTo(target, 800, {offset: 0, 'axis':'y'});
		
	});
     
    /* Bootstrap lightbox */
    /* Ref: http://ashleydw.github.io/lightbox/ */

    $(document).delegate('*[data-toggle="lightbox"]', 'click', function(e) {
        e.preventDefault();
        $(this).ekkoLightbox();
    });    


});

$(".readmore-link").click( function(e) {
    // record if our text is expanded
    var isExpanded =  $(e.target).hasClass("expand");
    
    //close all open paragraphs
    $(".readmore.expand").removeClass("expand");
    $(".readmore-link.expand").removeClass("expand");
    
    // if target wasn't expand, then expand it
    if (!isExpanded){
      $( e.target ).parent( ".readmore" ).addClass( "expand" );
      $(e.target).addClass("expand");  
    } 
  });

// Pop images - Medium
$(function() {
    $('.pop').on('click', function() {
      $('.imagepreview').attr('src', $(this).find('img').attr('src'));
      $('#imagemodal').modal('show');   
    });		
  });
// Pop images - Large
$(function() {
  $('.pop-large').on('click', function() {
    $('.imagepreview-large').attr('src', $(this).find('img').attr('src'));
    $('#imagemodal-large').modal('show');   
  });		
});

let navigation = window.location.href
if (navigation.includes("start.html")) {
    const metaImg = document.getElementById('img-metadata');
    if (screen.width < 800) {
        metaImg.src = 'assets/images/guide/metadata_mobile.png'
    } else {
        metaImg.src = 'assets/images/guide/metadata.png'
    }
}
