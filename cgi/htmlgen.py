#!c:/Python27/python.exe
import htmlgenerator as hg

class button:
	id = ""
	_class = ""
	caption = ""
	def text(self):
		return '<button' + hg.at("id", self.id) + hg.at("class", self._class) + '>' + self.caption + '</button>'

class htmlgn:
	items = []
	def gen(self):
		print "<!DOCTYPE html><html><head></head><body>"
		print "Hello word"
		for i in self.items:
			print i.text();
		print "</body></html>"