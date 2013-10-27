function getXmlHttp() {
    var xmlhttp;
    try {
        xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
    } catch (e) {
        try {
            xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        } catch (e) {
            xmlhttp = false;
        }
    }
    if (!xmlhttp && typeof XMLHttpRequest != 'undefined') {
        xmlhttp = new XMLHttpRequest();
    }
    return xmlhttp;
}

function showprice() {
    //alert("show");
    req = getXmlHttp();

    req.onreadystatechange = function () {
        if (req.readyState == 4)
            statusElem.innerHTML = req.statusText;
        if (req.status == 200) {
            alert("Ответ сервера: " + req.responseText);
        }
    }
}
}