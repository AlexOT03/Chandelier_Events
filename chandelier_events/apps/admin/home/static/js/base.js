// Alert para eliminar
(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro de eliminar la cotizacion, no podra recuperarla?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });

})();

// Inicializar popovers
var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl);
});

// -- Add more form-set's to the template --
$(document).ready(function() {
    $('#add-form').click(function() {
      var formset = $('#images');  // El contenedor del formset
      var formCount = formset.children().length;  // Número actual de formularios
  
      // Clonar el último formulario y cambiar los índices de los campos
      var newForm = formset.children(':last').clone();
      newForm.find('input').each(function() {
        var newName = $(this).attr('name').replace('-' + (formCount - 1) + '-', '-' + formCount + '-');
        $(this).attr('name', newName);
        $(this).val('');  // Limpiar los valores de los campos clonados si es necesario
      });
  
      // Agregar el formulario clonado al final del formset
      formset.append(newForm);
  
      // Opcional: si utilizas algún plugin o librería para estilizar los formularios, puedes inicializarlo para el nuevo formulario aquí
  
      // Opcional: si necesitas realizar alguna acción adicional después de añadir el formulario, puedes hacerlo aquí
    });
  });

// -- Detect if a form field is not empty --
$(document).ready(function() {
  

});

// Select2 multy select
$(document).ready(function() {
  $('.selectmultiple').select2();
  
});