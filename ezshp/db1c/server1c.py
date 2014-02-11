import suds
client = suds.client.Client("http://127.0.0.1/USODev2014/ws/restservice.1cws?wsdl", location = "http://127.0.0.1/USODev2014/ws/restservice.1cws")
client.set_options(cache=suds.cache.DocumentCache())
client.service.helloword()
