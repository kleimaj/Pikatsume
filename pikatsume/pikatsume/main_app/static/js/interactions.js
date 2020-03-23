$(document).ready(function() {

    $(".navbar-burger").click(function() {
        $(".navbar-burger").toggleClass("is-active");
        $("#navMenu").toggleClass("is-active").toggleClass("slideInDown");
    });

    $(".pikaball").click(function(){
        $(".pikaball").toggleClass("shake");
    })
    
  });