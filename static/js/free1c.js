function s4() {
  return Math.floor((1 + Math.random()) * 0x10000)
             .toString(16)
             .substring(1);
};

function guid() {
  return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
         s4() + '-' + s4() + s4() + s4();
}

Документы = {
    "ВнутреннийЗаказ" : {
        __name__ : "ВнутреннийЗаказ",
        СоздатьДокумент: function (attr) {
            var res = {
                Прочитать: function () {
                    var r = $.Deferred();
                    r.resolve();
                    return r;
                }
            };
            res.__sqlselect__ = {
              "main": "SELECT"
            };
            var field = attr.split(",");
            var sqlfields = [];
            for (var f in field){
                var cf = field[f].trim(); //
                var tm = cf.split("."); //
                if (tm.length == 1) {
                    var sqlname = Схема1С.Документ["ВнутреннийЗаказ"].Поля[cf];
                    res[cf] = "";
                    sqlfields.push("t." + Схема1С.Документ["ВнутреннийЗаказ"].Поля[cf]);
                }
                else if (tm.length == 2) {
                    var fieldName = tm[0].trim();
                    if (res[fieldName] == undefined) {
                      res[fieldName] = {};
                      res[fieldName]["Колонки"] = {};
                      res[fieldName]["Строки"] = [];
                      };
                    res[fieldName].Колонки[tm[1]] = "";
                }
            }
            return res;
        }
    }
}

r = $.Deferred();
r
.done(function () {
    alert("Task complate");
});

//к = Документы.ВнутреннийЗаказ.СоздатьДокумент("Номер, Товары.НомерСтроки");