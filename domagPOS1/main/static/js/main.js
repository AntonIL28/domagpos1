/*Pop up Clientes*/
function toggleDiv_clientes() {
  // Obtener el div por su ID
  var div = document.getElementById('control_clientes');
  // Verificar el estado actual del div
  if (div.style.display === 'none') {
      // Si está oculto, mostrarlo
      div.style.display = 'block';
  } else {
      // Si está visible, ocultarlo
      div.style.display = 'none';
  }
}

/*Funcion de prueba para recoger datos*/
function MostrarMensaje(){

	$.get('funciones.html',function(mensaje,estado){

		document.getElementById('resultado').innerHTML=mensaje;
	})
}