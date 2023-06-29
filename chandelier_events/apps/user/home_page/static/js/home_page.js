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

//loader screen
window.onload = function() {
  var contenedor = document.getElementById('contenedor_carga');

  contenedor.style.visibility = 'hidden';
  contenedor.style.opacity = '0';
}