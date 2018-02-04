import time 
from threading import Thread

from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=2)

def square(a):
  print("Calculate square numbers\n")
  for i in a:
    time.sleep(0.2)
    print('square: ' + str(i*i))
  return i*i

def cube(a):
  print("Calculate cube numbers\n")
  for i in a:
    time.sleep(0.2)
    print('cube: ' + str(i*i*i))
  return i*i*i

arr = [2,3,8,9]
t = time.time()

t1 = pool.apply_async(square,(arr,))
t2 = pool.apply_async(cube,(arr,))
 
# t1 = Thread(target=square, args=(arr,))
# t2 = Thread(target=cube, args=(arr,))
# t1.start()
# t2.start()

# t1.join()
# t2.join()
print('t1',t1.get())
print('t2',t2.get())

print('The program completed in ',time.time()-t)