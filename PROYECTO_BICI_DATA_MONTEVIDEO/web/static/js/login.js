//01_validar_fichero_de_login [X]
function validarLogin(form) {
	var retorno = true;

	if(form["usu_nombre"].value.trim() == "") {
		alert("El nombre de usuario es requerido")
		form["usu_nombre"].focus()
		retorno = false;
	}
	else if(form["usu_contra"].value.trim() == "") {
		alert("La contraseña es requerida")
		form["usu_contra"].focus()
		retorno = false;
	}


	return(retorno);
}