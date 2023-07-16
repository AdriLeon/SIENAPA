$(".admin").on("click", function () {
  $('.admin').addClass("active");
  $('.operador').removeClass("active");
  var valorBoton = $(this).val();
  $('#boton-valor').val(valorBoton);
});
$(".operador").on("click", function () {
  $('.operador').addClass("active");
  $('.admin').removeClass("active");
  var valorBoton = $(this).val(); // Capturar el valor del botón
  $('#boton-valor').val(valorBoton); // Actualizar el campo oculto del formulario
});
$('.open-btn').click(function () {
    $('.sidebar').addClass('active');
  });
$('.close-btn').click(function () {
    $('.sidebar').removeClass('active');
  });