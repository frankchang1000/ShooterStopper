
function displayTable(data) {
  //table
  console.log("running display table");
  table = data.table;
  var tableContainer = document.getElementById("table-display");
  var length = Object.keys(table).length;
  for(var i = 0; i < length; i++) {
    var div = document.createElement("div");
    div.innerHTML = "<br>" + "<strong>" + 'Diagnosis: ' + "</strong>" + table[i].Diagnosis + "</br>" + '<br>' + "<strong>" + 'Level/Grade: ' + "</strong>" + table[i].LevelOrGrade + '</br>' + "<br>" + "<strong>" + 'Reasoning for diagnosis: ' + "</strong>"+ table[i].Reasoning + "</br>";	
    tableContainer.appendChild(div);
    //console.log("json iterate: " + i);
  }
  show(tableContainer);
}
