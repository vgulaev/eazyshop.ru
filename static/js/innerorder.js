function acceptorder () {
		vg1c.ws.updateobj({
			"data" : {
				"type" : "",
				"uid" : $("meta[property='orderuid']").attr("content"),
				"version" : "",
				"field" : "Исполнитель",
				"value" : "1b194a0e-7da9-11e3-8908-5404a68af278"
			},
			"done" : function (data) {
				vg1c.innerorder.update({"uid" : $("[property='orderuid']").attr("content")});				
			}
		});
	};
$(function () {
	loadvg1cobject({"url" : "/ws/restservice.1cws", "wsdl": "/ws/restservice.wsdl"});
	vg1c.innerorder.update({"uid" : $("[property='orderuid']").attr("content")});
});

function InnerOrders ($scope, dateFilter) {
	$scope.order = {};
	$scope.orderuid = $("[property='orderuid']").attr("content");

	$scope.$watch('order.Date', function (date)
    {
        $scope.order.dateString = dateFilter(date, 'yyyy-MM-dd');
    });

    $scope.$watch('order.dateString', function (dateString)
    {
        $scope.order.Date = new Date(dateString);
    });
	//$scope.dateString dateString
	$scope.update = function update() {
		/*var sql = [];
		var jqxhr = $.ajax({
			"url":"/jsonws/ws/",
			type: "POST",
			"data": {
				"method"        : "getorder",
				"uid"			: $scope.orderuid
			},
			beforeSend: function () {
				$("#ajaxing").css("left", (window.screen.availWidth - $("#ajaxing").width())/2 + "px");
				$("#ajaxing").css("top", ($("#maincontainer").height()- $("#ajaxing").height()) / 2 + "px");
				$("#ajaxing").show();
			},
		})
		.done(function(data) {
			$scope.order = data;
			$scope.Date = new Date($scope.Date);
			$scope.$apply();
		})
		.fail(function() {
		})
		.always(function() {
			$("#ajaxing").hide();
		});*/
	}

	//$scope.update();
}