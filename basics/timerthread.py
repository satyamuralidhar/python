import threading
def satya():
  print("hi satya")
def murali():
  print("hi murali")
t1 = threading.Timer(5,satya)
t2=threading.Timer(2,murali)
t1.start()
t2.start()
