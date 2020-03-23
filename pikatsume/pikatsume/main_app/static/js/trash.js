console.log('i am the trash man');
let pikas = $('.pika_img');
const trash = `<i class="fas fa-trash-alt"></i>`
for (p of pikas) {
    console.log(p);
    p.addEventListener("mouseover",function(){
        // opaque pika image
        p.style.opacity=.4;
        // let el = document.createElement(trash);
        p.insertAdjacentHTML('afterend', '<i class="fas fa-trash-alt fa-9x" id="trash"></i>');
        // add trash can over image
    });
    p.addEventListener("mouseout", function() {
        p.style.opacity=1;
        p.nextSibling.remove()
    })
    // , function() {
    //     p.style.opacity=1
    // });
    // p.click(function(){
    //     // delete
    // });
}
