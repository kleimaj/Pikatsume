console.log('i am the trash man');
let pikas = $('.trashchu');
// const trash = `<i class="fas fa-trash-alt"></i>`
let currentCard = '';

for (p of pikas) {
    console.log(p);
    p.addEventListener("mouseover",function(event){
        // opaque pika image
        p.style.opacity=.4;
        currentcard = p
        // let el = document.createElement(trash);
        p.insertAdjacentHTML('afterend', '<i class="fas fa-trash-alt fa-7x" id="trash"></i>');
        let trash = document.querySelector("#trash");
    });
    p.addEventListener("mouseout", function() {
        p.style.opacity=1;
        $('#trash').remove();
    })
    // , function() {
    //     p.style.opacity=1
    // });
    // p.click(function(){
    //     // delete
    // });
}
