	function execute() {
	
		var newtaskli = document.createElement("LI");
		var checkbox = document.createElement("INPUT");
		checkbox.type= "checkbox";
		newtaskli.appendChild(checkbox);
		
		var innerInput = document.getElementById("textbox1").value;
		var outerContainer = document.createElement("SPAN");
		outerContainer.innerHTML= innerInput;
		newtaskli.appendChild(outerContainer);
		
		var list = document.getElementById("list");
		list.appendChild(newtaskli);
		
		checkbox.onclick = crossedOut;
	}
	
	function savedList() {
	
		list = JSON.parse(localStorage.getItem("toDoSave"));
		var newtaskli = document.createElement("LI");
		var checkbox = document.createElement("INPUT");
		checkbox.type="checkbox";
		newtaskli.appendChild(checkbox);
		
		var innerInput = document.getElementById("textbox1").value;
		var outerContainer = document.createElement("SPAN");
		
		.shift
	}
	
	window.onload = savedList;
	
	function crossedOut() {
		parent=this.parentNode;
		if (parent.className != "done") {
			parent.className = "done";
		}
		else {
			parent.className = "";
		}
	}
	
	function localSave() {
		res = [];
		var i;
		allEntries = document.querySelectorAll('li');
		for (i=0; i< allEntries.length; i++) {
			if (allEntries[i].className != "done") {
				res.push(allEntries[i].innerText)
			}
		}
		localStorage.setItem("toDoSave", JSON.stringify(res));
	}