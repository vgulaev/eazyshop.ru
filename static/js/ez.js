Date.prototype.toMYSQL = function () {
    var s = this.getFullYear() + "-" + this.getMonth() + "-" + this.getDate() + " " + t.toLocaleTimeString();
    return s;
};

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
                if ( data.rows.length == 0 ) {
                    $("#addposition").show();
                } else {
                    $("#addposition").hide();
                };
                $scope.$apply();
            })
            .fail(function() {
            })
            .always(function() {
                ajaxtopricetable = false;
                $scope.uptableprice();
            });
        }
    };

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
    };

    $scope.createposition = function () {
        var cl = new suds1c;
        var ws = cl.client({"url" : "/ws/restservice.1cws", "wsdl": "/ws/restservice.wsdl"});
        ws.createobj({"data" : {"type" : "Номенклатура",
            "variant" : "own",
            "strrepresent" : $("#substr").val()},
                    "done" : function (data) {
                        //alert(data);
                        sql = "insert into goods (id, caption) value ('{id}', '{caption}')";
                        sql = sql.replace("{id}", data);
                        sql = sql.replace("{caption}", $("#substr").val());
                        var jqxhr = $.ajax({
                            "url":"/jsonws/db/",
                            type: "POST",
                            "data": {
                                "method"        : "query",
                                "qtext"         : sql,
                                "commit"        : "True"
                            },
                            beforeSend: function () {
                            },
                        })
                        .done(function(data) {
                            $("#addposition").hide();
                            lastsubstr = "";
                            $scope.uptableprice();
                            })
                        .fail(function() {
                        })
                        .always(function() {
                        });
                    }
                });
    };
    $scope.clearsubstr = function () {
        $("#substr").val("");
        lastsubstr = "";
    };
    
    
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

function cancelchoise() {
    $("#page-choise").show();
    $("#page-amount").hide();
}

$(function () {
    ajaxtopricetable = false;
    bindcall = 0;
    ajaxcall = 0;
    lastsubstr = null;
    $("#page-amount").hide();
    var lines = getarrayfromlocalstorage("lines");
    $("#choicelength").html(lines.length);
    
    function moveloginformtop() {
        if ($("#togglebutton").css("display") != "none") {
            $("#userpassdiv").css("position", "absolute");
            $("#userpassdiv").css("top", "0px");
        }
    };
    
    function moveloginformdefault() {
        if ($("#togglebutton").css("display") != "none") {
            $("#userpassdiv").css("position", "inherit");
            $("#userpassdiv").css("top", "");
        }
    };
    $(".movetop").focus(moveloginformtop);
    $(".movetop").focusout(moveloginformdefault);
})