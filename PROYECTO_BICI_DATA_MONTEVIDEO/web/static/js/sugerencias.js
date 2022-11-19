//01_frase_dos [X]
function mostrarFraseDos() {
alert('“La fuerza de tus piernas es proporcional a la de tu corazón”');
}
//02_frase_uno [X]
function mostrarFraseUno (){
alert('"No hay distancia que no se pueda recorrer, ni meta que no se pueda alcanzar"');
}

//03_validar_fichero_de_sugerencia [X]
function validarSugerencia(form) {
	var retorno = true;

	if(form["sug_fecha"].value.trim() == "") {
		alert("La fecha es requerida")
		form["sug_fecha"].focus()
		retorno = false;
	}
	else if(form["sug_texto"].value.trim() == "") {
		alert("El texto es requerido")
		form["sug_texto"].focus()
		retorno = false;
	}
	return(retorno);
}


//05_logica_para_cargar_automaticamente_la_fecha_al_registrar_la_sugerencia:
function fechaActual() {
  var myDate = document.getElementById('sug_fecha');
  var today = new Date();
  myDate.value = today.toISOString().substr(0, 10);
  console.log(myDate);
}
fechaActual();

//05_Logica_de_la_tabla_para_la_barra_de_desplazamiento_virtical [] {No sé bien para qué sirve...}
/*
$(window).on("load resize ", function() {
  var scrollWidth = $('.tbl-content').width() - $('.tbl-content table').width();
  $('.tbl-header').css({'padding-right':scrollWidth});
}).resize();
*/


//06_logica_para el buscador de la tabla:
 (function(document) {
      'use strict';

      var LightTableFilter = (function(Arr) {

        var _input;

        function _onInputEvent(e) {
          _input = e.target;
          var tables = document.getElementsByClassName(_input.getAttribute('data-table'));
          Arr.forEach.call(tables, function(table) {
            Arr.forEach.call(table.tBodies, function(tbody) {
              Arr.forEach.call(tbody.rows, _filter);
            });
          });
        }

        function _filter(row) {
          var text = row.textContent.toLowerCase(), val = _input.value.toLowerCase();
          row.style.display = text.indexOf(val) === -1 ? 'none' : 'table-row';
        }

        return {
          init: function() {
            var inputs = document.getElementsByClassName('light-table-filter');
            Arr.forEach.call(inputs, function(input) {
              input.oninput = _onInputEvent;
            });
          }
        };
      })(Array.prototype);

      document.addEventListener('readystatechange', function() {
        if (document.readyState === 'complete') {
          LightTableFilter.init();
        }
      });

    })(document);

//07_boton toggle de la tabla:
var btnToggle4 = document.getElementById('btnToggle4');
var tabla= document.getElementById('tabla');

btnToggle4.addEventListener('click', () => {
tabla.classList.toggle('mostrar');
});
