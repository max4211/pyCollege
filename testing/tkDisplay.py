'''
Created: 24 August 2019
Author: Max Smith
Goal: Create a utility to read in carefully formatted excel files
'''

import os
import logging
from tkinter import *

log_name = "tkDisp.log"
# Clear logger each time
if os.path.isfile(log_name):
    os.remove(log_name)
logging.basicConfig(filename=log_name, level=logging.INFO)

# TODO Make this log_and_print a global utiliity for whole repo
def log_and_print(message):
    logging.info(message)
    print(message)

'''Keep track of IntVars for checkbox grid'''
def create_intvars(total):
    boxVars = []
    for i in range(total):
        boxVars.append(IntVar())
        boxVars[i].set(0)
    return boxVars

'''Get which boxes are checked'''
def get_selected(boxVars):
    selected = {}
    for i in range(len(boxVars)):
        temp = []
        if (boxVars[i].get() == 1):
            temp.append()

'''Testing out various window options'''
def basic(class_list):
    # Initialize window
    window = Tk()
    window.title("Course Selector")
    window.configure(background="light gray")
    window.geometry("400x500+1000+300")
    # window.resizable(0,0)                 # Option to lock window size
    
    # Create labels
    Label(window, text="Select the courses you would like to take:", bg="black", fg="white", font="none 12").pack()  #.grid(row=1, column=0, sticky=W)
    
    # Init vars to keep track of checkbuttons states
    boxes = []
    boxVars = create_intvars(len(class_list))
    
    # Create list of class buttons
    for i in range(len(class_list)):
        course_info = class_list[i]
        log_and_print(f"course_info: {course_info}")
        # TODO Try to add padding - padx, pady
        c = Checkbutton(window, text=course_info, variable=class_list[i], activeforeground="green")
        c.pack(anchor=W)

    # Run main loop
    window.mainloop()

# TODO Change these list options to more class info
# TODO Create class ID for all checkbox items
class_list = ["COMP 30080", "EEEN 30110", "ECON 30270"]
basic(class_list)