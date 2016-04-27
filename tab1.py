from Tkinter import *
from ttk import *
import sys

class Tab1(Frame):
    def __init__(self, master):
        Frame.__init__(self,master,width = 500, height=300)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.button = Button(self, text = "Clear", command = self.helloCallBack)
        self.button.grid(row = 1, column = 1)

    def helloCallBack(self):
    	print("Pushed the Button!!!")
