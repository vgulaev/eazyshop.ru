function update_release_date() {
    var curent_time = new Date();
    var release_time = new Date(2014, 5, 1);
    var diff = new Date(release_time - curent_time);
    var oneDay = 1000 * 60 * 60 * 24;
    var days = Math.floor(diff / oneDay);
    $("#release_time").html(days + " дня и " + diff.getHours() + " : " + diff.getMinutes() + " : " + diff.getSeconds());
}

$(function () {
    update_release_date();
    setInterval(update_release_date, 1000);
});