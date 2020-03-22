$(document).ready(function() {
    console.log('ready!')
    // Check for click events on the navbar burger icon
    $(".navbar-burger").click(function() {
        console.log('clicky')
        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $(".navbar-burger").toggleClass("is-active");
        $("#navMenu").toggleClass("is-active");
  
    });
  });