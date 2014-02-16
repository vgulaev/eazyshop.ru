function suds1c () {
  var soapquery = function () {
    var xstr = '<?xml version="1.0" encoding="UTF-8"?>'+
    '<SOAP-ENV:Envelope xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">' +
    '<SOAP-ENV:Header/>'+
    '<ns0:Body>'+
    '</ns0:Body>'+
    '</SOAP-ENV:Envelope>';
    return $.parseXML(xstr);
  }

  var soapclient = function () {
  };

  this.client = function (paramobj) {
    res = new soapclient;
    $.ajax({
      "url" : paramobj["wsdl"],
      "type": "GET",
      "async" : false
    })
    .done(function (wsdl) {
      var namespace = wsdl.documentElement.attributes["targetNamespace"].value;
      var swname = wsdl.documentElement.attributes["targetNamespace"].value;
      var portType = wsdl.getElementsByTagName("portType");
      var operators = portType[0].getElementsByTagName("operation");
      for (var i = 0; i < operators.length; i++) {
        var methodname = operators[i].attributes["name"].value;
        res[methodname] = function (methodname) {
          return function (params) {
            var soapq = soapquery();
            $(soapq.documentElement).attr("xmlns:ns1", namespace);
            var body = soapq.documentElement.getElementsByTagNameNS("http://schemas.xmlsoap.org/soap/envelope/", "Body")[0];
            var el = soapq.createElement("ns1:" + methodname);
            if (params["data"] != undefined) {
              for (var e in params["data"]) {
                var pxml = soapq.createElement("ns1:" + e);
                pxml.textContent = params["data"][e];
                el.appendChild(pxml);
              }
            }
            body.appendChild(el);
            var xstr = (new XMLSerializer()).serializeToString(soapq);
            $.ajax({
              "url": paramobj["url"],
              type: "POST",
              "data": xstr
            })
            .done(function (data) {
              var res = $(data).text();
              params["done"](res);
            });
          }
        }(methodname);
      }
    })
.fail(function () {
});
return res;
};
}

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

