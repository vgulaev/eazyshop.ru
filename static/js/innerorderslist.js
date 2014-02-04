function InnerOrdersList ($scope) {
	$scope.lines = [];

	$scope.update = function update() {
		var jqxhr = $.ajax({
			"url":"/jsonws/db/",
			type: "POST",
			"data": {
				"method"        : "query",
				"qtext"         : "select * from innerorder order by docdate desc limit 0, 10"
			},
			beforeSend: function () {
			},
		})
		.done(function(data) {
			$scope.lines = data.rows;
			$scope.$apply();
		})
		.fail(function() {
		})
		.always(function() {
		});
	}

	$scope.update();
}