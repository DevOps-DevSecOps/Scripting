# """ CLIENT """ #
import socket
p=socket.socket()
port=5678
host='127.0.0.1'
p.connect((host,port))

print p.recv(1024)
p.send('hai server')

text=p.recv(1024*1500)
f=open('F:\Python\Pratice\Atom.exe','wb')
f.write(text)
f.close()


# """ SERVER """ #
import socket
s=socket.socket()
port=5678
host='127.0.0.1'
s.bind((host,port))

file=open('F:\Python\Atom 32bit.exe','rb')
text=file.read()
file.close()

s.listen(5)
while True:

	a,host=s.accept()
	print 'connection established'
	a.send('hi client')
	print a.recv(1024)

	a.send(text)
	a.close()

	inp=input('enter some thing to terminate: \n')
	if inp=='exit':
		break
	else:
		continue


# """ SMTP """ #
import smtplib

sypder = 'aruntheja94@gmail.com'
gambler = 'aruntheja9494@gmail.com'

msg = 'hai how are you'
print('message has been sent')

username = 'aruntheja9394@gmail.com'
password = 'Admin@1994'
print('login successfully')

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(sypder, gambler, msg)
server.quit()
