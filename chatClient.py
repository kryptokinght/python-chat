#client side code
#encode and decode() converts it to binary from string/from binary to string

import socket
from threading import Thread
import sys
host = '192.168.0.103'
port = 8001
flag = 0
s = socket.socket()

def respond(s):
	i = raw_input("Enter data  : ")
	while i != exit:
		s.send(i.encode())
		i = raw_input()
		if i == 'exit':
			sys.exit()
def receive(s):
	j = s.recv(1024)
	while j.decode() != 'exit':
		j = j.decode()
		print("From Server : " + j)
		j = s.recv(1024)

#connecting to 192.168.0.103:8003 where the chatServer is located
s.connect((host, port))
t1 = Thread(target=respond, args=(s,))
t2 = Thread(target=receive, args=(s,))
t1.start()
t2.start()
t1.join()
print("Exited receive")
t2.join()
print("Exited response")
s.close()

