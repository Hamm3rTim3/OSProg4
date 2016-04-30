
from tkinter import *
from tkinter.ttk import *
import sys
from tab1 import Tab1
from tab2 import Tab2
from tab3 import Tab3

class MyWindow:
    def __init__(self):
        root = Tk()
        root.title("GUI Prog 4")
        notebook = Notebook(root)

        tab1 = Tab1(notebook)
        tab2 = Tab2(notebook)
        tab3 = Tab3(notebook)
        notebook.add(tab1, text="TAB 1")
        notebook.add(tab2,text="TAB 2")
        notebook.add(tab3,text="TAB 3")
        
        notebook.pack()
        
        root.mainloop()  

def main():
    window = MyWindow()
  
main()