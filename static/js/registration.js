function sendregistermail(){
    var jqxhr = $.ajax({
    "url":"/jsonws/ws/",
    type: "POST",
    "data": {
        method:"sendacceptedmail",
        email:$("#reg-email").val()},
    beforeSend: function () {
            $("#sender").html("Идет обработка");
            $("#sender").attr("disabled", true);
    }
    } )
        .done(function() {
            //alert( "success" );
            alert( "На Ваш адресс " + $("#reg-email").val() + " выслано письмо с дальнейшими действиями.");
            $("#reg-email").attr("disabled", true);
            $("#point-one").css("text-decoration", "line-through");
        })
        .fail(function() {
            alert( "error" );
        })
        .always(function() {
            //alert( "На Ваш адресс " + $("#reg-email").val() + " выслано письмо с дальнейшими действиями.");
            $("#sender").html("Зарегистрироваться");
        });
    }
    