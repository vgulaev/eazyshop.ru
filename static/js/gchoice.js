function TableChoice($scope) {
	$scope.lines = [];
	
	var lines = getarrayfromlocalstorage("lines");

	for (var l in lines) {
		var item = JSON.parse(localStorage[lines[l]]);
		delete item['$$hashKey'];
		$scope.lines.push(item);
	}

	$("#choicelength").html($scope.lines.length);

	$scope.clear = function clear () {
		var lines = getarrayfromlocalstorage("lines");
		for (var l in lines) {
			localStorage.removeItem(lines[l]);
		}
		localStorage.removeItem("lines");
		$scope.lines = [];
		$("#choicelength").html($scope.lines.length);
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

	$scope.updateamount = function updateamount (el) {
		localStorage[el.id] = JSON.stringify(el);
	};

	$scope.choicetoxml = function () {
		xstr = "";
		xstr = xstr + "<DocumentObject.ВнутреннийЗаказ>"
		xstr = xstr + "<Ответственный>" + $("meta[property='uid1c']").attr("content") + "</Ответственный>"
		xstr = xstr + "<Комментарий>" + $("#Комментарий").val() + "</Комментарий>"
		for (var l in $scope.lines) {
			xstr = xstr + '<row номенклатура = "' + $scope.lines[l]["id"] + '"' + ' количество = "' + $scope.lines[l]["amount"] + '"/>'
		}
		xstr = xstr + "</DocumentObject.ВнутреннийЗаказ>"
		return xstr;
	};
	
	$scope.create_innerorder = function create_innerorder () {
    	var cl = new suds1c;
    	var ws = cl.client({"url" : "/ws/restservice.1cws", "wsdl": "/ws/restservice.wsdl"});
    	ws.createobj({"data" : {"type" : "ВнутреннийЗаказ",
    		"variant" : "own",
    		"strrepresent" : $scope.choicetoxml()},
    				"done" : function (data) {
    					$scope.clear();
    				}
    			});
	}
}