console.log('i am the trash man');
let pikas = $('.delete_trash');
for (p of pikas) {
    p.click(function() {
        console.log("Here");
    }
}
