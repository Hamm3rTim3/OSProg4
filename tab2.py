from tkinter import *
from tkinter.ttk import *
import sys

class Tab2(Frame):
    def __init__(self, master):
        Frame.__init__(self,master,width=500, height=300)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
    	self.canvas = Canvas(self, width=1000, height=800)
    	self.fillCanvas()
    	self.canvas.pack()
    def fillCanvas(self):
    	self.canvas.create_line(0,0,200,100)
    	self.canvas.create_rectangle((150, 150, 250, 250))

    def helloCallBack(self):
    	print("Pushed the Button!!!")
