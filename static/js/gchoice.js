function updatechoicetable() {
	db = openDatabase("goods", "0.1", "A list of to do items.", 2000);
    db.transaction(function(tx) {
        tx.executeSql("select * from gchoice", [], function (trx, result) {
    for (var i=0; i < result.rows.length; i++) {
      $('body').append(result.rows.item(i).id); // <-- getting Field1 value
    }
  }, null);
        });
}

$(function () {
	updatechoicetable();
})