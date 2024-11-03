import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import psutil
import time
import datetime


import datetime

#converts date into three integers, one for day, month, and year
def split_date(date_str):
    date_list_int = []
    date_list = date_str.split("-")
    
    for i in date_list: #Convert string list to int list
        date_list_int.append(int(i))
    
    print(date_list_int)
    
    if(date_list_int[2]>31):
        date_list_int.reverse() #go from [DD/MM/YYY] to [YYYY/MM/DD]
    
    print(date_list_int)
    
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
traffic_jam_count = np.zeros((n_years+2,n_months,n_weekdays))
traffic_jam_heaviness = np.zeros((n_years+2,n_months,n_weekdays))
count_list = []
heaviness_list = []
year_list = ["2018","2019","2022","2023"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
months = ["January", "February", "March", "April", "May", "June", "July", 
          "August", "September", "October", "November", "December"]



#populate a list of months and years for future iteration through files
for i in year_list:
    file_year.append(i)
    for j in range(1,13):
        file_month.append(str(j).zfill(2))

#read in data to 
for i in file_year:
    for j in file_month:
        file_path = "C:\\Users\\thoma\\Documents\\TIL_6022_Python\\"+"TIL6022-GroupProject\\traffic-jam-data\\filtered_data"+"\\%s-%s_rws_filedata_filtered.csv" % (i, j)
        temp_data=pd.read_csv(file_path)
        temp_data.set_index("NLSitNumber")
        for index, row in temp_data.iterrows():
            traffic_jam_count[int(i)-2018][int(j)-1][(get_day_of_week(split_date(row["StartDateJam"]))-1)] += 1
            traffic_jam_heaviness[int(i)-2018][int(j)-1][(get_day_of_week(split_date(row["StartDateJam"]))-1)] += int(row["HeavinessJam"].replace(",",""))\


count_plot = plt.figure()
heaviness_plot = plt.figure()

print(traffic_jam_count)

width = 0.075

x=np.arange(0,5)


fig, axs_count = plt.subplots(2,2)
fig, axs_heaviness = plt.subplots(2,2)

"""for i in file_year:
    for j in file_month:
        file_path = "C:\\Users\\thoma\\Documents\\TIL_6022_Python\\"+"TIL6022-GroupProject\\traffic-jam-data\\processed_data"+"\\%s-%s_processed.csv" % (i, j)
        with open(file_path, 'w', newline = '') as csvfile:
            """

for ax, year in zip(axs_count.flat, year_list):
    multiplier = 0 
    ax.set_title(year)
    for month in range(len(months)):
        offset = width * multiplier
            
        rects=ax.bar(x+offset, traffic_jam_count[int(year)-2018, month, :], width, label = month)
        #ax.bar_label(rects, padding=3)
        multiplier += 1
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
            
    ax.set_xticks(x + width, weekdays)
    ax.set_xticklabels(weekdays)
    ax.set_xlabel("Days of the week")
    ax.set_ylabel("Number of Traffic Jams")
    
for ax, year in zip(axs_heaviness.flat, year_list):
    multiplier = 0 
    ax.set_title(year)
    for month in range(len(months)):
        offset = width * multiplier
            
        rects=ax.bar(x+offset, traffic_jam_heaviness[int(year)-2018, month, :], width, label = month)
        #ax.bar_label(rects, padding=3)
        multiplier += 1
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
            
    ax.set_xticks(x + width, weekdays)
    ax.set_xticklabels(weekdays)
    ax.set_xlabel("Days of the week")
    ax.set_ylabel("Total Heaviness of Traffic Jams")    
    
fig.tight_layout()
plt.show()