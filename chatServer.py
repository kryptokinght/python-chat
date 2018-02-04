import socket
from threading import Thread
from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=2)

def receive(clientSocket) :
	print("receive started")
	while True:
		data_c = clientSocket.recv(1024)
		print("client   : " + str(data_c.decode()))
		if str(data_c.decode()) == 'exit':
			break
		


def respond(clientSocket) :
	while True:
		data_s = raw_input()
		clientSocket.send(data_s.encode())
		if not clientSocket:
			break

port = 8001
#host = socket.gethostbyname(socket.gethostname()) -for localhost only(172.0.1.1 or 172.0.0.1)
#host =  '192.168.0.103' for devices connected on LAN
host = '' #for all which includes localhost and  devices connected on a LAN(Eg: wifi)

s = socket.socket()
s.bind((host,port)) #takes in a tuple (host,port)
s.listen(1)

clientSocket, clientAddr = s.accept()
print("A client connected")
print(clientAddr)

t1 = Thread(target=receive, args=(clientSocket,))
t2 = Thread(target=respond, args=(clientSocket,))
t1.start()
t2.start()

t1.join()
print("Exited receive")
t2.join()
print("Exited response")
s.close()
#program end

# while True:
# 	data_c = clientSocket.recv(1024)
# 	if not data_c:
# 		break
# 	print("client   : " + str(data_c.decode()))
# 	data_s = raw_input("Enter reponse : ")
# 	clientSocket.send(data_s.encode())



