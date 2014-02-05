function InnerOrdersList ($scope, dateFilter) {
	$scope.lines = [];
	$scope.order = {};

	$scope.$watch('order.date', function (date)
    {
        $scope.order.dateString = dateFilter(date, 'yyyy-MM-dd');
    });

    $scope.$watch('order.dateString', function (dateString)
    {
        $scope.order.date = new Date(dateString);
    });	
	//$scope.dateString dateString
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
			angular.forEach($scope.lines, function(value, key){
				value[2] = dateFilter((new Date(value[2])), "yyyy-MM-dd");
			});
			$scope.$apply();
		})
		.fail(function() {
		})
		.always(function() {
		});
	}

	$scope.closeorder = function closeorder() {
		$("#page-order").hide();
		$("#page-order-list").show();
	}

	$scope.openinnerorder = function openinnerorder (id1c) {
		var s = ["select * from innerorder where id1C = '{id1C}'".replace("{id1C}", id1c), "select * from innerorder_goods where id1C = '{id1C}'".replace("{id1C}", id1c)];
		var jqxhr = $.ajax({
			"url":"/jsonws/db/",
			type: "POST",
			"data": {
				"method"        : "queries",
				"qtext"         : JSON.stringify(s)
			},
			beforeSend: function () {
				$("#ajaxing").css("left", (window.screen.availWidth - $("#ajaxing").width())/2 + "px");
				$("#ajaxing").css("top", ($("#maincontainer").height()- $("#ajaxing").height()) / 2 + "px");
				$("#ajaxing").show();
				$("#page-order-list").hide();
				$("#page-order").show();
			},
		})
		.done(function(data) {
			if (data.results.length > 0) {
				var headdata = data.results[0];
				if (headdata.rows.length > 0){
					var curent = headdata.rows[0];
					$scope.order.date = new Date(curent[2]);
				}
				var tabledata = data.results[1];
				if (tabledata.rows.length > 0) {
					$scope.order.lines = tabledata.rows;
				}
				$scope.$apply();
			}
		})
		.fail(function() {
		})
		.always(function() {
			$("#ajaxing").hide();
		});

	}

	$scope.update();
}