Документы = {
    "ВнутреннийЗаказ" : {
        СоздатьДокумент: function (attr) {
            var res = {};
            var field = attr.split(",");
            for (var f in field){
                var cf = field[f]; //
                var tm = cf.split("."); //
                if (tm.length == 1) {
                    res[cf] = "";
                }
                else if (tm.length == 2) {
                    var fieldName = tm[0].trim();
                    if (res[fieldName] == undefined) {res[fieldName] = {}};
                    res[fieldName][tm[1]] = "";
                }
            }
            return res;
        }
    }
}

к = Документы.ВнутреннийЗаказ.СоздатьДокумент("Номер, Товары.НомерСтроки");