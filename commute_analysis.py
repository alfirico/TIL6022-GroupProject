'''Using the data created by the file commute_data_cleanup.py, this code will organize the data for general commuting considering the weekdays and years 
in interest, outputing tbles and graphs for the analysis.'''
import pandas as pd

# Load the cleaned commuting data
df = pd.read_csv('FinalCommuteData/total_commuting_data.csv')

# Filter data for chosen years and weekdays
df_years = df[df['Year'].isin([2018, 2019, 2022, 2023])]
df_weekdays = df_years[df_years['Trip characteristics'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])]

# Order weekdays
order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
df_weekdays['Trip characteristics'] = pd.Categorical(df_weekdays['Trip characteristics'], categories=order, ordered=True)

# Group per year and weekday and generate table
df_weekdays_trip = df_weekdays.groupby(['Year', 'Trip characteristics'])['Average per person per day/Trips (number)'].mean().unstack()

# Calculate the total average for weekdays
df_weekdays_trip['Total'] = df_weekdays_trip.mean(axis=1)

# Adjust order and labels
df_weekdays_trip.columns.name = 'Average commute trip/person/weekday'


print(
    "The average of trips per person per weekday for 2018, 2019, 2022 and 2023 is the following: \n",
    df_weekdays_trip)