Date.prototype.toMYSQL = function () {
    var s = this.getFullYear() + "-" + this.getMonth() + "-" + this.getDate() + " " + t.toLocaleTimeString();
    return s;
};

function curenttimeforMYSQL(){

}

function PageChooser($scope) {
    $scope.result = [];
    $scope.t = "";

    $scope.uptableprice = function uptableprice() {
        if ((!ajaxtopricetable) && (lastsubstr != $("#substr").val())) {
            var cond = $("#substr").val().split(" ");
            var filter = "True"
            for (e in cond) {
                if (cond[e].trim() != ""){
                    filter += "and caption like '%" + cond[e] + "%'";
                }
            }

            if (filter.trim() != "True"){
                filter = filter.slice(8);
            }

            var jqxhr = $.ajax({
                "url":"/jsonws/db/",
                type: "POST",
                "data": {
                    "method"        : "query",
                    "qtext"         : "select * from goods where {0} limit 10".replace("{0}", filter)
                },
                beforeSend: function () {
                    ajaxtopricetable = true;
                    ajaxcall = ajaxcall + 1;
                    lastsubstr = $("#substr").val();
                },
            })
            .done(function(data) {
                //$("#output").html(data);
                $scope.result = data;
                $scope.$apply();
            })
            .fail(function() {
            })
            .always(function() {
                ajaxtopricetable = false;
                $scope.uptableprice();
            });
        }
    }

    $scope.addgoodtochoice = function addgoodtochoice(el){
        var lines = getarrayfromlocalstorage("lines");
        var goodsid = el[0];
        var caption = el[2];
        if (localStorage.getItem(goodsid) == null) {
            lines.push(goodsid);    
            localStorage["lines"] = JSON.stringify(lines);
        }

        localStorage[goodsid] = JSON.stringify({"id" : goodsid, "caption" : caption, "amount" : 0, "unit": el[4]});

        $("#art-name").html(caption);
        $("#art-name").attr("art-uid", goodsid);
        $("#art-unit").html(el[4]);
        $("#page-choise").hide();
        $("#page-amount").show();
        $("#choicelength").html(lines.length);
    }

    $scope.uptableprice();
    $("#substr").bind("change paste keyup", function () {
        bindcall = bindcall + 1;
        $scope.uptableprice();
    });

}

function authorize(){
    var jqxhr = $.ajax({
        "url":"/jsonws/ws/",
        type: "POST",
        "data": {
            method    : "authorize",
            login     : $("#login").val(),
            pass      : $("#pass").val()
        },
        beforeSend: function () {
            $("#button-signin").html("Идет авторизация");
            $("#button-signin").attr("disabled", true);
        }
    } )
    .done(function( data ) {
            //$("#button-signin").attr("disabled", false);
            location.reload();
        })
    .fail(function() {
        alert( "error" );
    })
    .always(function() {
        $("#button-signin").html("Войти");
        $("#button-signin").attr("disabled", false);
    });
}

function logout(){
    var jqxhr = $.ajax({
        "url":"/jsonws/ws/",
        type: "POST",
        "data": {
            method    : "logout",
        },
        beforeSend: function () {
            $("#button-logout").html("Выходим...");
            $("#button-logout").attr("disabled", true);
        }
    } )
    .done(function() {
            //$("#button-signin").attr("disabled", false);
            location.reload();
        })
    .fail(function() {
        alert( "error" );
    })
    .always(function() {
        $("#button-logout").html("Войти");
        $("#button-logout").attr("disabled", false);
    });
}

function getarrayfromlocalstorage(arrayname){
    var lArray = localStorage.getItem(arrayname);
    if (lArray == null){
        lArray = [];
    }
    else {
        lArray = JSON.parse(lArray);
    }
    return lArray;
}

function updateamount() {
    var goodsid = $("#art-name").attr("art-uid");
    var temobj = JSON.parse(localStorage[goodsid]);
    temobj.amount = Number(parseFloat($("#amount").val()).toFixed(3));
    $("#amount").val("");
    localStorage[goodsid] = JSON.stringify(temobj);
    $("#page-choise").show();
    $("#page-amount").hide();
}

$(function () {
    ajaxtopricetable = false;
    bindcall = 0;
    ajaxcall = 0;
    lastsubstr = null;
    //createdb();
    $("#page-amount").hide();

    var lines = getarrayfromlocalstorage("lines");
    $("#choicelength").html(lines.length);
})