window.onload = function() {
	var fields = document.querySelectorAll(".ui.form [type=file]");

	for (var i = fields.length - 1; i >= 0; i--) {
		var field = fields[i];
		
		field.onclick = function() {
			field.value = null;
		};

		field.onchange = function() {
			var el = field.nextSibling.querySelector("span");
			if (field.files.length > 1)
				return el.textContent = field.files.length.toString() + " files";
			el.textContent = field.files[0].name;
		};
	}
}