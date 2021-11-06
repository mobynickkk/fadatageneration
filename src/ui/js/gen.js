
$('document').ready(function () {
	$('.generate').click(function () {


		var hash = document.querySelector('.main-block').getAttribute('id')
		var control = true
		var main_dict = {}
		main_dict = {}
		main_dict["user_id"] = `${hash}`
		main_dict["functions"] = []
		var words = ['import', 'compile', 'eval', 'exec', 'try', 'except', 'return', 'def', 'class', 'type', 'dir', 'dict', 'list', 'tuple', 'while', 'for', ' in', 'range', 'yield', 'async', 'await', 'lambda']
		document.querySelectorAll('.pole_for_func').forEach(function (el) {
			control = true
			var id = el.getAttribute('id')
			var F = String(el.querySelector('#F_{i}'.replace(new RegExp("{i}", "g"), id)).value)
			for (v in words) {
				if (F.includes(words[v])) {
					control = false

				}

			}

			var L = parseFloat(el.querySelector('#L_{i}'.replace(new RegExp("{i}", "g"), id)).value)
			var R = parseFloat(el.querySelector('#R_{i}'.replace(new RegExp("{i}", "g"), id)).value)
			if (L > R) { control = false };

			var S = parseFloat(el.querySelector('#S_{i}'.replace(new RegExp("{i}", "g"), id)).value)
			if (S > Math.abs(L - R) || S < 0) { control = false };

			var A = parseFloat(el.querySelector('#A_{i}'.replace(new RegExp("{i}", "g"), id)).value)
			

			var V = el.querySelectorAll('.checkbox-input')[0].checked
			var P = el.querySelectorAll('.checkbox-input')[1].checked

			if (F == "" || isNaN(L) || isNaN(R) || isNaN(S) || isNaN(A)) { control = false }

			if (control) {
				help_dict = {}
				help_dict['function'] = `${F}`
				help_dict['range_from'] = `${L}`
				help_dict['range_to'] = `${R}`
				help_dict['use_even_range'] = `${S}`
				help_dict['accuracy'] = `${A}`
				help_dict['use_emissions'] = `${V}`
				help_dict['use_template'] = `${P}`
				main_dict["functions"].push(help_dict)
			} else {
				$('#{id}'.replace(new RegExp("{id}", "g"), id)).css('borderColor', 'red')
			}

		})



		console.log(JSON.stringify(main_dict));
		$.ajax({
			type:"POST",
			url:"https://fa-data.herokuapp.com/api/",
			data:JSON.stringify(main_dict),
			success: function(data){
			console.log(data);
			$(".plot").attr("src", data);}
			
			
		})

	})


})


