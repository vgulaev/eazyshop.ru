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
};