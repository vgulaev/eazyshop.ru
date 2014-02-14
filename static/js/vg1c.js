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
      alert("ok");
    })
    .fail(function () {
    });


    return res;
  };
}

cl = new suds1c;
ws = cl.client({"url" : "http://127.0.0.1/USODev2014/ws/restservice.1cws",
 "wsdl": "http://127.0.0.1/USODev2014/ws/restservice.1cws?wsdl"});
ws
