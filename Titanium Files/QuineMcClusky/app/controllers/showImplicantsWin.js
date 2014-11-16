var args = arguments[0] || {};
//alert(args.minterms);
var minterm = args.minterms;
var dontcare = args.dontcares;
var variables = args.variables;
var showWin = Ti.UI.createWindow({
	backgroundColor: 'white'
});
	var implicants;
	var func;
	var cover;
	var primeImplicants;

// var sectionPI = Ti.UI.createTableViewSection({ headerTitle: 'Prime Implicants' });
// for (var i=1; i<=implicants; i++){
  // var row = Ti.UI.createTableViewRow({
    // className:'forumEvent', // used to improve table performance
    // selectedBackgroundColor:'white',
    // rowIndex:i, // custom property, useful for determining the row during events
    // height:110
  // });

var implicantsTable = Ti.UI.createTableView({
	//data : primeImplicants,
	headerTitle: 'The Reduced Function',
	backgroundColor : "#FFFFFF"
});
var rfunction = Ti.UI.createTextArea({
	top: 200,
	center : true,
	color : "#0066FF",
	enabled : false,
	editable : false 
});
var nextStep = Ti.UI.createButton({
	title: "Start Over",
	center:true,
	top: 250,
	width: 150,
	height: 40,
	backgroundColor: "#0066FF",
	color: '#FFFFFF',
	borderRadius:5
});
nextStep.addEventListener('click', function(e){
	showWin.close();
});
showWin.add(implicantsTable);
showWin.add(nextStep);

function sendAjax(){
var url = 'http://10.0.2.2:3000/quine';
var params =  {'minterms':minterm , 'dontcares':dontcare,'Variables':variables};


var xhr = Ti.Network.createHTTPClient();
        xhr.onerror = function(e){
            var error = e.error;
            alert(error);               
        };
        xhr.open('POST', url);
        xhr.send(params);
        xhr.onload= function(e){
            if (this.readyState == 4) {
				 
            }
            else if (cancelSend) {
                  xhr.abort();
            }
        };
        xhr.ondatastream = function(e){           
        };
        xhr.onload = function(e) {
        	var array = JSON.parse(this.responseText);		
			func = array['function'];
			cover = array['cover'];
			primeImplicants = array['primeImplicants'];
			implicants = array['implicants'];
			alert("Cover "+cover);
			alert("Implicants "+implicants);
			alert("Prime Implicants "+ primeImplicants);
			implicantsTable.setData(implicants);
			rfunction.setValue(func);
			//alert(implicants.length);
			//implicantsTable.setSe
			// alert(cover);
			// alert(func);
			// alert(primeImplicants);
			 //alert(implicants);
			};
}

sendAjax();
showWin.add(rfunction);
showWin.open();
