function InnerOrdersList ($scope) {
	$scope.lines = [];
	$scope.order = {};

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
				value[2] = (new Date(value[2])).toDateString();
			});
			$scope.$apply();
		})
		.fail(function() {
		})
		.always(function() {
		});
	}

	$scope.openinnerorder = function openinnerorder (id1c) {
		var jqxhr = $.ajax({
			"url":"/jsonws/db/",
			type: "POST",
			"data": {
				"method"        : "query",
				"qtext"         : "select * from innerorder order by docdate desc limit 0, 10"
			},
			beforeSend: function () {
				$("#ajaxing").css("left", (window.screen.availWidth - $("#ajaxing").width())/2 + "px");
				$("#ajaxing").css("top", ($("#maincontainer").height()- $("#ajaxing").height()) / 2 + "px");
				$("#ajaxing").show();
				$("#page-order-list").hide();
			},
		})
		.done(function(data) {
			$scope.lines = data.rows;
			angular.forEach($scope.lines, function(value, key){
				value[2] = (new Date(value[2])).toDateString();
			});
			$scope.$apply();
		})
		.fail(function() {
		})
		.always(function() {
		});
	}

	$scope.update();
}