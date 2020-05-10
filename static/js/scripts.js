$(document).ready(function () {
  $(".collapsible").collapsible();
  $(".sidenav").sidenav();
  $(".carousel.carousel-slider").carousel({
    fullWidth: true,
    indicators: true,
    dist: 0,
  });
  window.setInterval(function () {
    $(".carousel").carousel("next");
  }, 5500);
});
