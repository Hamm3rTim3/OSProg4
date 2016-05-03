'''************************************************************************
   Program: Simulation Project
   Author: Adam Lawson & Evan Hammer
   Class: CSC-456
   Instructor: Dr. Jeff McGough
   Date: 5/1/2016
   Description: This GUI program demonstrates 3 main concepts: 1) Various process schedulers (Round Robin, Priority, Shortest Job First) 2) Simulation of the memory magagement unit, TLB, page tables and paging 3) Simulatino of page replacement algorithms (FIFO, Optimal, LRU, LFU, NRU). This program opens with 3 visible tabs for the user to choose from among the 3 simulations. After the user enters in the required information (which the program error checks) and clicks on the 'run' button, the program will display the desired information in a graphic along the bottom of the page.

   Compilation instructions: This program was built using Python 3 and tkinter. To run type the following: python3 ttkNotebook.py.

   Usage: See above under Compilation instructions.

 ************************************************************************'''
from tkinter import *
from tkinter.ttk import *
import sys
from tab1 import Tab1
from tab2 import Tab2
from tab3 import Tab3

#Create main class using the notebook feature which allows for seperate
# modular tabs.
class MyWindow:
    def __init__(self):
        root = Tk()
        root.geometry("1000x400")
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
