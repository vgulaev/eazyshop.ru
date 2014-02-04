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

	$scope.updateamount = function removeitem (el) {
		localStorage[el.id] = JSON.stringify(el);
	}

	$scope.create_innerorder = function create_innerorder () {
		var sql = "START TRANSACTION; insert into innerorder (id1C) value ('{id1C}');"

		var today = new Date();
		var id1C = "new " + today.getFullYear() + "-" + today.getMonth() + "-" + today.getDate() + " " + today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
		//sql = sql.replace("{id1C}", id1C);
		sql = sql + " insert into innerorder_goods (id1C, rownumber) VALUES ('{id1C}', 3), ('{id1C}', 4)"

		for (e in $scope.lines) {
			sql = sql + "('{id1C}', " + e + "), "
		}

		sql = sql + ";COMMIT;";
		sql = sql.replace("/{id1C}/g", id1C);
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