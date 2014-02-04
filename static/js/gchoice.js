function TableChoice($scope) {
	$scope.lines = [];
	
	var lines = getarrayfromlocalstorage("lines");

	for (var l in lines) {
		var item = JSON.parse(localStorage[lines[l]]);
		$scope.lines.push({"id" : item.id, "caption" : item.caption, "amount" : item.amount});
	}

	$("#choicelength").html($scope.lines.length);
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
		$("#choicelength").html($scope.lines.length);
	};

	$scope.updateamount = function removeitem (el) {
		localStorage[el.id] = JSON.stringify(el);
	}

	$scope.create_innerorder = function create_innerorder () {
		var today = new Date();
		var sql = "START TRANSACTION; insert into innerorder (id1C, docdate) value ('{id1C}', '{docdate}');"
		var id1C = "new " + today.toJSON();
		sql = sql.replace("{docdate}", today.toJSON());
		//sql = sql.replace("{id1C}", id1C);
		sql = sql + " insert into innerorder_goods (id1C, rownumber, good, quantity) VALUES "

		for (e in $scope.lines) {
			sql = sql + "('{id1C}', " + e + ", '"+ $scope.lines[e].id + "'," + $scope.lines[e].amount + "),"
		}
		sql = sql.slice(0, -1);
		sql = sql + ";COMMIT;";
		sql = sql.replace(/{id1C}/g, id1C);
		var jqxhr = $.ajax({
			"url":"/jsonws/db/",
			type: "POST",
			"data": {
				"method"        : "query",
				"qtext"         : sql,
				"commit"		: "False"
			},
			beforeSend: function () {
			},
		})
		.done(function(data) {
			$scope.clear();
            })
		.fail(function() {
		})
		.always(function() {
		});
	}
}

$(function () {
	$("#output2").html(localStorage.length);
})