// Get the button
var backToTopButton = document.getElementById("back-to-top");
      
// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    backToTopButton.style.display = "block";
  } else {
    backToTopButton.style.display = "none";
  }
};

// When the user clicks on the button, scroll to the top of the document
backToTopButton.onclick = function() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
};

// -- Select2 multy select --
$(document).ready(function() {
  $('#id_service_detail').select2();
});

// -- Código JavaScript para activar el modal al cargar la página --
// document.addEventListener("DOMContentLoaded", function() {
//   $('#myModal').modal('show');
// });
// document.addEventListener("DOMContentLoaded", function() {
//   var show_modal = document.body.getAttribute('data-show-modal');

//   if (show_modal === 'true') {
//       $('#myModal').modal('show');
//   }
// });