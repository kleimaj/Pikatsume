/* ======= ======= ======= ======= ======= */
/* POPOP.JS - FUNCTIONALITY FOR YOUR MODAL */
/* ======= ======= ======= ======= ======= */

///* - DOCUMENT ELEMENTS - *///
//* - Main Modal - *//
const modalContent = document.querySelector('.popop-content')
//* - Button Calls - *//
const btn = document.querySelectorAll('.button');
const openBtn = document.querySelectorAll('.popop-open-btn');
const closeBtn = document.querySelectorAll('.popop-close-btn');
let pikaIndex = '';

/* ======= ======= ======= ======= ======= */

let openModalArr = [];
///* - FUNCTIONS - *///

//* - VISIBILITY - *//
//* - Open Modal - *//
function openModal(modalId){
    const modal = document.getElementById(`${modalId}`);
    modal.classList.add('popop-show');
    openModalArr.push(modal);
};
function closeModal (){
    if(!openModalArr.length){
        return;
    }
    const modal = openModalArr[openModalArr.length-1];
    modal.classList.remove('popop-show');
    openModalArr.pop();
}
//* - EVENT LISTENERS - *//
//* - Open Modal - *//
function openModalEvent(){
  openBtn.forEach( trigger => { 
    trigger.addEventListener('click', function (e) {
        const targetModal = e.target;
        const modalId = targetModal.getAttribute('data-modal-id')
        pikaIndex = targetModal.getAttribute('index')
        openModal(modalId);
    });
  });
};
//* - Close Modal - *//
function closeModalEvent(){
  closeBtn.forEach( trigger => {
    trigger.addEventListener('click', function (e) {
        if (event.target.id == 'trash-this-chu') {
          // Get pika index
          // pikaIndex
          // remove from front-end
          let trashchu = document.querySelectorAll('.trashchu')
          for (chu of trashchu) {
            if (chu.getAttribute('index') == pikaIndex){
              console.log("HERE")
              chu.style.display="none";
              // $.ajax(
              //   {
              //       type:"POST",
              //       url: "/removepika/",
              //       data:{
              //                pika_index: pikaIndex,
              //               //  csrfmiddlewaretoken: '{{ csrf_token }}'
              //       },
              //       success: function( data ) 
              //       {
              //           // $( '#like'+ catid ).remove();
              //           // $( '#message' ).text(data);
              //           console.log("Success");
              //       }
              //    });
            }
          }
          // remove from back-end
        }
        e.stopImmediatePropagation();
        closeModal();
    });
  });
};

//** - INIT POPOP.JS! - **//
openModalEvent();
closeModalEvent();