# -*- coding: utf-8 -*-
import initdb

initdb.doinitdb()

#print("Привет!")
if (os.environ.get('C9_USER') == None):
	os.environ['C9_USER'] = "root"
print(os.environ.get('C9_USER'))