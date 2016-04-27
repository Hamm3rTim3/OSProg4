from Tkinter import *
from ttk import *
import sys

class Tab3(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.create_widgets()

    def create_widgets(self):
        self.button = Button(self, text = "another button", command = self.buttonCallback)
        self.button.pack()
    def buttonCallback(self):
    	print("Pushed tab3 button")