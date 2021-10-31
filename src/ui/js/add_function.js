$(document).ready(function () {
	$('#add').click(function () {
		var a = $('.function > .pole_for_func').length;
		if (a < 14) {
			$('.function').append('<div class="pole_for_func" id={id}>\
						<input class = "input_func" id = "F_{id}" style = "width:31%" placeholder="Функция"></input>\
						<input class = "input_func_L" id = "L_{id}" style = "width:5%" placeholder="L"></input>\
						<input class = "input_func_R" id = "R_{id}" style = "width:5%" placeholder="R"></input>\
						<input class = "input_func" id = "S_{id}" style = "width:5%" placeholder="Шаг"></input>\
						<input class = "input_func" id = "A_{id}" style = "width:5%" placeholder="Acc"></input>\
						<input class="checkbox-input" style = "margin-left:3%" type="checkbox" >Выбросы<Br>\
						<input class="checkbox-input" style = "margin-left:3%" type="checkbox" >Шаблоны<Br>\
	</div>'.replace(new RegExp("{id}", "g"), a + 1))
		}
		else {
			alert('Максимальное количество функций')
		}

	});
});

$(document).ready(function () {
	$('#del').click(function () {
		var a = $('.function > .pole_for_func').length;


		if (a > 1) {
			$("#{id}".replace(new RegExp("{id}", "g"), a)).remove()
		}
		else {
			alert('Минимальное количество функций')
		}

	});
});
