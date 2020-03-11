import threading

def square(num):
  print(num*num)
def cube(num):
  print(num*num*num)
t1 = threading.Thread(target=square,args=(10,))
t2 = threading.Thread(target=cube,args=(5,))
t1.start()
t2.start()
