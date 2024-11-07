# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:08:31 2024

@author: BodMa
"""

import pandas as pd
import glob
import os

# Path to the data files
path = r'C:\Users\BodMa\Documents\TU Delft\MSc TIL\2024-2025\Q1\TIL6022 - TIL Programming\Project\data'

# Load all files into a list of DataFrames
all_files = glob.glob(os.path.join(path, "*.csv"))


def translate(text):
    """Function to replace specific words

    The function replaces some importamt Dutch words with their English
    translations, to ensure readability for all group members.
    """

    translations = {
        'Spitsfile': 'Rush hour jam',
        'spitsfile': 'rush hour jam',
        'ongeval': 'accident',
        'Ongeval': 'Accident',
        'aflopend': 'descending',
        'oplopend': 'ascending',
        'een':'a',
        'met':'with',
        'geen oorzaak gemeld':'no cause mentioned',
        'ga oorzaak gemeld':'no cause mentioned'
    }
    for dutch, english in translations.items():
        text = text.replace(dutch, english)
    return text


# Process each file, filter and translate
for file in all_files:
    df = pd.read_csv(file, sep=";")

    # Filter the DataFrame to only contain rush hour traffic jams
    filtered_df = df[df['OorzaakGronddetail'].str.contains('spitsfile', case=False, na=False)]

    # Translate the Dutch column headers
    filtered_df = filtered_df.rename(columns={
        "NLSitNummer":"NLSitNumber",
        "DatumFileBegin":"StartDateJam",
        "DatumFileEind":"EndDateJam",
        "TijdFileBegin":"StartTimeJam",
        "TijdFileEind":"EndTimeJam",
        "FileZwaarte":"HeavinessJam",
        "GemLengte":"AvgLength",
        "FileDuur":"DurationJam",
        "HectometerKop":"HectrometreHead",
        "HectometerStaart":"HectrometreTail",
        "RouteLet":"RouteLet",
        "RouteNum":"RouteNum",
        "RouteOms":"RouteDescr",
        "hectometreringsrichting":"HectrometreDir",
        "KopWegvakVan":"FromSection",
        "KopWegvakNaar":"ToSection",
        "TrajVan":"RouteFrom",
        "TrajNaar":"RouteTo",
        "OorzaakGronddetail":"CauseGroundDetail",
        "OorzaakVerloop":"CauseProgression",
        "OorzaakCodeVerloop":"CauseCodeProgression",
        "OorzaakCode":"CauseCode",
        "Oorzaak_1":"Cause_1",
        "Oorzaak_2":"Cause_2",
        "Oorzaak_3":"Cause_3",
        "Oorzaak_4":"Cause_4",
    })

    # Apply translation function
    filtered_df['CauseGroundDetail'] = filtered_df['CauseGroundDetail'].apply(translate)
    filtered_df['HectrometreDir'] = filtered_df['HectrometreDir'].apply(translate)

    # Extract the year and month from the file name
    file_name = os.path.basename(file)
    year_month = file_name.split('_')[0]

    # Save the filtered DataFrame seperately
    new_file_name = f'{year_month}_rws_filedata_filtered.csv'
    new_path =r'C:\Users\BodMa\Documents\TU Delft\MSc TIL\2024-2025\Q1\TIL6022 - TIL Programming\Project\data\filtered data'
    filtered_df.to_csv(os.path.join(new_path, new_file_name), index=False)

print("Filtering complete")

import numpy as np
import matplotlib.pyplot as plt

# Assuming the following arrays were populated with actual data in the original code
n_years = 4  # 2018, 2019, 2022, 2023
n_weekdays = 5  # Monday to Friday

# Sample data for demonstration purposes; in real use, these would be populated from actual data files
traffic_jam_count = np.random.randint(1000, 5000, (n_years, 12, n_weekdays))  # counts for 12 months
traffic_jam_heaviness = np.random.randint(1e6, 5e6, (n_years, 12, n_weekdays))  # heaviness for 12 months

# Sum across months to get yearly data for each weekday
total_traffic_jam_count_per_year = np.sum(traffic_jam_count, axis=1)
total_traffic_jam_heaviness_per_year = np.sum(traffic_jam_heaviness, axis=1)

# Years and weekdays labels
years = ["2018", "2019", "2022", "2023"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Plotting the total number of traffic jams with years on the horizontal axis
plt.figure(figsize=(10, 6))
width = 0.15  # Width of each bar

# Plot each weekday's data with an offset to align bars side by side for each year
for i, weekday in enumerate(weekdays):
    plt.bar(np.arange(len(years)) + i * width, total_traffic_jam_count_per_year[:, i], width=width, label=weekday)

plt.xticks(np.arange(len(years)) + width * 2, years)  # Center ticks under grouped bars
plt.ylabel("Total Number of Traffic Jams")
plt.xlabel("Year")
plt.title("Total Number of Traffic Jams per Year by Weekday")
plt.legend(title="Weekday")
plt.show()