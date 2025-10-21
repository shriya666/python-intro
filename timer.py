import termios
import time
import os
import sys
choice= input("Normal timer, speech timer, or a stopwatch? ")
if choice=="Normal timer":
    def stopping_time():
        ask= int(input("How long do you want the timer to run? (in secs) "))
        while ask>0:
            time.sleep(1)
            print(ask-1)
            ask-=1
        print("Time's up. ")

    stopping_time()

elif choice=="speech timer":
    def speech_timer():
        print("Starting Now ")
        counter=600
        while counter > -30:
            time.sleep(1)
            print(counter-1)
            counter-=1
            if counter==0:
                print("Time's up. ")
        print("Stop talking. ")

    speech_timer()

def stopwatch():
    print("Type 'q'' to stop. ")
    start= input("Type start to start ")
    counter= 0
    new = termios.tcgetattr(0)
    old = termios.tcgetattr(0)
    
    new[3] = ~(termios.ICANON)
    new[6][termios.VMIN] = 1
    new[6][termios.VTIME] = 0
    termios.tcsetattr(0, termios.TCSANOW, new) 
    os.set_blocking(0, False)

    while start!= "stop":
        x = sys.stdin.read(1)
        if x == 'q':
            break
        time.sleep(1)
        print(counter+1) 
        counter+=1

    termios.tcsetattr(0, termios.TCSANOW, old) 

stopwatch()





