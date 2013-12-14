import smtplib

server = smtplib.SMTP('localhost')
server.set_debuglevel(1)
server.sendmail("webmaster@eazyshop.ru", "vgulaev@yandex.ru", "Hello my old friend")
server.quit()