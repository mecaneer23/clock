#!/usr/bin/env python3

from tkinter import Tk, ttk, StringVar
from time import strftime

root = Tk()
root.title("Clock")

formatted_time = StringVar()
clock = ttk.Label(root, textvariable=formatted_time, font=("arial", 40), background="black", foreground="white")
clock.pack()

def update_time():
    formatted_time.set(strftime("%I:%M:%S %p"))
    clock.after(1000, update_time)

update_time()
root.mainloop()
