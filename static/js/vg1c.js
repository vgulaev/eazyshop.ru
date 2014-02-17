function loadvg1cobject () {
    vg1c = {};
    $("[vg1csource]").each( function ( i ) {
        var strobj = $(this).attr("vg1csource");
        var defarray = strobj.split(".");
        if (defarray[0] == "ДокументСписок") {
          var objid = this.id;
          vg1c[objid] = {};
          vg1c[objid].view = this;
          vg1c[objid].tablename = "Документ." + defarray[1];
          var colums = "";
          $(this).find("[vg1cfield]").each( function () {
            colums = colums + $(this).attr("vg1cfield") + ",";
          });
          if (colums != "") {colums = colums.slice(colums, -1)};
          vg1c[objid].colums = colums;

          vg1c[objid].update = function (params) {
            var first = params["first"];
            var count = params["count"];
            if (first == undefined) {
                first = "0";
            };
            if (count == undefined) {
                count = "10";
            };
            ws.gettable({
              "data" : {
                "tablename" : this.tablename,
                "colums" : this.colums,
                "firstrecord" : first,
                "count" : count
              },
              "done" : function (data) {
                var xmltable = $.parseXML(data);
                var tbody = $(vg1c.tab.view).find("tbody");
                tbody.empty();
                var tdnames = colums.split(",");
                $(xmltable).find("row").each(function () {
                  var tr = document.createElement("tr");
                  for (var i =  0; i < tdnames.length; i++) {
                    var td = document.createElement("td");
                    $(td).html($(this).attr(tdnames[i]));
                    tr.appendChild(td);
                  };
                  tbody.append(tr);
                });
              }
            });
          };
          vg1c[objid].show = function () {
            $(this.view).show();
          }
          vg1c[objid].hide = function () {
            $(this.view).hide();
          }
        }
        var k = 1;
    });
}

$(function () {
    cl = new suds1c;
    ws = cl.client({"url" : "http://127.0.0.1/USODev2014/ws/restservice.1cws", "wsdl": "http://127.0.0.1/USODev2014/ws/restservice.1cws?wsdl"});

    /*ws.helloword({"done" : function (data) {
      alert(data);
    }});*/
    loadvg1cobject();
    
    vg1c.tab.update({});
    //vg1c.tab.hide();
/*ws.getobj({
  "data" : {
    "uid" : "3081c8b7-9498-11e3-88b2-94de80b807e8",
    "type" : "ВнутреннийЗаказ",
    "variant" : "own",
  },
  "done" : function (data) {
    alert(data)
  }
});*/
});

