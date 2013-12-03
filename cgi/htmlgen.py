#!c:/Python27/python.exe
import htmlgenerator as hg

class htmltag:
	id = ""
	_class = ""

class button(htmltag):
	caption = ""
	def text(self):
		return '<button' + hg.at("id", self.id) + hg.at("class", self._class) + '>' + self.caption + '</button>'

class input(htmltag):
	def text(self):
		return '<input' + hg.at("id", self.id) + hg.at("class", self._class) + '></input>'

class htmlgn:
	items = []
	def gen(self):
		print "<!DOCTYPE html><html><head>"
		print hg.wh("", "script", hg.at("src", "//code.jquery.com/jquery-1.10.2.min.js"))
		print "</head><body>"
		print "Hello word"
		for i in self.items:
			print i.text();
		print "</body></html>"