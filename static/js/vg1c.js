function loadvg1cobject (params) {
  vg1c = {};
  var cl = new suds1c;
  vg1c.ws = cl.client(params);
  $("[vg1csource]").each( function ( i ) {
    var strobj = $(this).attr("vg1csource");
    var defarray = strobj.split(".");
    var objid = this.id;
    vg1c[objid] = {};
    vg1c[objid].view = this;
    vg1c[objid].show = function () {
      $(this.view).show();
    }
    vg1c[objid].hide = function () {
      $(this.view).hide();
    }

    if (defarray[0] == "ДокументСписок") {
      vg1c[objid].tablename = "Документ." + defarray[1];
      var colums = "";
      $(this).find("[vg1cfield]").each( function () {
        colums = colums + $(this).attr("vg1cfield") + ",";
      });
      if (colums != "") {colums = colums.slice(colums, -1)};
      vg1c[objid].colums = colums;
      vg1c[objid].comands = "open";

      vg1c[objid].update = function (params) {
        var first = params["first"];
        var count = params["count"];
        if (first == undefined) {
          first = "0";
        };
        if (count == undefined) {
          count = "10";
        };
        vg1c.ws.gettable({
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
              if (vg1c[objid].comands == "open") {
                var td = document.createElement("td");
                $(td).html('<a href="/innerorder/' + $(this).attr("uid") + '" class="btn btn-success"><span class = "glyphicon glyphicon-folder-open"></span></a>');
                tr.appendChild(td);
              };
              tbody.append(tr);
            });
          }
        });
      };
    }
    else if (defarray[0] == "ДокументОбъект") {
      vg1c[objid]["push"] = {length : 0, items: {}};
      vg1c[objid].pushtoserver = function () {
        var fields = [];
        var values = [];
        for (i in vg1c[objid]["push"].items){
          fields.push(i);
          values.push(vg1c[objid]["push"].items[i]);
        }
        vg1c.ws.update({
      "data" : {
        "type" : "",
        "uid" : $("meta[property='orderuid']").attr("content"),
        "version" : "",
        "field" : fields.join(","),
        "value" : values.join(",")
      },
      "done" : function (data) {
        vg1c.innerorder.update({"uid" : $("[property='orderuid']").attr("content")});       
      }
    });
        vg1c[objid]["push"] = {length : 0, items: {}};
        var bt = $( "[vg1ccommand = 'write']" );
        $( bt ).hide();
      };
      $( "[vg1ccommand = 'write']" ).click(vg1c[objid].pushtoserver);
      vg1c[objid].update = function (params) {
        vg1c.ws.getobj({
          "data" : {
            "uid" : params["uid"],
            "type" : "ВнутреннийЗаказ",
            "variant" : "own",
          },
          "done" : function (data) {
            var xmltable = $.parseXML(data);
            $(vg1c[objid].view).attr("uid", params["uid"]);
            $(vg1c[objid].view).attr("version", $(xmltable).find("DataVersion").text());
            $(vg1c[objid].view).find("input[vg1cfield]").each(function ( i ) {
              var node = $(xmltable).find($(this).attr("vg1cfield"));
              $(this).val(node.text());
              if ($(this).attr("vg1cuid") != undefined) {
                $(this).attr("vg1cuid", $(node).attr("uid"));
              }
            });
            $(vg1c[objid].view).find("textarea[vg1cfield]").each(function ( i ) {
              var node = $(xmltable).find($(this).attr("vg1cfield"));
              $(this).html(node.text());
            });
            $(vg1c[objid].view).find("table[vg1ctable]").each(function ( i ) {
              var columns = $(this).find("[vg1ccolumn]");
              var tbody = $(this).find("tbody");
              var index = 0;
              var tablename = $(this).attr("vg1ctable");
              tbody.empty();
              $(xmltable).find(tablename + ">Row").each(function () {
                var tr = document.createElement("tr");
                for (var i = 0; i < columns.length; i++) {
                  var td = document.createElement("td");
                  var fieldname = $(columns[i]).attr("vg1ccolumn");
                  var represent = $(this).find(fieldname).text();
                  var tdinner = represent;
                  if ($(columns[i]).attr("vg1ceditable") == "true") {
                    var tid = tablename + "[" + index + "]." + fieldname;
                    tdinner = "<input id = '" + tid + "' value = '" + represent + "' class = 'choise-input' vg1ceditable = 'true'>";
                  }
                  $(td).html(tdinner);
                  tr.appendChild(td);
                };
                tbody.append(tr);
                index = index + 1;
              });
            });
            var onchangefunction = function () {
              if (vg1c[objid].push.items[this.id] == undefined) {
                vg1c[objid]["push"].length = vg1c[objid]["push"].length + 1;
              }
              vg1c[objid].push.items[this.id] = $(this).val();
              var bt = $( "[vg1ccommand = 'write']" );
              bt.show();
              $( bt ).find("span").html(vg1c[objid]["push"].length);
            };
            $("input[vg1ceditable='true']").bind("change paste keyup", onchangefunction);
            $("textarea[vg1ceditable='true']").bind("change paste keyup", onchangefunction);
            var k = 1;
          }
        });
}
}
});
}

$(function () {
    //cl = new suds1c;
    //ws = cl.client({"url" : "http://127.0.0.1:8000/ws/restservice.1cws", "wsdl": "http://127.0.0.1:8000/ws/restservice.wsdl"});
    /*ws.helloword({"done" : function (data) {
      alert(data);
    }});*/
    //loadvg1cobject({"url" : "http://127.0.0.1:8000/ws/restservice.1cws", "wsdl": "http://127.0.0.1:8000/ws/restservice.wsdl"});
    //vg1c.tab.hide();
    //vg1c.innerorder.update({"uid" : "3081c8b7-9498-11e3-88b2-94de80b807e8"});
    //vg1c.tab.update({});
    //vg1c.innerorder.hide();
});