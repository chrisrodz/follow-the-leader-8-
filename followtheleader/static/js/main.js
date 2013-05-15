
var h = $(window).height();

$(document).ready(function() {

	// Handler for .ready() called.

	$("#core1").hide();

	$("#core2").hide();

	$("#core").hide();
			$('label[for="id_f1"]').html("Nombre&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_f2"]').html("Seguro Social&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_f3"]').html("Transaccion&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_f5"]').html("Horas Periodo Pago&nbsp;&nbsp;");
			$('label[for="id_f6"]').html("Proposito&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_f7"]').html("Prep. Acad. Mas Alta");
			$('label[for="id_f8"]').html("Fecha de Efectividad&nbsp;");
			$('label[for="id_f9"]').html("Fecha de Terminacion");
			$('label[for="id_f10"]').html("Grupo de Trabajo/Codigo de Asignacion- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VIGENTES");
			$('label[for="id_f10_1"]').html("DESPUES DEL CAMBIO");
			$('label[for="id_f11"]').html("Facultad, Departamento/Decanato, Oficina- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VIGENTES");
			$('label[for="id_f11_1"]').html("DESPUES DEL CAMBIO");
			$('label[for="id_f12"]').html("Nombre de Plaza- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VIGENTES");
			$('label[for="id_f12_1"]').html("DESPUES DEL CAMBIO");
			$('label[for="id_f13"]').html("Cuenta(s) a afectarse- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VIGENTES");
			$('label[for="id_f13_1"]').html("DESPUES DEL CAMBIO");
			$('label[for="id_f14"]').html("Titulo/Rango-  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VIGENTES");
			$('label[for="id_f14_1"]').html("DESPUES DEL CAMBIO");
			$('label[for="id_f15"]').html("Tipo de Nombramiento- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VIGENTES");
			$('label[for="id_f15_1"]').html("DESPUES DEL CAMBIO");
			$('label[for="id_f16"]').html("Clases de Servicio- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VIGENTES");
			$('label[for="id_f16_1"]').html("DESPUES DEL CAMBIO");
			$('label[for="id_f17"]').html("Codigo de Pago y/o CAL ID- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VIGENTES");
			$('label[for="id_f17_1"]').html("DESPUES DEL CAMBIO");
			$('label[for="id_f18"]').html("Escala/Rate- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VIGENTES");
			$('label[for="id_f18_1"]').html("DESPUES DEL CAMBIO");
			$('label[for="id_f19"]').html("Sueldo Total Bimensual- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VIGENTES");
			$('label[for="id_f19_1"]').html("DESPUES DEL CAMBIO");


			$('label[for="id_f20"]').html("Sobresueldo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_f20_1"]').html("Prep. Acad. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_f20_2"]').html("Bonificacion");
			$('label[for="id_f20_3"]').html("Diferencial docente");
			$('label[for="id_f20_4"]').html("Aumentos concedidos");
			$('label[for="id_f20_5"]').html("Quinq. Ret. ");

			$('label[for="id_f21"]').html("Grupo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_f21_1"]').html("Codigo asig.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_f21_2"]').html("Status&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_f21_3"]').html("Tipo de Transaccion&nbsp;&nbsp;&nbsp;");
			$('label[for="id_f21_4"]').html("Razon&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_f21_5"]').html("Fecha de Terminación- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mes");
			$('label[for="id_f21_6"]').html("Dia");
			$('label[for="id_f21_7"]').html("Año");
			$('label[for="id_f21_8"]').html("Fecha de Separacion- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mes");
			$('label[for="id_f21_9"]').html("Dia");
			$('label[for="id_f21_10"]').html("Año");
			$('label[for="id_f22"]').html("AEELA");
			$('label[for="id_f23"]').html("Retiro");
			$('label[for="id_f23_1"]').html("Tipo de Cotizacion");
			$('label[for="id_f24"]').html("Jornada Completa Parcial&nbsp");
			$('label[for="id_f25"]').html("Asignacion principal&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp");
			$('label[for="id_f26"]').html("Facultad&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_f27"]').html("Descripcion de Tarea o Curso: &nbsp;(1)&nbsp;");
			$('label[for="id_f27_1"]').html("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_f27_2"]').html("Descripcion de Tarea o Curso: &nbsp;(2)&nbsp;");
			$('label[for="id_f27_3"]').html("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_f30"]').html("Observaciones y/o Programa Academico &nbsp;&nbsp;");

			$('label[for="id_sponsored_accounts"]').html("Spnsored Account- Campus&nbsp;&nbsp;");
			$('label[for="id_sponsored_accounts_1"]').html("Account Numbers &nbsp;&nbsp;");
			$('label[for="id_sponsored_accounts_2"]').html("Cost Category &nbsp;&nbsp;");
			$('label[for="id_sponsored_accounts_3"]').html("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Level of Effort &nbsp;&nbsp;");
			$('label[for="id_sponsored_accounts_4"]').html("Amount charged &nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_sponsored_accounts_5"]').html("Spnsored Account- Campus&nbsp;&nbsp;");
			$('label[for="id_sponsored_accounts_6"]').html("Account Numbers &nbsp;&nbsp;");
			$('label[for="id_sponsored_accounts_7"]').html("Cost Category &nbsp;&nbsp;");
			$('label[for="id_sponsored_accounts_8"]').html("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Level of Effort &nbsp;&nbsp;");
			$('label[for="id_sponsored_accounts_9"]').html("Amount charged &nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_sponsored_accounts_10"]').html("Spnsored Account- Campus&nbsp;&nbsp;");
			$('label[for="id_sponsored_accounts_11"]').html("Account Numbers &nbsp;&nbsp;");
			$('label[for="id_sponsored_accounts_12"]').html("Cost Category &nbsp;&nbsp;");
			$('label[for="id_sponsored_accounts_13"]').html("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Level of Effort &nbsp;&nbsp;");
			$('label[for="id_sponsored_accounts_14"]').html("Amount charged &nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_sponsored_accounts_15"]').html("Spnsored Account- Campus&nbsp;&nbsp;");
			$('label[for="id_sponsored_accounts_16"]').html("Account Numbers &nbsp;&nbsp;");
			$('label[for="id_sponsored_accounts_17"]').html("Cost Category &nbsp;&nbsp;");
			$('label[for="id_sponsored_accounts_18"]').html("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Level of Effort &nbsp;&nbsp;");
			$('label[for="id_sponsored_accounts_19"]').html("Amount charged &nbsp;&nbsp;&nbsp;&nbsp;");

			$('label[for="id_cost_sharing"]').html("Cost Sharing- Campus&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_cost_sharing_1"]').html("Account Numbers &nbsp;&nbsp;");
			$('label[for="id_cost_sharing_2"]').html("Cost Category &nbsp;&nbsp;");
			$('label[for="id_cost_sharing_3"]').html("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Level of Effort &nbsp;&nbsp;");
			$('label[for="id_cost_sharing_4"]').html("Amount charged &nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_cost_sharing_5"]').html("Cost Sharing- Campus&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_cost_sharing_6"]').html("Account Numbers &nbsp;&nbsp;");
			$('label[for="id_cost_sharing_7"]').html("Cost Category &nbsp;&nbsp;");
			$('label[for="id_cost_sharing_8"]').html("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Level of Effort &nbsp;&nbsp;");
			$('label[for="id_cost_sharing_9"]').html("Amount charged &nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_cost_sharing_10"]').html("Cost Sharing- Campus&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_cost_sharing_11"]').html("Account Numbers &nbsp;&nbsp;");
			$('label[for="id_cost_sharing_12"]').html("Cost Category &nbsp;&nbsp;");
			$('label[for="id_cost_sharing_13"]').html("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Level of Effort &nbsp;&nbsp;");
			$('label[for="id_cost_sharing_14"]').html("Amount charged &nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_cost_sharing_15"]').html("Cost Sharing- Campus&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_cost_sharing_16"]').html("Account Numbers &nbsp;&nbsp;");
			$('label[for="id_cost_sharing_17"]').html("Cost Category &nbsp;&nbsp;");
			$('label[for="id_cost_sharing_18"]').html("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Level of Effort &nbsp;&nbsp;");
			$('label[for="id_cost_sharing_19"]').html("Amount charged &nbsp;&nbsp;&nbsp;&nbsp;");

			$('label[for="id_university_funds"]').html("Cost Sharing- Campus&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_university_funds_1"]').html("Account Numbers &nbsp;&nbsp;");
			$('label[for="id_university_funds_2"]').html("Cost Category &nbsp;&nbsp;");
			$('label[for="id_university_funds_3"]').html("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Level of Effort &nbsp;&nbsp;");
			$('label[for="id_university_funds_4"]').html("Amount charged &nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_university_funds_5"]').html("Cost Sharing- Campus&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_university_funds_6"]').html("Account Numbers &nbsp;&nbsp;");
			$('label[for="id_university_funds_7"]').html("Cost Category &nbsp;&nbsp;");
			$('label[for="id_university_funds_8"]').html("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Level of Effort &nbsp;&nbsp;");
			$('label[for="id_university_funds_9"]').html("Amount charged &nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_university_funds_10"]').html("Cost Sharing- Campus&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_university_funds_11"]').html("Account Numbers &nbsp;&nbsp;");
			$('label[for="id_university_funds_12"]').html("Cost Category &nbsp;&nbsp;");
			$('label[for="id_university_funds_13"]').html("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Level of Effort &nbsp;&nbsp;");
			$('label[for="id_university_funds_14"]').html("Amount charged &nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_university_funds_15"]').html("Cost Sharing- Campus&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_university_funds_16"]').html("Account Numbers &nbsp;&nbsp;");
			$('label[for="id_university_funds_17"]').html("Cost Category &nbsp;&nbsp;");
			$('label[for="id_university_funds_18"]').html("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Level of Effort &nbsp;&nbsp;");
			$('label[for="id_university_funds_19"]').html("Amount charged &nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_university_funds_20"]').html("Cost Sharing- Campus&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_university_funds_21"]').html("Account Numbers &nbsp;&nbsp;");
			$('label[for="id_university_funds_22"]').html("Cost Category &nbsp;&nbsp;");
			$('label[for="id_university_funds_23"]').html("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Level of Effort &nbsp;&nbsp;");
			$('label[for="id_university_funds_24"]').html("Amount charged &nbsp;&nbsp;&nbsp;&nbsp;");

			$('label[for="id_total_compensation"]').html("Total- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Level of Effort&nbsp;&nbsp;&nbsp;");
			$('label[for="id_total_compensation_1"]').html("Amount Charged &nbsp;&nbsp;");

			$('label[for="id_payments_paid"]').html("Payments Paid- Account Number&nbsp;&nbsp;");
			$('label[for="id_payments_paid_1"]').html("Type of work &nbsp;&nbsp;");
			$('label[for="id_payments_paid_2"]').html("Amount Paid &nbsp;&nbsp;");
			$('label[for="id_payments_paid_3"]').html("Payments Paid- Account Number&nbsp;&nbsp;");
			$('label[for="id_payments_paid_4"]').html("Type of work &nbsp;&nbsp;");
			$('label[for="id_payments_paid_5"]').html("Amount Paid&nbsp;&nbsp;");
			$('label[for="id_payments_paid_8"]').html("Payments Paid- Account Number&nbsp;&nbsp;");

			$('label[for="id_Facultad"]').html("Facultad &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_NumPlaza"]').html("NumPlaza &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_Titulo_Rango"]').html("Titulo Rango&nbsp");
			$('label[for="id_Escala_Rate"]').html("Escala Rate&nbsp&nbsp&nbsp");
			$('label[for="id_SueldoTotal"]').html("Sueldo Total&nbsp&nbsp");

			$('label[for="id_professor"]').html("Professor &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_Facultad_1"]').html("Facultad &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_NumPlaza_1"]').html("NumPlaza &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;");
			$('label[for="id_Titulo_Rango_1"]').html("Titulo Rango&nbsp;&nbsp");
			$('label[for="id_Escala_Rate_1"]').html("Escala Rate&nbsp&nbsp&nbsp;&nbsp;&nbsp");
			$('label[for="id_SueldoTotal_1"]').html("Sueldo Total&nbsp;&nbsp;&nbsp&nbsp");
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