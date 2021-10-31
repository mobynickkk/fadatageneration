
$('document').ready(function(){
	$('.generate').click(function(){
		
		
		var hash = document.querySelector('.main-block').getAttribute('id')
		var control = true
		var main_dict = {}
		main_dict[`${hash}`] = {}
		var words = ['import', 'compile', 'eval', 'exec', 'try', 'except', 'return', 'def', 'class', 'type', 'dir', 'dict', 'list', 'tuple', 'while', 'for', 'in', 'range', 'yield', 'async', 'await', 'lambda']
		document.querySelectorAll('.pole_for_func').forEach(function(el){
			control = true
			var id = el.getAttribute('id')
			var F = el.querySelector('#F_{i}'.replace(new RegExp("{i}", "g"),id)).value
			for (v in words){
				if (F.includes(words[v])){
					control = false
					
				}
				
			}
	
			var L = parseFloat(el.querySelector('#L_{i}'.replace(new RegExp("{i}", "g"),id)).value)
			var R = parseFloat(el.querySelector('#R_{i}'.replace(new RegExp("{i}", "g"),id)).value)
			if (L > R){control = false};
			
			var S = parseFloat(el.querySelector('#S_{i}'.replace(new RegExp("{i}", "g"),id)).value)
			if (S > Math.abs(L-R)|| S < 0){control = false};
		
			var A = parseFloat(el.querySelector('#A_{i}'.replace(new RegExp("{i}", "g"),id)).value)
			if (A <= 0 || A >= 1 ){control = false};
			
			var V = el.querySelectorAll('.checkbox-input')[0].checked
			var P = el.querySelectorAll('.checkbox-input')[1].checked
			
		
			if (!isNaN(F)|| isNaN(L)|| isNaN(R)|| isNaN(S)|| isNaN(A)){control=false}
			
			if (control){
				main_dict[`${hash}`][`${id}`] = {}
				main_dict[`${hash}`][`${id}`]['F'] = `${F}`
				main_dict[`${hash}`][`${id}`]['L'] = `${L}`
				main_dict[`${hash}`][`${id}`]['R'] = `${R}`
				main_dict[`${hash}`][`${id}`]['S'] = `${S}`
				main_dict[`${hash}`][`${id}`]['A'] = `${A}`
				main_dict[`${hash}`][`${id}`]['V'] = `${V}`
				main_dict[`${hash}`][`${id}`]['P'] = `${P}`
			}else{
				$('#{id}'.replace(new RegExp("{id}", "g"),id)).css('borderColor','red')
			}
			
			})
			
		
		
		console.log(JSON.stringify(main_dict));
		/* $.ajax({
			type:"POST",
			url:"#",
			data:JSON.stringify(main_dict),
			success: function(data){$(".plot").attr("src", data);}
		}) */
		
		})	
		
		
		})
		
	
		