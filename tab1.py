from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from time import sleep
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

	def generateProcNoPriority(self):
		self.warningLabel = "Danger, Danger!!!"
		if self.numProcessValue.get().isnumeric() == False:
			messagebox.showerror(self.warningLabel,self.numProcessValue.get() + " is not a number.")
			return
		if self.timeQuantaValue.get().isnumeric() == False:
			messagebox.showerror(self.warningLabel, self.timeQuantaValue.get() + " is not a number.")
		if int(self.numProcessValue.get()) > 10:
			messagebox.showwarning(self.warningLabel, "Please use a smaller number of processes. Please use less than 10 processes.")
			return

		self.processWindow = Frame(self)
		self.processWindow.grid(row=3, columnspan=100, rowspan=100)
		self.processList = []
		self.processListLabel = []
		self.processListValue = []
		for i in range(int(self.numProcessValue.get())):
			self.processListLabel.append(Label(self.processWindow, text="P"+str(i+1)))
			self.processListLabel[i].grid(row=i, column=0)
			self.processListValue.append(StringVar())
			self.processList.append(Entry(self.processWindow, textvariable=self.processListValue[i]))
			self.processList[i].grid(row=i, column=1)
		self.simulateButton = Button(self.processWindow, text="Simulate", command=self.simulateRoundRobin)
		self.simulateButton.grid(row = int(self.numProcessValue.get()), columnspan=2)
		ganttRow = int(self.numProcessValue.get())+1
		self.ganttChart = Canvas(self.processWindow, width=800,height=40)
		self.ganttChart.grid(row = ganttRow, columnspan=100)
		self.ganttChart.create_rectangle((5, 5, 800, 40))

	def radioCallback(self):
		if self.radioValue.get() == 1:
			self.drawRoundRobin()
		elif self.radioValue.get() == 2:
			self.drawPriority()
		else:
			self.drawSJF()
	def drawRoundRobin(self):
		self.inner = Frame(self)
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
		self.button = Button(self.inner, text = "Generate Processes", command = self.generateProcNoPriority)
		self.button.pack(side=LEFT)
		
	def drawPriority(self):
		print("Pushed the 2 Radio Button")
	def drawSJF(self):
		print("Pushed the 3 Button!!")
	def simulateRoundRobin(self):
		if self.checkProcessInput() is False:
			return
		self.unit = 795/self.totalTime
		self.timeQuanta = int(self.timeQuantaValue.get())
		currentProcess = 0
		prevProcess = -1
		processLines = []
		totalProcesses = int(self.numProcessValue.get())
		for i in range(self.totalTime):
			if (i % self.timeQuanta) == 0 or self.processTime[currentProcess] == 0:
				currentProcess = (currentProcess + 1) % totalProcesses
			elif currentProcess == prevProcess:
				self.ganttChart.remove(processLines[i-1])
				processLines.append(self.ganttChart.create_line((5+(i*self.unit), 5, (5+(i*self.unit), 40))))
				self.processTime[currentProcess] = int(self.processTime[currentProcess]) - 1
			else:
				processLines.append(self.ganttChart.create_line((5+(i*self.unit), 5, (5+(i*self.unit), 40))))
				self.processTime[currentProcess] = int(self.processTime[currentProcess]) - 1
				self.ganttChart.create_text((10+(i*self.unit), 10), text="P"+str(currentProcess+1))
			sleep(1)
	def checkProcessInput(self):
		self.totalTime = 0
		self.processTime = []
		for i in range(int(self.numProcessValue.get())):
			cpuBurst = self.processListValue[i].get()
			self.processTime.append(int(cpuBurst))
			if cpuBurst.isnumeric() == False or int(cpuBurst) < 1:
				messagebox.showwarning(self.warningLabel, "Please enter a valid CPU burst time")
				return False
			else:
				self.totalTime += int(cpuBurst)
		return True