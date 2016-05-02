'''************************************************************************
   Class: tab2.py
   Author: Adam Lawson & Evan Hammer
   Description: This file is used in conjuction with ttkNotebook.py
 ************************************************************************'''
from tkinter import *
from tkinter.ttk import *
import sys
import random

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

        elif int(self.numFramesValue.get()) > 20:
            messagebox.showwarning(self.warningLabel, "Please use no more than 20 frames.")
            return

        elif self.numPagesValue.get().isnumeric() == False:
            messagebox.showerror(self.warningLabel, "You must enter a number.")
            return

        elif int(self.numPagesValue.get()) > int(self.numFramesValue.get()):
                messagebox.showwarning(self.warningLabel, "Please use no more pages than frames.")
                return

        elif self.numTLBValue.get().isnumeric() == False:
            messagebox.showerror(self.warningLabel, "You must enter a number.")
            return

        elif int(self.numTLBValue.get()) > 20:
                messagebox.showwarning(self.warningLabel, "Please use a size no larger than 20.")
                return
        else:
            self.simulateTLB()
    def simulateTLB(self):
        self.inner = Frame(self)
        self.inner.grid(columnspan = 10)
        self.label = Label(self.inner, text="Effective Access Time: ")
        self.label.grid(row=1, column=0)
        self.EATLabel = Label(self.inner)
        self.EATLabel.grid(row=1, column=1)
        self.stopButton = Button(self.inner, text="Stop Simulation", command=self.stopSimulation)
        self.stopButton.grid(row=1, column=2)
        self.TLBLabel = Label(self.inner, text="TLB")
        self.TLBLabel.grid(row=2, column=0, columnspan=2)
        self.pagesLabel = Label(self.inner, text = "Page Table")
        self.pagesLabel.grid(row=2, column=3)
        self.frameLabel = Label(self.inner, text="Frames")
        self.frameLabel.grid(row=2, column=5)
        self.TLBPageBox = Listbox(self.inner)
        self.TLBPageBox.grid(row=3,column=0, rowspan=int(self.numTLBValue.get()), sticky=(N+E))
        self.TLBFrameBox = Listbox(self.inner)
        self.TLBFrameBox.grid(row=3,column=1, rowspan=int(self.numTLBValue.get()), sticky=(N+W))
        self.frames, self.pages = self.randomFrameNumber()
        self.pagesBox = Listbox(self.inner)
        for i in range(len(self.pages)):
            self.pagesBox.insert(i, self.pages[i])
        self.pagesBox.grid(row=3, column=3, rowspan=len(self.pages), sticky=N)
        self.frameBox = Listbox(self.inner)
        for i in range(len(self.frames)):
            self.frameBox.insert(i, self.frames[i])
        self.frameBox.grid(row=3,column=5, rowspan=len(self.frames), sticky=N)
        self.initTLB(int(self.numTLBValue.get()))
        self.simulateMemAccess(len(self.pages))
    def initTLB(self, tlbSize):
        self.TLB = [["~","~"]]*tlbSize
        print(self.TLB)
        for i in range(len(self.TLB)):
            self.TLBPageBox.insert(i, self.TLB[i][0])
            self.TLBFrameBox.insert(i, self.TLB[i][1])
    def simulateMemAccess(self, numPages):
        memAccess = random.randrange(0,numPages)

    def stopSimulation(self):
        try:
            self.inner.after_cancel(self.afterId)
        except(NameError, AttributeError):
            print("Uh, Oh!!")
            pass
    def randomFrameNumber(self):
        frameList = ["Used"]*int(self.numFramesValue.get())
        pages = []
        for i in range(int(self.numPagesValue.get())):
            rand = random.randrange(0,len(frameList))
            while(frameList[rand] != "Used"):
                rand = random.randrange(0,len(frameList))
            frameList[rand] = i
            pages.append(rand)
        return frameList, pages










