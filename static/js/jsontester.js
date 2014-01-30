function sendAJAX() {
    var jqxhr = $.ajax({
        "url": $("#jsonserver").val(),
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
