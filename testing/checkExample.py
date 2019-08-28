'''
Created: 28 August 2019
Author: Max Smith
Goal: Create a utility to display schedule options
'''

## Checkbox Example from Python Course
# https://www.python-course.eu/tkinter_checkboxes.php
# Adapting this code to my needs

#!/usr/bin/python3

from tkinter import *

'''Choices class to toggle options on and off'''
class Choices(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        
        Frame.__init__(self, parent)
        self.vars = []
        self.picks = picks

        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars.append(var)

    # Return map of check box states
    def state(self):
        return map((lambda var: var.get()), self.vars)



if __name__ == '__main__':
    # TODO Configure root window here
    root = Tk()
    
    # Configure what goes into boxes here
    # TODO Get class list from excel read dictionary
    class_list = ["COMP 30080", "EEEN 30110", "ECON 30270"]
    option_list = ['Analytics','View Only']
    # Create check box sections
    lng = Choices(root, picks=class_list) #, header="Class List")
    tgl = Choices(root, picks=option_list) #, header="Options")
    # Orient check boxes
    lng.pack(side=TOP,  fill=X)
    tgl.pack(side=LEFT)
    lng.config(relief=GROOVE, bd=2)

    # Function to parse states and picks, print results from peek
    def printresults(header, states, picks):
        print(f"Category: {header}")
        for i in range(len(states)):
            print(f"Choice: {picks[i]}, State: {states[i]}")

    # Function to print states of all checkboxes
    def allstates():
        printresults("Class List", list(lng.state()), lng.picks) 
        printresults("Options", list(tgl.state()), tgl.picks) 

    Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
    # TODO Change peek from a submit esque function to a queue that places info when states change
    Button(root, text='Peek', command=allstates).pack(side=RIGHT)
    root.mainloop()