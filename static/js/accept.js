function sendform(){
    var jqxhr = $.ajax({
        "url":"/jsonws/ws/",
        type: "POST",
        "data": {
            method    : "addaccount",
            email     : $("#email").val(),
            pass      : $("#passwd").val(),
            shopname  : $("#shopname").val(),
            synonyms  : $("#synonyms").val()
        },
        beforeSend: function () {
            $("#sendform").html("Идет обработка");
            $("#sendform").attr("disabled", true);
        }
    } )
    .done(function() {
            //alert( "success" );
            //alert( "На Ваш адресс " + $("#reg-email").val() + " выслано письмо с дальнейшими действиями.");
            $("#reg-email").attr("disabled", true);
            $("#point-one").css("text-decoration", "line-through");
        })
    .fail(function() {
        alert( "error" );
    })
    .always(function() {
        $("#sendform").html("Завершить регистрацию");
    });
}