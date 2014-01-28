function TableChoice($scope) {
	$scope.exv = "";
	$scope.lines = [];
	
	var lines = getarrayfromlocalstorage("lines");

	for (var l in lines) {
		var item = JSON.parse(localStorage[lines[l]]);
		$scope.lines.push({"id" : item.id, "caption" : item.caption, "amount" : item.amount});
	}
	//$scope.$apply();

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
	};
}

$(function () {
	$("#output2").html(localStorage.length);
})