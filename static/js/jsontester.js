function sendAJAX() {
    var jqxhr = $.ajax({
        "url":"/jsonws/ws/",
        type: "POST",
        "data": JSON.parse($("#jsondata").val()),
        beforeSend: function () {
        }
    } )
    .done(function( data ) {
        })
    .fail(function() {
    })
    .always(function() {
    });
}
