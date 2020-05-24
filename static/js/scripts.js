$(document).ready(function () {

    // Materialize Collapsible Initialization
    $(".collapsible").collapsible();

    // Materialize Sidenav Initialization
    $(".sidenav").sidenav();

    // Materialize Select Initialization
    $("select").formSelect();

    // Materialize Carousel Initialization
    $(".carousel.carousel-slider").carousel({
        fullWidth: true,
        indicators: true,
        dist: 0,
    });
    
    window.setInterval(function () {
        $(".carousel").carousel("next");
    }, 5500);

});
