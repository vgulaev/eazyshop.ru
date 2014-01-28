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

function addgoodtochoice(goodsid, caption){
    var lines = getarrayfromlocalstorage("lines");
    
    if (localStorage.getItem(goodsid) == null) {
        lines.push(goodsid);    
        localStorage["lines"] = JSON.stringify(lines);
    }
    localStorage[goodsid] = JSON.stringify({"id" : goodsid, "caption" : caption, "amount" : 0});

    $("#art-name").html(caption);
    $("#art-name").attr("art-uid", goodsid);
    $("#page-choise").hide();
    $("#page-amount").show();
}

function updateamount() {
    var goodsid = $("#art-name").attr("art-uid");
    var temobj = JSON.parse(localStorage[goodsid]);
    temobj.amount = $("#amount").val();
    $("#amount").val("");
    localStorage[goodsid] = JSON.stringify(temobj);
    $("#page-choise").show();
    $("#page-amount").hide();
}

function uptableprice(){
    if ((!ajaxtopricetable) && (lastsubstr != $("#substr").val())) {
        var jqxhr = $.ajax({
            "url":"/htmlws/pricetable/",
            type: "POST",
            "data": {
                substr    : $("#substr").val(),
            },
            beforeSend: function () {
                ajaxtopricetable = true;
                ajaxcall = ajaxcall + 1;
                lastsubstr = $("#substr").val();
            },
        } )
        .done(function(data) {
            $("#output").html(data);
        })
        .fail(function() {
        })
        .always(function() {
            ajaxtopricetable = false;
            uptableprice();
        });
    }
    //$("#output2").html("Call bindcall: " + bindcall + " ajaxcall: " + ajaxcall);
    $("#output2").html("Height: " + window.screen.availHeight + " Width: " + window.screen.availWidth);
}

$(function () {
    ajaxtopricetable = false;
    bindcall = 0;
    ajaxcall = 0;
    lastsubstr = null;
    //createdb();
    uptableprice();
    $("#page-amount").hide();
    $("#substr").bind("change paste keyup", function () {
        bindcall = bindcall + 1;
        uptableprice();
        //alert("Try to find");
    });
})