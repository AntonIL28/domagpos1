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
function ajax() {
    const http = new XMLHttpRequest();
    const url = "http://127.0.0.1:8000/ajax-view/";

    http.onreadystatechange = function (){
        if(this.readyState == 4 && this.status == 200){
            console.log(this.responseText);
            document.getElementById("response").innerHTML =this.responseText;
        }
    }

    http.open("GET", url);
    http.send();
    }

document.getElementById("boton").addEventListener("click", function(){
    ajax();
});


/*Barra de busqueda dinamica
const onSearch = () =>{
    const input =document.querySelector("#search");
    const filter =input.ariaValueMax.toUpperCase();
    const list = document.querySelectorAll("#dynamic-table td")
    list.forEach((el)=>{
        const text =el.textContent.toUpperCase();

        el.style.display =text.includes(filter) ? "": "none";
    });
};*/ //Codigo de prueba (No funciono)

