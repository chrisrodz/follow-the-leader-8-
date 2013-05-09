
var h = $(window).height();

$(document).ready(function() {

	// Handler for .ready() called.

	$("#core1").hide();

	$("#core2").hide();

	$("#core").hide();

});

var count = 0;

function hide_show(id){

	$(id).toggle('slow', function() {

		

	});

}


function ModifyPlaceHolder () {

    var input = document.getElementById ("id_username");

    input.placeholder = "Enter your username";

    var input1 = document.getElementById ("id_password");

    input1.placeholder = "Enter your password";

}

ModifyPlaceHolder ();