'''
Using the data created by the file commute_data_cleanup.py, this code will organize the data for general commuting considering the weekdays and years 
in interest, outputing tables and graphs for the result analysis.
'''

import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned commuting data
df = pd.read_csv('data/commute-data/final-commute-data/total_commuting_data.csv')

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

# Print table
print(
    "The average of trips per person per weekday for 2018, 2019, 2022 and 2023 is the following: \n",
    df_weekdays_trip)


#Visualization
# Creating the DataFrame
data = {
    'Year': [2018, 2019, 2022, 2023],
    'Monday': [0.72, 0.66, 0.56, 0.57],
    'Tuesday': [0.76, 0.70, 0.59, 0.61],
    'Wednesday': [0.69, 0.65, 0.51, 0.55],
    'Thursday': [0.71, 0.66, 0.57, 0.59],
    'Friday': [0.63, 0.57, 0.44, 0.46],
}
df_commute_trips = pd.DataFrame(data).set_index('Year')
df_commute_trips.columns.name = ''

# Plotting graph
df_commute_trips.plot(kind='bar', grid=True, figsize=(10, 6))
plt.xlabel('Year')
plt.ylabel('Average Commute Trip per Person per Weekday')
plt.ylim(0, 0.8)  # Setting y-axis range from 0 to 0.8 in order to show the result clearly
plt.title('Average Commute Trips per Person per Weekday (2018, 2019, 2022, 2023)')
plt.xticks(rotation=0)
plt.show()