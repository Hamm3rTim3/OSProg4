'''************************************************************************
   Class: tab2.py
   Author: Adam Lawson & Evan Hammer
   Description: This file is used in conjuction with ttkNotebook.py
 ************************************************************************'''
from tkinter import *
from tkinter.ttk import *
import sys

class Tab2(Frame):
    def __init__(self, master):
        Frame.__init__(self,master,width = 1000, height=800)
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        self.numFramesLabel = Label(self, text="Number of Frames")
        self.numFramesLabel.grid(row=1, column=1)
        self.numFramesValue = StringVar()
        self.numFramesEntry = Entry(self, textvariable = self.numFramesValue)
        self.numFramesEntry.grid(row=1, column=2)

        self.numPagesLabel = Label(self, text="Number of Pages")
        self.numPagesLabel.grid(row=1, column=3)
        self.numPagesValue = StringVar()
        self.numPagesEntry = Entry(self, textvariable = self.numPagesValue)
        self.numPagesEntry.grid(row=1, column=4)

        self.numTLBLabel = Label(self, text="TLB Size")
        self.numTLBLabel.grid(row=1, column=5)
        self.numTLBValue = StringVar()
        self.numTLBEntry = Entry(self, textvariable = self.numTLBValue)
        self.numTLBEntry.grid(row=1, column=6)

        self.generateButton = Button(self, text = "Simulate", command = self.inputCheck)
        self.generateButton.grid(row=2, column=1)

    def inputCheck(self):
        self.warningLabel = "Danger, Danger!!!"

        if self.numFramesValue.get().isnumeric() == False or self.numFramesValue.get() is None :
            messagebox.showerror(self.warningLabel, "You must enter a number.")
            return

        elif int(self.numFramesValue.get()) > 10:
            messagebox.showwarning(self.warningLabel, "Please use no more than 10 frames.")
            return

        elif self.numPagesValue.get().isnumeric() == False:
            messagebox.showerror(self.warningLabel, "You must enter a number.")
            return

        elif int(self.numPagesValue.get()) > 20:
                messagebox.showwarning(self.warningLabel, "Please use no more than 20 pages.")
                return

        elif self.numTLBValue.get().isnumeric() == False:
            messagebox.showerror(self.warningLabel, "You must enter a number.")
            return

        elif int(self.numTLBValue.get()) > 10:
                messagebox.showwarning(self.warningLabel, "Please use a size no larger than 20.")
                return
