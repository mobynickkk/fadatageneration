$('document').ready(function () {
    $('#generate').click(function (event) {
		event.preventDefault()

        let hash = document.querySelector('.main-block').getAttribute('id')
        let control = true
        let main_dict = {
        	user_id: `${hash}-${Date.now()}`,
			functions: []
		}
        let words = ['import', 'compile', 'eval', 'exec', 'try', 'except', 'return', 'def', 'class', 'type', 'dir',
			'dict', 'list', 'tuple', 'while', 'for', ' in', 'range', 'yield', 'async', 'await', 'lambda']
        document.querySelectorAll('.pole_for_func').forEach(function (el) {
            control = true
            let id = el.getAttribute('id')
            let F = String(el.querySelector('#F_{i}'.replace(new RegExp("{i}", "g"), id)).value)
            for (v in words) {
                if (F.includes(words[v])) {
                    control = false

                }

            }


            let L = parseFloat(el.querySelector('#L_{i}'.replace(new RegExp("{i}", "g"), id)).value)
            let R = parseFloat(el.querySelector('#R_{i}'.replace(new RegExp("{i}", "g"), id)).value)
            if (L > R) {
                control = false
            }

            let S = parseFloat(el.querySelector('#S_{i}'.replace(new RegExp("{i}", "g"), id)).value)
            if (S > Math.abs(L - R) || S < 0) {
                control = false
            }

            let A = parseFloat(el.querySelector('#A_{i}'.replace(new RegExp("{i}", "g"), id)).value)


            let V = el.querySelectorAll('.checkbox-input')[0].checked
            let P = el.querySelectorAll('.checkbox-input')[1].checked

            if (F == "" || isNaN(L) || isNaN(R) || isNaN(S) || isNaN(A)) {
                control = false
            }

			let help_dict;
			if (control) {
				help_dict = {
					function: `${F}`,
					range_from: L,
					range_to: R,
					step: S,
					accuracy: A,
					use_emissions: V,
					use_template: P
				}
				main_dict["functions"].push(help_dict)
			} else {
				$('#{id}'.replace(new RegExp("{id}", "g"), id)).css('borderColor', 'red')
			}

        })


        console.log(JSON.stringify(main_dict));
        $.ajax({
            type: "POST",
            url: "https://fa-data.herokuapp.com/api/",
            contentType: "application/json; charset=utf-8",
            headers: {
                "Access-Control-Allow-Origin": "*",
            },
            dataType: "json",
            data: JSON.stringify(main_dict),
            success: function (data) {
                console.log(data['img_base64']);
                $("#plot").attr("src", `https://fa-data.herokuapp.com/${data['img_base64']}`);
                $("#save").attr("href", `https://fa-data.herokuapp.com/${data['csv_path']}`);
            }
        })
    })


})


