# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import csv
import matplotlib.gridspec as gridspec

#converts date into three integers, one for day, month, and year
def split_date(date_str):
    date_list_int = []
    date_list = date_str.split("-")
    
    for i in date_list: #Convert string list to int list
        date_list_int.append(int(i))
    
    if(date_list_int[2]>31):
        date_list_int.reverse() #go from [DD/MM/YYY] to [YYYY/MM/DD]
    
    return date_list_int


#converts a date in the form [yyyy, mm, dd] into a day of the week (1-7)
def get_day_of_week(date_list):
    date = datetime.datetime(*date_list)

    day_of_week = date.isoweekday()

    return day_of_week


n_months = 12
n_years = 4
n_weekdays = 5
file_year = []
file_month = []
temp_data = []
traffic_jam_heaviness = np.zeros((n_years+2,n_weekdays))
count_list = []
heaviness_list = []
year_list = ["2018","2019","2022","2023"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
months = ["January", "February", "March", "April", "May", "June", "July", 
          "August", "September", "October", "November", "December"]

#get the location of the python file
script_dir = os.path.dirname(__file__)

#populate a list of months and years for future iteration through files
for i in year_list:
    file_year.append(i)
    for j in range(1,13):
        file_month.append(str(j).zfill(2))

#read in data and process to smaller arrays of useful info
for i in file_year:
    for j in file_month:
        rel_file_path = "traffic-jam-data\\filtered_data"+"\\%s-%s_rws_filedata_filtered.csv" % (i, j)
        abs_file_path = os.path.join(script_dir, rel_file_path)
        try:
            temp_data=pd.read_csv(abs_file_path)
        except:
            print(abs_file_path)
        temp_data.set_index("NLSitNumber")
        for index, row in temp_data.iterrows():
            traffic_jam_heaviness[int(i)-2018][(get_day_of_week(split_date(row["StartDateJam"]))-1)] += int(row["HeavinessJam"].replace(",",""))

"""#save heaviness data to csv file for easier processing in the future
for i in file_year:
        rel_file_path_csv = "traffic-jam-data\\processed_data"+"\\%s_heaviness_processed.csv" % i
        abs_file_path_csv = os.path.join(script_dir, rel_file_path_csv)
        with open(abs_file_path_csv, 'w', newline = '') as csvfile:
            writer = csv.writer(csvfile)
            for j in file_month:
                writer.writerow(traffic_jam_heaviness[int(i)-2018][int(j)-1][:])   """
                
#remove all zero columns
traffic_jam_heaviness_clean=np.delete(traffic_jam_heaviness, [2,3], 0)

#create plot
ax = plt.subplot(111)

#set bar width and x range
width = 0.075
x=np.arange(0,5)

year_list = ["2018","2019","2022","2023","2024"]

#Generate total traffic jam graph using loops to create multiple value series
multiplier = 0 
for day in range(len(weekdays)):
    offset = width * multiplier
    
    print(day)
            
    rects=ax.bar(x+offset, traffic_jam_heaviness_clean[:][day], 
                 width, label = year_list)
    multiplier += 1
plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
            
ax.set_xticks(x + width, weekdays)
ax.set_xticklabels(weekdays)
ax.set_xlabel("Days of the week")
ax.set_ylabel("Total Heaviness")

 #Create title and legend for fig 1
ax.title("Total Number of Traffic Jams")
ax.legend(weekdays, loc="upper right", ncol = 1,bbox_to_anchor = (1.25,1))  

#Set layout for figures
ax.tight_layout()
plt.show()