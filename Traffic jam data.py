# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:08:31 2024

@author: BodMa
"""

import pandas as pd
import glob
import os

# Path to the data files
#path = r'C:\Users\BodMa\Documents\TU Delft\MSc TIL\2024-2025\Q1\TIL6022 - TIL Programming\Project\data'
path = "traffic-jam-data/data"

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
    #new_path =r'C:\Users\BodMa\Documents\TU Delft\MSc TIL\2024-2025\Q1\TIL6022 - TIL Programming\Project\data\filtered data'
    new_path = 'traffic-jam-data/filtered_data'
    filtered_df.to_csv(os.path.join(new_path, new_file_name), index=False)

print("Filtering complete")
