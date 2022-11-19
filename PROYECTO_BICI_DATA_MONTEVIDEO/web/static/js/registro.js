//01_validar_fichero_de_registro [X]
function validarRegistro(form) {
	var retorno = true;

	if(form["usu_fecha"].value.trim() == "") {
		alert("La fecha de usuario es requerida")
		form["usu_fecha"].focus()
		retorno = false;
	}
	else if(form["usu_correo"].value.trim() == "") {
		alert("El correo es requerido")
		form["usu_correo"].focus()
		retorno = false;
	}
	else if(form["usu_nombre"].value.trim() == "") {
		alert("El nombre es requerido")
		form["usu_nombre"].focus()
		retorno = false;
	}else if(form["usu_contra"].value.trim() == "") {
		alert("La contraseña es requerida")
		form["usu_contra"].focus()
		retorno = false;
	}
	return(retorno);
}

//02_logica_para_cargar_automaticamente_la_fecha_al_registrarse:
function fechaActual() {
  var myDate = document.getElementById('usu_fecha');
  var today = new Date();
  myDate.value = today.toISOString().substr(0, 10);
  console.log(myDate);
}
fechaActual();
