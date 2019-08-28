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
    header = Label(window, text="Select the courses you would like to take:", bg="white", fg="black", font="none 12 bold")
    header.pack()
    
    # Init vars to keep track of checkbuttons states
    boxes = []
    boxVars = create_intvars(len(class_list))
    
    # Create list of class buttons
    # TODO Create ID system
    id_list = []
    last_id = 0
    for i in range(len(class_list)):
        course_info = class_list[i]
        course_id = (course_info + " (" + str(last_id) + ")")
        id_list.append(course_id)
        last_id += 1
        log_and_print(f"Adding button with label: {course_info}")
        # TODO Try to add padding - padx, pady
        c = Checkbutton(window, text=course_info, variable=course_id, activeforeground="green")
        c.pack(anchor=W)

    # Create submit button
    submit = Button(window, text="SUBMIT", bg="white", fg="black", font="none 10 bold", command=get_input(id_list))
    submit.pack()

    # Run main loop
    window.mainloop()

'''After the user makes selections and hits submit, gather info'''
def get_input(id_list):
    for i in range(len(id_list)):
        state = 0 # id_list[i].get()
        log_and_print(f"State of {id_list[i]} is {state}")

# TODO Change these list options to more class info
# TODO Create class ID for all checkbox items
class_list = ["COMP 30080", "EEEN 30110", "ECON 30270"]
basic(class_list)