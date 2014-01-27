function TableChoice($scope) {
	$scope.exv = "";
	$scope.lines = [];
	
	var db = openDatabase("goods", "0.1", "A list of to do items.", 2000);
	db.transaction(function(tx) {
		tx.executeSql("select * from gchoice", [], function (trx, result) {
			for (var i=0; i < result.rows.length; i++) {
				$scope.lines.push({"id" : result.rows.item(i).id, "caption" : result.rows.item(i).caption});
			}
			$scope.$apply();
		}, null);
	});	

	$scope.clear = function clear () {
		var db = openDatabase("goods", "0.1", "A list of to do items.", 2000);
		db.transaction(function(tx) {
			tx.executeSql("delete from gchoice", [], function (trx, result) {
				$scope.lines = [];
				$scope.$apply();
			}, null);
		});	
	};

	$scope.printtest = function printtest () {
		//alert("Hello!!!");
		$scope.exv = "What ever you want";
		$scope.$apply();
	};

	$scope.removeitem = function removeitem (uid) {
		var db = openDatabase("goods", "0.1", "A list of to do items.", 2000);
		db.transaction(function(tx) {
			tx.executeSql("delete from gchoice where id = :id", {"id" : uid}, function (trx, result) {
				//$scope.lines = [];
				$scope.lines = $.grep( $scope.lines, function( n, i ) {
  						return n.id != uid;
				});				
				$scope.$apply();
				//alert(uid);
			}, null);
		});	
	};
}
//it = _.template($('#item-template').html());

/*function updatechoicetable() {
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
})*/