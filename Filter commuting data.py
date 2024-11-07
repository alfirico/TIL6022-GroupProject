'''
This code combines the datasets in the CommuteData folder. This folder contains both the weekday trip data for every year,
as well as the travel modes of the trips per year.
This file combines all the weekday trip data into a single dataframe with only the relevant information, and multiplies it by
the car trip data to create a final dataset (saved in FinalCommuteData) that contains the car trips done by weekday per year, for commuting

'''

import pandas as pd
import os

# Access to CSV files
folder_path = "CommuteData"
csv_files = [
    "2018-weekday-trip-data.csv",
    "2019-weekday-trip-data.csv",
    "2020-weekday-trip-data.csv",
    "2021-weekday-trip-data.csv",
    "2022-weekday-trip-data.csv",
    "2023-weekday-trip-data.csv"
]

# Lists for dataframes
commute_dfs = []
total_trips_dfs = []

# Load data
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path, delimiter=';', decimal=',', on_bad_lines='skip')
    year = file.split('-')[0]
    df['Year'] = int(year)        # Use the year in the file name as a variable in the dataframe      

    commute_data = df[df['Travel motives'].str.contains('commute', case=False, na=False)]
    total_trips_data = df[~df['Travel motives'].str.contains('commute', case=False, na=False)]
    
    commute_dfs.append(commute_data)
    total_trips_dfs.append(total_trips_data)

# Combine dataframes
combined_commute_df = pd.concat(commute_dfs, ignore_index=True)
combined_total_trips_df = pd.concat(total_trips_dfs, ignore_index=True)

# Drop irrelevant columns
combined_commute_df = combined_commute_df.drop(columns=['Population', 'Margins', 'Region characteristics', 'Travel motives', 'Periods'], errors='ignore')
combined_total_trips_df = combined_total_trips_df.drop(columns=['Population', 'Margins', 'Region characteristics', 'Travel motives', 'Periods'], errors='ignore')

# Load additional travel modes data
modes_file = "per_person__travel_modes__travel_purpose_13102024_144003.csv"
modes_file_path = os.path.join(folder_path, modes_file)
modes_df = pd.read_csv(modes_file_path, delimiter=';', decimal=',', on_bad_lines='skip')

# Separate and clean modes data
commute_mode_df = modes_df[modes_df['Travel motives'].str.contains('commute', case=False, na=False)]
total_mode_df = modes_df[~modes_df['Travel motives'].str.contains('commute', case=False, na=False)]

commute_mode_df = commute_mode_df.drop(columns=['Population', 'Margins', 'Region characteristics', 'Travel motives'], errors='ignore')
total_mode_df = total_mode_df.drop(columns=['Population', 'Margins', 'Region characteristics', 'Travel motives'], errors='ignore')

commute_mode_df.rename(columns={'Periods': 'Year'}, inplace=True)
total_mode_df.rename(columns={'Periods': 'Year'}, inplace=True)

# Calculate mode fractions
pivot_trips_df = commute_mode_df.pivot(index='Year', columns='Travel modes', values='Average per person per day/Trips (number)').reset_index()
normalized_trips_df = pivot_trips_df.copy()
trips_modes = [col for col in pivot_trips_df.columns if col not in ['Year', 'Total']]
normalized_trips_df[trips_modes] = pivot_trips_df[trips_modes].div(pivot_trips_df['Total'], axis=0)

# Calculate car trips
car_percentage_df = normalized_trips_df[['Year', 'Passenger car (driver)']]
merged_commute_car_df = pd.merge(combined_commute_df, car_percentage_df, on='Year', how='left')
merged_commute_car_df['CarTrips'] = merged_commute_car_df['Average per person per day/Trips (number)'] * (merged_commute_car_df['Passenger car (driver)'])

# Reorder and save data
cols = merged_commute_car_df.columns.tolist()
cols.insert(0, cols.pop(cols.index('Year')))
merged_commute_car_df = merged_commute_car_df[cols]
file_path = os.path.join('FinalCommuteData', 'total_commuting_data.csv')
merged_commute_car_df.to_csv(file_path, index=False)

df_head()