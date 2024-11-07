# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os

# Converts date into three integers, one for day, month, and year
def split_date(date_str):
    date_list_int = [int(i) for i in date_str.split("-")]
    if date_list_int[2] > 31:  # if year is at the end, reverse order
        date_list_int.reverse()
    return date_list_int

# Converts a date in the form [yyyy, mm, dd] into a day of the week (1-7)
def get_day_of_week(date_list):
    date = datetime.datetime(*date_list)
    return date.isoweekday()  # returns 1-7 (Monday-Sunday)

# Define constants
n_weekdays = 5  # Only weekdays are counted (Monday to Friday)
years = [2018, 2019, 2022, 2023]  # The years of interest
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Initialize an array to store summed heaviness data by year and weekday
traffic_jam_heaviness = np.zeros((len(years), n_weekdays))

# Get the script's directory to construct file paths
script_dir = os.path.dirname(__file__)

# Loop through the years and months to read data from all the CSV files
for year in years:
    for month in range(1, 13):  # 1 to 12 months
        file_month = str(month).zfill(2)  # Format month as two digits (01, 02, ...)

        # Construct file path based on the current year and month
        file_path = os.path.join(script_dir, f"traffic-jam-data/filtered_data/{year}-{file_month}_rws_filedata_filtered.csv")

        try:
            # Read the CSV file for the current month
            temp_data = pd.read_csv(file_path, low_memory=False)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            continue

        # Process the data from the current file
        temp_data.set_index("NLSitNumber")
        for index, row in temp_data.iterrows():
            date_list = split_date(row["StartDateJam"])
            day_of_week = get_day_of_week(date_list) - 1  # Convert to 0-indexed (0-4 for Monday-Friday)
            year_from_data = date_list[0]

            if year_from_data in years and 0 <= day_of_week < n_weekdays:  # Check that year and weekday are in range
                year_index = years.index(year_from_data)  # Map year to index (e.g., 2018 -> 0)
                heaviness_value = int(row["HeavinessJam"].replace(",", ""))
                traffic_jam_heaviness[year_index][day_of_week] += heaviness_value

# Plotting the summed data for each year by weekday
fig, ax = plt.subplots()

# Set bar width and x positions
width = 0.15
x = np.arange(len(years))

# Plot a set of bars for each weekday, with each bar showing total heaviness for that weekday across years
for i, weekday in enumerate(weekdays):
    ax.bar(x + i * width, traffic_jam_heaviness[:, i], width, label=weekday)

# Configure x-axis with year labels
ax.set_xticks(x + (width * 2))
ax.set_xticklabels(years)
ax.set_xlabel("Year")
ax.set_ylabel("Total Heaviness")
ax.set_title("Total Traffic Jam Heaviness by Year and Weekday")

# Create legend and layout adjustments
ax.legend()
ax.grid()
plt.tight_layout()
plt.show()
