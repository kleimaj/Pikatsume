console.log('i am the trash man');
let pikas = $('.trashchu');
const trash = `<i class="fas fa-trash-alt"></i>`
for (p of pikas) {
    console.log(p);
    p.addEventListener("mouseover",function(){
        // opaque pika image
        p.style.opacity=.4;
        // let el = document.createElement(trash);
        p.insertAdjacentHTML('afterbegin', '<i class="fas fa-trash-alt fa-7x" id="trash"></i>');
        // add trash can over image
    });
    p.addEventListener("mouseout", function() {
        p.style.opacity=1;
        $('#trash').remove()
    })
    // , function() {
    //     p.style.opacity=1
    // });
    // p.click(function(){
    //     // delete
    // });
}
