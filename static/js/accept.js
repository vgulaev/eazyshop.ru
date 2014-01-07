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
            $("#reg-email").attr("disabled", true);
            $("#point-one").css("text-decoration", "line-through");
            alert("Поздравляем, Вы, успешно зарегистрировались!!! Перейдите на главную страницу или в личный кабинет");
        })
    .fail(function() {
        alert( "error" );
    })
    .always(function() {
        $("#sendform").html("Завершить регистрацию");
    });
}