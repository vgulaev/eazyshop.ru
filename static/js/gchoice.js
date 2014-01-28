function TableChoice($scope) {
	$scope.exv = "";
	$scope.lines = [];
	
	var lines = getarrayfromlocalstorage("lines");

	for (var l in lines) {
		var item = JSON.parse(localStorage[lines[l]]);
		$scope.lines.push({"id" : item.id, "caption" : item.caption});
	}
	$scope.$apply();

	/*var db = openDatabase("goods", "0.1", "A list of to do items.", 2000);
	db.transaction(function(tx) {
		tx.executeSql("select * from gchoice", [], function (trx, result) {
			for (var i=0; i < result.rows.length; i++) {
				$scope.lines.push({"id" : result.rows.item(i).id, "caption" : result.rows.item(i).caption});
			}
			$scope.$apply();
		}, null);
	});	*/

	$scope.clear = function clear () {
		var lines = getarrayfromlocalstorage("lines");
		for (var l in lines) {
			localStorage.removeItem(lines[l]);
		}
		localStorage.removeItem("lines");
		$scope.lines = [];
		$scope.$apply();
	};

	$scope.printtest = function printtest () {
		//alert("Hello!!!");
		$scope.exv = "What ever you want";
		$scope.$apply();
	};

	$scope.removeitem = function removeitem (uid) {
		var lines = [];
		$scope.lines = $.grep( $scope.lines, function( n, i ) {
			if (n.id != uid){
				lines.push(n.id);
			}
			return n.id != uid;
			});
		localStorage["lines"] = JSON.stringify(lines);
		localStorage.removeItem(uid);
		/*var db = openDatabase("goods", "0.1", "A list of to do items.", 2000);
		db.transaction(function(tx) {
			tx.executeSql("delete from gchoice where id = :id", {"id" : uid}, function (trx, result) {
				//$scope.lines = [];
				$scope.lines = $.grep( $scope.lines, function( n, i ) {
  						return n.id != uid;
				});				
				$scope.$apply();
				//alert(uid);
			}, null);
		});	*/
	};
}

$(function () {
	$("#output2").html(localStorage.length);
})