#client side code

import socket
host = '127.0.0.1'
port = 8000

s = socket.socket()
s.connect((host, port))
i = raw_input("Enter data  : ")

while i != 'exit':
	s.send(i.encode())
	j = s.recv(1024)
	j = j.decode()
	print("From Server : " + j)
	i = raw_input("Enter data  : ")

s.close()

