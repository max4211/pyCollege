'''
Created: 28 August 2019
Author: Max Smith
Goal: Create a display to view class scheulde
Notes: Starting off with a single day to display, then will try to repeat the frame n times
'''

from tkinter import *

'''Weekly schedule class to display schedule options'''
class Schedule(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)

if __name__ == '__main__':
    def screen_dimensions(width, height):
        print(f"Screen Dimensions:\nWidth: {width} (pixels), Height: {height} (pixels)")

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
    def time_to_decimal(hour, minutes):
        # TODO Incorporate non military (change to military from PM)
        # NOTE For now - just asssumed to always be military
        # (e.g., 12:00 --> 0.5)
        


        pass


    
    # TODO Configure window here
    window = Tk()

    # Get screen width and height to open in center of screen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    screen_dimensions(screen_width, screen_height)

    # Configure root here
    window.title("Weekly Schedule")
    window.configure(background="light gray")
    # TODO Verify this is where we want the window
    window.geometry(f"400x500+{int(screen_width/4)}+{int(screen_height/4)}")

    # Create header for each day of the week
    week_days = ["Monday", "Tuesday", "Wedesday", "Thursday", "Friday", "Saturday", "Sunday"]
    header = Label(window, text=week_days[0], bg="white", fg="black", font="none 12 bold")
    header.pack()

    # Create time axis scale (every hour?)


    window.mainloop()
