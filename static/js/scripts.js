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
$("#selectUsuario").on("change", function () {
  var selectedOption = $(this).children("option:selected");
  var optionId = selectedOption.attr("id");
  var optionValue = selectedOption.attr("class");
  $('#select-valor').val(optionValue);
  console.log(optionValue);
  $('#no_control').val(optionId);
  if ($(this).val() == "administrador") {
    $('.admin').addClass("active");
    $('.operador').removeClass("active");
    var valorBoton = $(this).val();
    $('#boton-valor').val(valorBoton);
  }
  if ($(this).val() == "operador") {
    $('.operador').addClass("active");
    $('.admin').removeClass("active");
    var valorBoton = $(this).val();
    $('#boton-valor').val(valorBoton);
  }
});
$("#selectPozo").on("change", function () {
  var selectedOption = $(this).children("option:selected");
  var estado = selectedOption.attr("id");
  var horarios = selectedOption.attr("class");
  $('#horario').text(horarios);
  $('#estado').val(estado);
  if (estado == "1") {
    $('#flexSwitchCheckDefault').prop('checked', true);
  } else {
    $('#flexSwitchCheckDefault').prop('checked', false);
  }
});
$('#flexSwitchCheckDefault').on('change', function () {
  if ($(this).is(':checked')) {
    $('#estado').val("1");
  } else {
    $('#estado').val("0");
  }
})