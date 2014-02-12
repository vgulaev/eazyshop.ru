# -*- coding: utf-8 -*-
import suds

def remoteserver():
	#client = suds.client.Client("http://127.0.0.1/USODev2014/ws/restservice.1cws?wsdl", location = "http://127.0.0.1/USODev2014/ws/restservice.1cws")
	client = suds.client.Client("http://89.250.147.200:40080/USODev2014/ws/restservice.1cws?wsdl", location = "http://89.250.147.200:40080/USODev2014/ws/restservice.1cws")
	client.set_options(cache=suds.cache.DocumentCache())
	return client.service
