#!c:/Python27/python.exe
def at(atname, value):
    r = ""
    if (value != ""):
        r = atname + ' = "' + value + '"'
    return r
    
def wh(text, tag, att = ""):
    return "<" + tag + " " + att + ">" + text + "</" + tag + ">"