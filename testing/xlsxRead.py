'''
Created: 24 August 2019
Author: Max Smith
Goal: Create a utility to read in carefully formatted excel files
'''

# TODO Test lightweight file type - csv?

import os
from pathlib import Path
import logging
import xlrd

log_name = "dataRead.log"
# Clear logger each time
if os.path.isfile(log_name):
    os.remove(log_name)
logging.basicConfig(filename=log_name, level=logging.INFO)

def check_directory(directory):
    logging.info(f"Verifying directory {directory} exists")
    if os.path.exists(directory):
        logging.info(f"Path exists")
    else:
        os.mkdir(directory)
        logging.debug(f"Just created directory: {directory}")

def check_file(inpath):
    logging.info(f"Verifying file - {inpath} - exists")
    if os.path.isfile(inpath):
        logging.info(f"File exists")
    else:
        logging.debug(f"File - {inpath} - does not exist, make and try again :)")

def log_and_print(message):
    logging.info(message)
    print(message)

def extract_col(sheet):
    message = "Extracting all rows column headers from this sheet"
    log_and_print(message)
    for i in range(sheet.ncols):
        print(sheet.cell_value(0, i))

def sheet_stats(sheet):
    message = "Generating statistics on sheet dimensions"
    log_and_print(message)
    col_num = sheet.ncols
    row_num = sheet.nrows
    message = (f"Rows: {row_num}, Cols: {col_num}")
    log_and_print(message)
    return (row_num, col_num)

def class_info(sheet, row):
    message = "Pulling class info"
    log_and_print(message)
    header = []
    data = []
    # Extract info to keep
    for i in range(sheet.ncols):
        header.append(sheet.cell_value(0, i))
        data.append(sheet.cell_value(row, i))
    message = (f"Header Length: {len(header)}, Data Length: {len(data)}")
    log_and_print(message)
    return header, data

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

class Course(object):
    # Declare course variables
    def __init__(self, days, start_times, end_times, class_type):
        if days is None:
            days = []
        if start_times is None:
            start_times = []
        if end_times is None:
            end_times = []
        if class_type is None:
            class_type = []

def class_dict(header, data, convert_time, military):
    # Initialize empty data stores to hold class information
    # TODO Should these be sets or lists?
    days, start_times, end_times, class_type = [], [], [], []
    UCD_num, course_name, Duke_num, grading = "", "", "", ""

    # Parse sheet data and populate elements
    for i in range(len(header)):
        i_type = header[i]
        cell_info = data[i]
        # Skip over empty information (not all classes have same number of meeting times)
        if cell_info == "":
            pass
        else:
            if (i_type == "Day"):
                days.append(cell_info)
            elif (i_type == "Type"):
                class_type.append(cell_info)

            # NOTE Excel form likely very useful for computation
            elif (i_type == "Start Time"): 
                if convert_time:
                    time_info, hours, minutes, seconds = readable_time(cell_info, military)
                else:
                    time_info = cell_info
                start_times.append(time_info)
            elif (i_type == "End Time"):
                if convert_time:
                    time_info, hours, minutes, seconds = readable_time(cell_info, military)
                else:
                    time_info = cell_info
                end_times.append(time_info)
            # TODO Automatically append header as key - would need dynamic dict for this
            # Otherwise, information is administrative, want the key to be header info
            elif (i_type == "UCD Number"):
                UCD_num = cell_info
            elif (i_type == "Course Name"):
                course_name = cell_info
            elif (i_type == "Duke Credit"):
                Duke_num = cell_info
            elif (i_type == "Grading"):
                grading == cell_info

    # Populate dictionary
    my_class = {
        "UCD_num" : UCD_num,
        "course_name" : course_name,
        "Duke_num" : Duke_num,
        "days" : days,
        "start_times" : start_times,
        "end_times" : end_times,
        "class_type" : class_type
    }

    # Print to verify information
    for i in my_class.keys():
        message = (f"Key: {i}, Value: {my_class[i]}")
        log_and_print(message)
    # Return class dictionary
    return my_class

#=========================END FUNCTION DEFINITIONS==================================

root = os.path.join("C:\\", "Users", "Max Smith", "Desktop", "GitHub", "pyCollege", "testing")
check_directory(root)

filename = "ucd_sched.xlsx"
inpath = os.path.join(root, filename)
check_file(inpath)

logging.info("All files verified, moving on to file read")

# Open workbook
w = xlrd.open_workbook(inpath)
sheet = w.sheet_by_name("pyCollege_xl")

# Call actions on the sheet
# extract_col(sheet)
# row, col = sheet_stats(sheet)
# header, data = class_info(sheet, 1)
# my_class = class_dict(header, data, convert_time=True, military=True)

# Create a list of class dictionaries to populate tkinter window
all_classes = []
for k in range(sheet.nrows-1):
    row = k + 1
    log_and_print(f"row #: {row}")
    header, data = class_info(sheet, row)
    my_class = class_dict(header, data, convert_time=True, military=True)
    all_classes.append(my_class)

# Verify all_classes is correct
log_and_print("Verifying all classes are correctly implemented")
log_and_print(f"all_classes length: {len(all_classes)}")
log_and_print(f"all_classes type: {type(all_classes)}")

