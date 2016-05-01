'''************************************************************************
   Class: tab3.py
   Author: Adam Lawson & Evan Hammer
   Description: This file is used in conjuction with ttkNotebook.py
 ************************************************************************'''
from tkinter import *
from tkinter.ttk import *
import sys
import random

class Tab3(Frame):
    def __init__(self, master):
        Frame.__init__(self,master,width = 1000, height=800)
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        self.radioValue = IntVar()
        self.FIFO = Radiobutton(self, text = "FIFO", variable = self.radioValue, value = 1 )#, command = self.radioCallback)
        self.FIFO.grid(row=1, column=1)
        self.optimal = Radiobutton(self, text = "Optimal", variable = self.radioValue, value = 2 )#, command = self.radioCallback)
        self.optimal.grid(row=1, column=2)
        self.LRU = Radiobutton(self, text = "LRU", variable = self.radioValue, value = 3 )#, command = self.radioCallback)
        self.LRU.grid(row=1, column=3)
        self.LFU = Radiobutton(self, text = "LFU", variable = self.radioValue, value = 4 )#, command = self.radioCallback)
        self.LFU.grid(row=1, column=4)
        self.NRU = Radiobutton(self, text = "NRU", variable = self.radioValue, value = 5 )#, command = self.radioCallback)
        self.NRU.grid(row=1, column=5)


        self.numFramesLabel = Label(self, text="Number of Frames")
        self.numFramesLabel.grid(row=2, column=1)
        self.numFramesValue = StringVar()
        self.numFramesEntry = Entry(self, textvariable = self.numFramesValue)
        self.numFramesEntry.grid(row=2, column=2)

        self.numPagesLabel = Label(self, text="Number of Pages")
        self.numPagesLabel.grid(row=2, column=3)
        self.numPagesValue = StringVar()
        self.numPagesEntry = Entry(self, textvariable = self.numPagesValue)
        self.numPagesEntry.grid(row=2, column=4)

        self.numReferenceLabel = Label(self, text="Length of String")
        self.numReferenceLabel.grid(row=3, column=1)
        self.numReferenceValue = StringVar()
        self.numReferenceEntry = Entry(self, textvariable = self.numReferenceValue)
        self.numReferenceEntry.grid(row=3, column=2)

        self.numPageFaultLabel = Label(self, text="Number of Page Faults")
        self.numPageFaultLabel.grid(row=3, column=3)
        self.numPageFaultValue = StringVar()
        self.numPageFaultEntry = Entry(self, textvariable = self.numPageFaultValue)
        self.numPageFaultEntry.grid(row=3, column=4)


        self.generateButton = Button(self, text = "Find Page Faults", command = self.inputCheck)
        self.generateButton.grid(row=4, column=1)



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

        elif self.numReferenceValue.get().isnumeric() == False:
            messagebox.showerror(self.warningLabel, "You must enter a number..")
            return

        elif int(self.numReferenceValue.get()) > 10:
                messagebox.showwarning(self.warningLabel, "Please keep string to less than 20.")
                return
        else:
            self.radioCallback()


    def radioCallback(self):

        #Generate random reference String
        self.referenceString =[]
        topRange = int(self.numReferenceValue.get())
        for i in range( 0, topRange ):
            self.referenceString.append(random.randrange(0, 9))

        if self.radioValue.get() == 1:
            self.drawFIFO()
        elif self.radioValue.get() == 2:
            self.drawOptimal()
        elif self.radioValue.get() == 3:
            self.drawLRU()
        elif self.radioValue.get() == 4:
            self.drawLFU()
        else:
            self.drawNRU()

    def drawFrame( self, frame, refVal, frameValues, color ):

        numFrames = int(self.numFramesValue.get())
        width = 30
        var = width*(numFrames+1)
        canvas = Canvas( frame, width=width, height=var)
        canvas.create_rectangle((4, width, width, var), outline=color)
        canvas.create_text((width/2,width/2), text=refVal, fill=color)
        for i in range( numFrames ):
            canvas.create_text((width/2,width*(i+1)+width/2), text=frameValues[i], fill=color)
            canvas.create_line((4, width*(i+1), width, width*(i+1)), fill=color)
        canvas.pack(side=LEFT)


    def drawFIFO(self):
        self.inner=Frame(self)
        self.inner.grid(columnspan=1000)
        self.drawFrame( self.inner, self.referenceString[0], [1,2,3], "red" )
        self.drawFrame( self.inner, self.referenceString[1], [1,2,3], "black" )
        self.drawFrame( self.inner, self.referenceString[2], [1,2,3], "red" )
        self.drawFrame( self.inner, self.referenceString[3], [1,2,3], "red" )

    def drawOptimal(self):
        print("Optimal")
    def drawLRU(self):
        print("LRU")
    def drawLFU(self):
        print("LFU")
    def drawNRU(self):
        print("NRU")
