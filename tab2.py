'''************************************************************************
   Class: tab2.py
   Author: Adam Lawson & Evan Hammer
   Description: This file is used in conjuction with ttkNotebook.py. This
   tab generates and displays all of the algorithms in regards to using
   memory management and showing TLBs. It also displays the actual hit/miss
   ratio of memory accesses.
 ************************************************************************'''
from tkinter import *
from tkinter.ttk import *
import sys
import random

#Create frame for this tab.
class Tab2(Frame):
    def __init__(self, master):
        Frame.__init__(self,master,width = 1000, height=800)
        self.create_widgets()
        self.grid()

	#Create the labels and button needed for simulations.
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

	#Checking the input for invalid or not enough data.
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
		#If data is valid then run simulation.
        else:
            self.simulateTLB()

	#Simulation method.
    def simulateTLB(self):
		#This redraws the window by removing the parent and child elements
		#for when user wants to run an additional simulation.
        try:
            try:
                for elem in self.inner.winfo_children():
                    elem.destroy()
            except(NameError, AttributeError):
                pass
            self.inner.destroy()
        except (NameError, AttributeError):
            pass

		#Palcing of labels for hit/misses/boxes for showing memory data.
        self.TLBWaitTime = 100
        self.MemWaitTime = 500
        self.inner = Frame(self)
        self.inner.grid(columnspan = 10)
        self.label = Label(self.inner, text="Effective Access Time: ")
        self.label.grid(row=1, column=0)
        self.EATLabel = Label(self.inner)
        self.EATLabel.grid(row=1, column=1)
        self.stopButton = Button(self.inner, text="Stop Simulation", command=self.stopSimulation)
        self.stopButton.grid(row=1, column=2)
        self.label = Label(self.inner, text="Page Number:")
        self.label.grid(row=1, column=3)
        self.PageNumberLabel = Label(self.inner, text="Run")
        self.PageNumberLabel.grid(row=1, column=4)
        self.TLBHitLabel = Label(self.inner, text="TLB Hits:")
        self.TLBHitLabel.grid(row=1, column=5)
        self.TLBLabel = Label(self.inner, text="TLB")
        self.TLBLabel.grid(row=2, column=0, columnspan=2)
        self.pagesLabel = Label(self.inner, text = "Page Table")
        self.pagesLabel.grid(row=2, column=3)
        self.frameLabel = Label(self.inner, text="Frames")
        self.frameLabel.grid(row=2, column=5)
        self.TLBPageBox = Listbox(self.inner, height=int(self.numTLBValue.get()))
        self.TLBPageBox.grid(row=3,column=0, sticky=(N+E))
        self.TLBFrameBox = Listbox(self.inner, height=int(self.numTLBValue.get()))
        self.TLBFrameBox.grid(row=3,column=1, sticky=(N+W))
        self.frames, self.pages = self.randomFrameNumber()
        self.pagesBox = Listbox(self.inner, height=len(self.pages))

        for i in range(len(self.pages)):
            self.pagesBox.insert(i, self.pages[i])

        self.pagesBox.grid(row=3, column=3, sticky=N)
        self.frameBox = Listbox(self.inner, height=len(self.frames))

        for i in range(len(self.frames)):
            self.frameBox.insert(i, self.frames[i])

        self.frameBox.grid(row=3,column=5, sticky=N)
        self.initTLB(int(self.numTLBValue.get()))
        self.numPages = len(self.pages)
        self.EATLabel.config(text="0")
        self.TLBHit = 0
        self.TotalAccess = 0
        self.simulateMemAccess()

	#Set up TLB box.
    def initTLB(self, tlbSize):
        self.TLBpages = ["~"]*tlbSize
        self.TLBframes= ["~"]*tlbSize
        self.TLBage = [0]*tlbSize

        for i in range(tlbSize):
            self.TLBPageBox.insert(i, self.TLBpages[i])
            self.TLBFrameBox.insert(i, self.TLBframes[i])

	#Showing the simulated access times.
    def simulateMemAccess(self):
        self.inTLB = False
        self.pageNumber = random.randrange(0,self.numPages)
        self.PageNumberLabel.config(text=str(self.pageNumber))
        self.afterId = self.inner.after(100, self.findInTLB)

	#Searching within the TLB.
    def findInTLB(self):
        self.TLBage = [x+1 for x in self.TLBage]
        self.TotalAccess += 1

        try:
            self.TLBindex = self.TLBpages.index(self.pageNumber)
            #change the background of the item to green for found
            self.TLBPageBox.itemconfig(self.TLBindex, bg="green")
            self.TLBFrameBox.itemconfig(self.TLBindex, bg="green")
            self.frame = self.TLBframes[self.TLBindex]
            self.inTLB = True
            self.TLBHit +=1
			#Dislaying the TLB hits.
            self.TLBHitLabel.config(text = "TLB Hits: " + str(self.TLBHit)+"/"+str(self.TotalAccess))
            self.afterId = self.inner.after(self.TLBWaitTime, self.findInMemory)

		#If not in TLB then color red to show a miss.
        except(ValueError):
            for i in range(len(self.TLBframes)):
                self.TLBFrameBox.itemconfig(i,bg="red")
                self.TLBPageBox.itemconfig(i,bg="red")
            self.TLBHitLabel.config(text = "TLB Hits: " + str(self.TLBHit)+"/"+str(self.TotalAccess))
            self.afterId = self.inner.after(self.MemWaitTime, self.findInPageTable)

	#If not in TLB than look in memory.
    def findInMemory(self):
        #color item green
        self.frameBox.itemconfig( self.frame, bg="green")
        self.afterId =  self.inner.after(self.MemWaitTime, self.clearMemAccess)

	#Looking in page table, shoing green where found.
    def findInPageTable(self):
        #color item green
        self.pagesBox.itemconfig(self.pageNumber, bg="green")
        self.frame = self.pages[self.pageNumber]

        if not self.inTLB:
            pos = 0
            oldest = 0
            for i in self.TLBage:
                if i > oldest:
                    oldest = i
                    pos = self.TLBage.index(i)
            self.TLBage[pos] = 0
            self.TLBpages[pos] = self.pageNumber
            self.TLBframes[pos] = self.pages[self.pageNumber]
            self.TLBPageBox.delete(pos)
            self.TLBPageBox.insert(pos, self.pageNumber)
            self.TLBFrameBox.delete(pos)
            self.TLBFrameBox.insert(pos, self.pages[self.pageNumber])
        self.afterId = self.inner.after(self.MemWaitTime, self.findInMemory)

	#Clear the access to allow for additional acccesses.
    def clearMemAccess(self):
        hitPercent = self.TLBHit/self.TotalAccess
        EAT = 120*hitPercent + 220 * (1-hitPercent)
        self.EATLabel.config(text = ("%.2f"%EAT)+"ms")
        if not self.inTLB:
            for i in range(len(self.TLBframes)):
                self.TLBFrameBox.itemconfig(i,bg="white")
                self.TLBPageBox.itemconfig(i,bg="white")
            self.pagesBox.itemconfig(self.pageNumber, bg="white")
            self.frameBox.itemconfig(self.frame, bg="white")
        else:
            self.TLBPageBox.itemconfig(self.TLBindex,bg="white")
            self.TLBFrameBox.itemconfig(self.TLBindex, bg="white")
            self.frameBox.itemconfig(self.frame, bg="white")
        self.afterId = self.inner.after(self.TLBWaitTime, self.simulateMemAccess)

	#User can stop simulation anytime by cliking the stop button.
    def stopSimulation(self):
        try:
            self.inner.after_cancel(self.afterId)
        except(NameError, AttributeError):
            pass

	#Generating random frames numbers to simulate an actual system.		
    def randomFrameNumber(self):
        frameList = ["Used"]*int(self.numFramesValue.get())
        pages = []

        for i in range(int(self.numPagesValue.get())):
            rand = random.randrange(0,len(frameList))
            while(frameList[rand] != "Used"):
                rand = random.randrange(0,len(frameList))
            frameList[rand] = "Page " + str(i)
            pages.append(rand)

        return frameList, pages
