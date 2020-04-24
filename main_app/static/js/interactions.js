$(document).ready(function() {

    $(".navbar-burger").click(function() {
        $(".navbar-burger").toggleClass("is-active");
        $("#navMenu").toggleClass("is-active").toggleClass("slideInDown");
    });

    $(".pikaball").click(function(){
        $(".pikaball").toggleClass("shake");
    });
    
    $('#cat-card').mouseenter(function () {
        $('img', this).replaceWith('<img src="https://i.redd.it/3tb4vxbbfyh21.jpg" alt="Cat Frontend Engineer UX Designer" />');
    });
 
    $('#cat-card').mouseout(function () {
        $('img', this).replaceWith('<img src="https://i.ibb.co/z4gw8jd/surprisedpika.jpg" alt="A Pikachu" />');
    });

    $('#jacob-card').mouseenter(function () {
       $('img', this).replaceWith('<img src="../static/assets/images/jacob_profile.jpg" alt="Jacob Fullstac Dev" />');
     });

     $('#jacob-card').mouseout(function () {
       $('img', this).replaceWith('<img src="https://i.ibb.co/fCNpndG/bass-chu.png" alt="A Pikachu" />');
     });
    
    $('#johnson-card').mouseenter(function () {
        $('img', this).replaceWith('<img src="https://ca.slack-edge.com/T0351JZQ0-US6V78CTH-f153c9cab8be-512" alt="Cat Frontend Engineer UX Designer" />');
      });
 
    $('#johnson-card').mouseout(function () {
        $('img', this).replaceWith('<img id="cool-chu" src="https://i.ibb.co/XSBHnDF/cool-chu.png" alt="A Pikachu" />');
    });
  });