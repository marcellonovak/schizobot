from tkinter import *
from tkinter import messagebox
import string
import random
import keyboard
from keyboard import press
import time

window = Tk()

labelFrame = LabelFrame(window, text = "Seizure Bot 1.1", highlightthickness= 10)
labelFrame.pack(fill = "both", expand = "yes")

padAmount = 5

charText =        Label(labelFrame, text = "Characters:")
charText.grid     (row = 0, column = 0, sticky="w", padx = padAmount, pady = padAmount)
charEntry =       Entry(labelFrame, bd = 5)
charEntry.grid    (row = 0, column = 1, sticky="w", padx = padAmount, pady = padAmount)

repeatText =      Label(labelFrame, text = "Repetitions: ")
repeatText.grid   (row = 1, column = 0, sticky="w", padx = padAmount, pady = padAmount)
repeatEntry =     Entry(labelFrame, bd = 5)
repeatEntry.grid  (row = 1, column = 1, sticky="w", padx = padAmount, pady = padAmount)

timeText =        Label(labelFrame, text = "Fuse Sec: ")
timeText.grid     (row = 2, column = 0, sticky="w", padx = padAmount, pady = padAmount)
timeEntry =       Entry(labelFrame, bd = 5)
timeEntry.grid    (row = 2, column = 1, sticky="w", padx = padAmount, pady = padAmount)

def buttonAction ():
    buffer =  int(timeEntry.get())
    repeats = int(charEntry.get())
    length =  int(charEntry.get())

    time.sleep(buffer)
    for x in range (repeats):
        for x in range (length):
            keyboard.write(random.choice(string.ascii_letters))
        press('enter')
        time.sleep(0.5)
    

testButton = Button(labelFrame, text = "Schizophrenia", command = buttonAction)
testButton.grid (row = 3, column = 0, sticky="w", padx = padAmount, pady = padAmount)

window.mainloop()