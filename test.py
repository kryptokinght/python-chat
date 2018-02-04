import sys
from threading import Thread
from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=1)

def kill():
	ask = raw_input()
	while ask != 'exit':
		ask = raw_input()
	return

t1 = Thread(target=kill)
t1.start()
t1.join()
print("Program end!")