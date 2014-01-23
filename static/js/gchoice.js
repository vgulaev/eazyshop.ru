function TableController($scope) {
	$scope.exv = "";
	$scope.printtest = function printtest () {
		alert("Hello!!!");
		$scope.exv = "Hello!!!";
		$scope.$apply();
	}
}
//it = _.template($('#item-template').html());

function updatechoicetable() {
	db = openDatabase("goods", "0.1", "A list of to do items.", 2000);
	db.transaction(function(tx) {
		tx.executeSql("select * from gchoice", [], function (trx, result) {
			
			for (var i=0; i < result.rows.length; i++) {
      			//$('#tbodychoice').append(it({"title": result.rows.item(i).id})); // <-- getting Field1 value
  			}
		}, null);
	});
}

$(function () {
	updatechoicetable();
})