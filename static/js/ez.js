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
            //location.reload();
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
    $("#output2").html("Call bindcall: " + bindcall + " ajaxcall: " + ajaxcall);
}

$(function () {
    ajaxtopricetable = false;
    bindcall = 0;
    ajaxcall = 0;
    lastsubstr = null;
    uptableprice();
    $("#substr").bind("change paste keyup", function () {
        bindcall = bindcall + 1;
        uptableprice();
        //alert("Try to find");
    });
})