import socket
port = 8000
#host = socket.gethostbyname(socket.gethostname())
host = '127.0.0.1' 
s = socket.socket()


s.bind((host,port))
s.listen(1)

c, addr = s.accept()
print("A client connected")

while True:
	data_c = c.recv(1024)
	if not data_c:
		break
	print("client   : " + str(data_c.decode()))
	data_s = raw_input("Enter reponse : ")
	c.send(data_s.encode())
s.close()
