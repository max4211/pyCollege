'''
Created: 28 August 2019
Author: Max Smith
Goal: Create a display to view class scheulde
Notes: Starting off with a single day to display, then will try to repeat the frame n times
'''

from tkinter import *
# import tkinter as tk      # How to do tk.update to get window size
import numpy as np
import logging
import os

log_name = "dispSched.log"
# Clear logger each time
if os.path.isfile(log_name):
    os.remove(log_name)
logging.basicConfig(filename=log_name, level=logging.INFO)

'''Weekly schedule class to display schedule options
Current test is to try adding a single time to a display window'''
class Schedule(Frame):
    # Usefule link: http://effbot.org/tkinterbook/frame.htm
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)

if __name__ == '__main__':
    def log_and_print(message):
        logging.info(message)
        print(message)
    
    def window_geometry(window, window_width, window_height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        log_and_print(f"Screen Dimensions - Width: {screen_width} (pixels), Height: {screen_height} (pixels)")
        log_and_print(f"Desired Window Dimensions -  Width: {window_width} (pixels), Height: {window_height} (pixels)")
        x_corner = int((screen_width/2) - (window_width/2))
        y_corner = int((screen_height/2) - (window_height/2))
        log_and_print(f"Place window corners @ x = {x_corner} (pixels), y = {y_corner} (pixels)")
        return x_corner, y_corner

    '''Input a list of times, output labels in the window'''
    def time_labels(pane, window_height, times):
        # Place labels in a pane
        total_labels = len(times)
        padding = window_height/(3*(total_labels))
        for time in times:
            time_label = Label(pane, text=int(time), bg="white", fg="black", font="none 10 bold")
            # time_label.pack(anchor=W, pady=padding)
            time_label.pack(anchor=W, pady=padding, expand=False)

    '''Enter class information, output a display on the window'''
    def class_slot(window, start_time, end_time, title):
        log_and_print(f"Attempting to create a class slot in window")
        # Create label with appropriate labels and coloring
        class_box = Label(window, text=title, bg="blue", fg="white", font="none 10")
        # Configure label appropriately in the screen
        # NOTE Frames may make this process MUCH easier
        class_box.pack(side=TOP)

    def excel_to_time(time):
        decimal_time = time * 24            # Form HH.HHH
        return decimal_time

    def readable_time(time, military):
        # TODO Incorporate non military time (e.g. 1:00 PM instead of 13:00)
        if time < 1:                        # Raw excel form, convert first
            time = excel_to_time(time)
        hours = int(time)
        minutes = (time * 60) % 60
        seconds = (time * 3600) % 60
        text_time = ("%d:%02d.%02d" % (hours, minutes, seconds))
        print(f"Readable time: {text_time}")
        return(text_time, hours, minutes, seconds)

    '''Assumed time format: decimal less than one'''
    def time_to_decimal(hours, minutes, seconds):
        # TODO Incorporate non military (change to military from PM)
        # NOTE For now - just asssumed to always be military
        # (e.g., 12:00 --> 0.5)
        return hours/24 + minutes/60 + seconds/3600
    
    # TODO Configure window here
    window = Tk()

    # Configure root here
    window.title("Weekly Schedule")
    window.configure(background="light gray")
    # Get screen width and height to open in center of screen
    window_width, window_height = 300, 700
    x_corner, y_corner = window_geometry(window, window_width, window_height)
    window.geometry(f"{window_width}x{window_height}+{x_corner}+{y_corner}")

    # Create a top frame to fill in
    top_frame = Frame(window, width=window_width, height=window_height)
    top_frame.pack(side=TOP, fill=X, expand=True, anchor=N)

    # Create header for each day of the week
    week_days = ["Monday", "Tuesday", "Wedesday", "Thursday", "Friday", "Saturday", "Sunday"]
    header = Label(top_frame, text=week_days[0], bg="white", fg="black", font="none 12 bold")
    header.pack()

    # Create time axis scale (every hour?)
    start_time, stop_time = 8, 17
    num_points = stop_time - start_time + 1
    time_military = np.linspace(start_time, stop_time, num_points)
    time_decimal = []
    for time in time_military:
        decimal_time = time_to_decimal(hours=time, minutes=0, seconds=0)
        log_and_print(f"Military Time: {time}, Decimal Time: {decimal_time}")
        time_decimal = np.append(time_decimal, decimal_time)

    log_and_print(f"Length of time_decimal: {len(time_decimal)}")

    # Create labels on a pane in the windows
    # pane = Frame(window)
    # pane.pack(fill = NONE, expand = False)
    time_frame_width = 20
    time_frame = Frame(top_frame, width=time_frame_width, height=window_height, background="black")
    time_frame.pack(side=LEFT, anchor=W)
    time_labels(time_frame, window_height, times=time_military)

    # Add a single course time to the day
    start_time = 0.34
    end_time = 0.375
    message = "COMP 30080 (8 AM - 9 AM)"
    class_frame = Frame(top_frame, width=window_width-time_frame_width, height=window_height, background="light blue")
    class_frame.pack(side=LEFT, anchor=W)
    # class_slot(window, start_time, end_time, message)

    window.mainloop()
