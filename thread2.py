from threading import Thread
def satya():
  for x in range(5):
    print("hi satya")
def murali():
  for y in range(5):
     print("hi murali")
t1 = Thread(target=satya)
t2 = Thread(target=murali)
t1.start()
t2.start()
