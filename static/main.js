/* while (true) {
    getDB();
    displayTable();
    console.log("update");
} */

getDB();
displayTable();

var tableContainer = document.getElementById("table-display");

function getDB(){
    console.log("Getting DB");

    fetch("/database", {
        method: "GET",
        headers: {
          "Content-Type": "application/json"
        },
      })
      .then(resp => {
        if (resp.ok)
          resp.json().then(data => {
            displayTable(data);
          });
      })
      .catch(err => {
        console.log("An error occured", err.message);
        window.alert("Oops! Something went wrong.");
      });
}

function displayTable(data) {
  //table
  // console.log("running display table");
  console.log(JSON.stringify(data));
  var tableContainer = document.getElementById("table-display");
  data = JSON.stringify(data, null, 4)
  
  console.log(data.length);
  // here
  // function tableCreate() {
  //   const body = document.body,
  //         tbl = document.createElement('table');
  //   tbl.style.width = '100px';
  //   tbl.style.border = '1px solid black';
  
  //   for (let i = 0; i < 3; i++) {
  //     const tr = tbl.insertRow();
  //     for (let j = 0; j < 2; j++) {
  //       if (i === 2 && j === 1) {
  //         break;
  //       } else {
  //         const td = tr.insertCell();
  //         td.appendChild(document.createTextNode(`Cell I${i}/J${j}`));
  //         td.style.border = '1px solid black';
  //         if (i === 1 && j === 1) {
  //           td.setAttribute('rowSpan', '2');
  //         }
  //       }
  //     }
  //   }
  //   body.appendChild(tbl);
  // }
  
  // tableCreate();
  // var length = Object.keys(data).length;
  for(var i = 0; i < length; i++) {
    // var div = document.createElement("div");
    // div.innerHTML = "<br>" + "<strong>" + 'Diagnosis: ' + "</strong>" + table[i].Diagnosis + "</br>" + '<br>' + "<strong>" + 'Level/Grade: ' + "</strong>" + table[i].LevelOrGrade + '</br>' + "<br>" + "<strong>" + 'Reasoning for diagnosis: ' + "</strong>"+ table[i].Reasoning + "</br>";	
    // tableContainer.appendChild(div);
    console.log("hi");
    console.log(data[i]);
  }

  //{"0":"2016-03-26 15:10:10","1":"2016-03-26 00:00:00","2":"2022-06-11 12:35:02.058480","3":"2016-03-26 15:10:10","4":"2016-03-26 00:00:00"}

  tableContainer.append(data); //div);
}

