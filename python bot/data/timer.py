import os
import threading 
def mytimer(): 
   print("timer end\n") 
   os.system("xdg-open alarm.mp3")
x=int(input("enter a time in sec "))
my_timer = threading.Timer(x, mytimer) 
my_timer.start() 
print("timer start\n")
