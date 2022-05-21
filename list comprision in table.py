import threading
import time

class table(threading.Thread):
 def accept(self,a):
  self.a=a
def run(self):
    for i in range(1,11):
        print(self.a,'*',i,'=',self.a*i)
time.sleep(1)

obj=table()
obj.accept(int(input("enter number")))
obj.start()
