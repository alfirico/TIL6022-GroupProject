import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import psutil
import time
import datetime


#converts date into three integers, one for day, month, and year
def split_date(date_str):
    date_list = int(date_str.split("-"))

    return date_list


#converts a date in the form [yyyy, mm, dd] into a day of the week (1-7)
def get_day_of_week(date_list):
    date_int = datetime(date_list)

    day_of_week = date_int.isoweekday() % 7

    return day_of_week


file_year = []
file_month = []
temp_data = []

#populate a list of months and years for future iteration through files
for i in range (2018,2024):
    file_year.append(str(i))
    for j in range(1,13):
        file_month.append(str(j).zfill(2))
        
#read in data to  list
for i in file_year:
    for j in file_month:
        file_path = "C:\\Users\\thoma\\Documents\\TIL_6022_Python\\TIL6022-GroupProject\\traffic-jam-data\\filtered_data\\%s-%s_rws_filedata_filtered.csv" % (file_year[0], file_month[0])
        temp_data.append(pd.read_csv(file_path))

#merge all data into one dataframe
data = pd.concat(temp_data)

