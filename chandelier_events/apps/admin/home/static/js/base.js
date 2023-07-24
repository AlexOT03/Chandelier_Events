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

// -- Inicializa los tooltips --
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    })

// -- Detect if a image field is not empty --
$(document).ready(function() {
  var fileInputs = document.querySelectorAll('input[id^="id_form-"][id$="-image"]');

  function validateFiles() {
    fileInputs.forEach(function(fileInput) {
      var file = fileInput.files[0];
  
      if (file) {
        // Un archivo ha sido seleccionado
        fileInput.classList.remove('is-invalid');
        fileInput.classList.add('is-valid');
      } else {
        // No se ha seleccionado ningún archivo
        fileInput.classList.remove('is-valid');
        fileInput.classList.add('is-invalid');
      }
    });
  }
  
  validateFiles();
  
  fileInputs.forEach(function(fileInput) {
    fileInput.addEventListener('change', validateFiles);
  });
});

// -- Select2 multy select --
$(document).ready(function() {
  $('.selectmultiple').select2();
  
});

// -- Buscador de datos --
document.addEventListener("keyup", e => {
  if (e.target.id === "buscador") {
    const term = e.target.value.toLowerCase();
    let resultadosEncontrados = false;

    document.querySelectorAll(".objetos").forEach(elemento => {
      if (elemento.textContent.toLowerCase().includes(term)) {
        elemento.classList.remove("filtro");
        resultadosEncontrados = true;
      } else {
        elemento.classList.add("filtro");
      }
    });

    const tabla = document.querySelector("table");
    const filaResultados = document.querySelector("#fila-resultados");

    if (resultadosEncontrados) {
      // Eliminar la fila de resultados si existía
      if (filaResultados) {
        tabla.removeChild(filaResultados);
      }
    } else {
      // Crear o actualizar la fila de resultados
      if (filaResultados) {
        filaResultados.querySelector("td").textContent = "No se encontraron resultados";
      } else {
        const fila = document.createElement("tr");
        fila.id = "fila-resultados";
        const celda = document.createElement("td");
        celda.textContent = "No se encontraron resultados";
        celda.classList.add("text-center");
        celda.setAttribute("colspan", "7"); // Añadir el atributo colspan
        fila.appendChild(celda);
        tabla.appendChild(fila);
      }
    }
  }
});

// -- Pagination of tables --
$(document).ready(function() {
  var elementsPerPage = parseInt($(".datatable-selector").val());

  // Función para realizar las operaciones dependientes de 'elementsPerPage'
  function performOperations() {
      // Ocultar todas las filas
      $("#listaObjetos tr.objetos").hide();

      // Mostrar las primeras 'elementsPerPage' filas
      $("#listaObjetos tr.objetos").slice(0, elementsPerPage).show();

      // Calcular la cantidad total de páginas
      var totalPages = Math.ceil($("#listaObjetos tr.objetos").length / elementsPerPage);

      // Generar los botones de paginación dinámicamente
      var pagination = '';
      // pagination += '<li class="page-item"><a class="page-link" href="#" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>';
      for (var i = 1; i <= totalPages; i++) {
          pagination += '<li class="page-item"><a class="page-link" href="#" data-page="' + i + '">' + i + '</a></li>';
      }
      // pagination += '<li class="page-item"><a class="page-link" href="#" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>';
      $("#paginationButtons").html(pagination);

      // Manejar el evento de clic en los botones de paginación
      $(".page-link").click(function() {
          var page = $(this).data('page');

          if (page === undefined) {
              // Si el atributo 'data-page' no está definido, significa que se hizo clic en "Previous" o "Next"
              var currentPage = parseInt($(".pagination-button.active").text());
              if ($(this).attr('aria-label') === 'Previous') {
                  page = parseInt(currentPage) - 1;
              } else if ($(this).attr('aria-label') === 'Next') {
                  page = parseInt(currentPage) + 1;
              }
          }

          if (page >= 1 && page <= totalPages) {
              // Cambiar de página solo si el número de página es válido
              changePage(page);
          }
      });

      // Mostrar la página activa actualmente
      $(".pagination-button").first().addClass("active");

      // Mostrar el rango de filas correspondiente a la página activa
      var startIndex = 0;
      var endIndex = elementsPerPage;
      $("#listaObjetos tr.objetos").hide().slice(startIndex, endIndex).show();

      // Función para manejar el cambio de página
      function changePage(page) {
          // Calcular el rango de filas a mostrar
          startIndex = (page - 1) * elementsPerPage;
          endIndex = startIndex + elementsPerPage;

          // Ocultar todas las filas y mostrar el rango seleccionado
          $("#listaObjetos tr.objetos").hide().slice(startIndex, endIndex).show();

          // Actualizar la clase 'active' en los botones de paginación
          $(".pagination-button").removeClass("active");
          $(".pagination-button").eq(page - 1).addClass("active");
      }
  }

  // Llamar a la función 'performOperations' inicialmente
  performOperations();

  // Manejar el evento de cambio en el select
  $(".datatable-selector").change(function() {
      elementsPerPage = parseInt($(this).val());

      // Volver a llamar a la función 'performOperations' cuando cambie 'elementsPerPage'
      performOperations();
  });
});

$(document).ready(function() {
  // Agregar un evento de escucha al cambio en el primer select
  $('#id_form-0-size').change(function() {
      // Obtener el valor seleccionado
      var selectedValue = $(this).val();

      // Verificar si el valor seleccionado es "0" (Unico)
      if (selectedValue === '0') {
          // Si es "Unico", deshabilitar los siguientes dos formularios
          $('#id_form-1-size, #id_form-2-size').prop('disabled', true);
          $('#id_form-1-price, #id_form-2-price').prop('disabled', true);
          $('#id_form-1-duration, #id_form-2-duration').prop('disabled', true);
      } else {
          // Si no es "Unico", habilitar los siguientes dos formularios
          $('#id_form-1-size, #id_form-2-size').prop('disabled', false);
          $('#id_form-1-price, #id_form-2-price').prop('disabled', false);
          $('#id_form-1-duration, #id_form-2-duration').prop('disabled', false);
      }
  });
});

// -- clonar form sets -- 
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