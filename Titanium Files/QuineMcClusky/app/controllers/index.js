var inputWin = Ti.UI.createWindow({
	backgroundColor: 'white'
});
/*var showImplicantsWin = Ti.UI.createWindow({
	backgroundColor: 'white'
});
var showPrimeImplicantsWin = Ti.UI.createWindow({
	backgroundColor: 'white'
});*/

var minterms = Ti.UI.createTextField({
  borderStyle: Ti.UI.INPUT_BORDERSTYLE_ROUNDED,
  color: '#336699',
  top: 50, left: 10,
  width: 250, height: 60,
  hintText : "Minterms",
  editable: true
});
var dontcares = Ti.UI.createTextField({
  borderStyle: Ti.UI.INPUT_BORDERSTYLE_ROUNDED,
  color: '#336699',
  top: 150, left: 10,
  width: 250, height: 60,
  hintText : "Don't Cares",
  editable: true
});

var variables = Ti.UI.createTextField({
  borderStyle: Ti.UI.INPUT_BORDERSTYLE_ROUNDED,
  color: '#336699',
  top: 250, left: 10,
  width: 250, height: 60,
  hintText : "Number of variables",
  editable: true
});
var minimize = Ti.UI.createButton({
	title: "Minimize",
	center:true,
	top: 350,
	width: 150,
	height: 40,
	backgroundColor: "#0066FF",
	color: '#FFFFFF',
	borderRadius:5
});
inputWin.add(minterms);
inputWin.add(dontcares);
inputWin.add(variables);
inputWin.add(minimize);
inputWin.open();
minimize.addEventListener('click',function(minE){
	var mintermsText = minterms.getValue();
	var dontcaresText = dontcares.getValue();
	var variablesText = variables.getValue();
	//inputWin.close();
	//showImplicantsWin.open();
	//var nextView = Alloy.createController("showImplicantsWin",{minterms: mintermsText , dontcares: dontcaresText}).getView();
	//nextView.open();
	Alloy.createController("showImplicantsWin",{minterms: mintermsText , dontcares: dontcaresText, variables: variablesText}).getView();
	//inputWin.add(nextView);
});
// var tableData= [];
// var implicantsTable = Ti.UI.createTableView({
// 	
	// data: tableData
// 	
// });
// var contToPI = Ti.UI.createButton({
	// title: "Continue",
	// center:true,
	// top: 300,
	// width: 150,
	// height: 40,
	// backgroundColor: "#0066FF",
	// color: '#FFFFFF',
	// borderRadius:5
// });
// showImplicantsWin.add(implicantsTable);
// showImplicantsWin.add(contToPI);
// contToPI.addEventListener('click',function(conE){
	// showImplicantsWin.close();
	// showPrimeImplicantsWin.open();
// }
// );


