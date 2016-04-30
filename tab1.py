from tkinter import *
from tkinter.ttk import *
import sys

class Tab1(Frame):
	def __init__(self, master):
		Frame.__init__(self,master,width = 1000, height=800)
		self.create_widgets()
		self.grid()

	def create_widgets(self):
		self.radioValue = IntVar()
		self.roundRobinRadio = Radiobutton(self, text = "Round Robin", variable = self.radioValue, value = 1, command = self.radioCallback)
		self.roundRobinRadio.grid(row=1, column=1)
		self.roundRobinRadio = Radiobutton(self, text = "Priority", variable = self.radioValue, value = 2, command = self.radioCallback)
		self.roundRobinRadio.grid(row=1, column=2)
		self.roundRobinRadio = Radiobutton(self, text = "Shortest Job First", variable = self.radioValue, value = 3, command = self.radioCallback)
		self.roundRobinRadio.grid(row=1, column=3)

	def helloCallBack(self):
		print("Pushed the Button!!!")
	def radioCallback(self):
		if self.radioValue.get() == 1:
			self.drawRoundRobin()
		elif self.radioValue.get() == 2:
			self.drawPriority()
		else:
			self.drawSJF()
	def drawRoundRobin(self):
		self.inner = Frame(self);
		self.inner.grid(row=2, columnspan=100)
		self.numProcessLabel = Label(self.inner, text="Number of Processes:")
		self.numProcessLabel.pack(side=LEFT)
		self.numProcessValue = StringVar()
		self.numProcessEntry = Entry(self.inner, textvariable = self.numProcessValue)
		self.numProcessEntry.pack(side=LEFT)
		self.timeQuantaValue = StringVar()
		self.timeQuantaLabel = Label(self.inner, text="Time Quanta:")
		self.timeQuantaLabel.pack(side=LEFT)
		self.timeQuantaEntry = Entry(self.inner, textvariable = self.timeQuantaValue)
		self.timeQuantaEntry.pack(side=LEFT)
		self.button = Button(self.inner, text = "Generate Processes", command = self.helloCallBack)
		self.button.pack(side=LEFT)
		
	def drawPriority(self):
		print("Pushed the 2 Radio Button")
	def drawSJF(self):
		print("Pushed the 3 Button!!")