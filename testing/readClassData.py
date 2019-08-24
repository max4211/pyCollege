'''
Created: 24 August 2019
Author: Max Smith

Goal: Create a utility to read in carefully formatted excel files

'''

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
    
    # Print header info
    for i in range(len(header)):
        print(header[i])

    # Print data info
    for i in range(len(data)):
        print(data[i])

    message = (f"Header Length: {len(header)}, Data Length: {len(data)}")
    log_and_print(message)

    return data, header
    
class Course(object):

    pass


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
extract_col(sheet)
row, col = sheet_stats(sheet)
data, header = class_info(sheet, 1)

