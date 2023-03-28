from tkinter import *
import  datetime
import time
import winsound
def alarm(set_alarm):
    while True:
        time.sleep(1)
        current_time=datetime.datetime.now()
        now=current_time.strftime("%H:%M:%S")
        date=current_time.strftime("%d/%m/%Y")
        print("The set date is : ",date)
        print(now)
        if now==set_alarm:
            print("Time to wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break
