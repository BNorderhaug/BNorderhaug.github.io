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
		localSave();
	}
	
	function crossedOut() {
		parent=this.parentNode;
		if (parent.className != "done") {
			parent.className = "done";
			localSave();
		}
		else {
			parent.className = "";
			localSave();
		}
	}
	
	function savedList() {
	
		list = JSON.parse(localStorage.getItem("toDoSave"));
		while (list.length != 0) {
			var newtaskli = document.createElement("LI");
			var checkbox = document.createElement("INPUT");
			checkbox.type="checkbox";
			newtaskli.appendChild(checkbox);
		
			var innerInput = list[0];
			var outerContainer = document.createElement("SPAN");
			outerContainer.innerHTML = innerInput;
			newtaskli.appendChild(outerContainer);
		
			var newList = document.getElementById("list");
			newList.appendChild(newtaskli);
		
			list.shift();
			checkbox.onclick = crossedOut;
		}	
	}
	
	window.onload = savedList;
	
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