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

print("\n")

print(
    "The average of trips per person per weekday for 2018, 2019, 2022 and 2023 is the following: \n",
    df_weekdays_trip)

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (replace the file path with the correct one for your data)
df = pd.read_csv('FinalCommuteData/total_commuting_data.csv')

# Filter data for chosen years (2018, 2019, 2022, 2023) and weekdays (Monday to Friday)
df_years = df[df['Year'].isin([2018, 2019, 2022, 2023])]
df_weekdays = df_years[df_years['Trip characteristics'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])]

# Order weekdays properly
order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
df_weekdays['Trip characteristics'] = pd.Categorical(df_weekdays['Trip characteristics'], categories=order, ordered=True)

# Group the data by 'Year' and 'Trip characteristics' (weekday), and calculate the average trips per person per day
df_weekdays_trip = df_weekdays.groupby(['Year', 'Trip characteristics'])['Average per person per day/Trips (number)'].mean().unstack()

# Calculate the total average for weekdays (across all selected years)
df_weekdays_trip['Total'] = df_weekdays_trip.mean(axis=1)

# Adjust the table's column name
df_weekdays_trip.columns.name = 'Average commute trip/person/weekday'

# Visualization
plt.figure(figsize=(10, 6))
df_weekdays_trip.drop('Total', axis=1).plot(kind='bar', figsize=(10, 6))

# Customize the plot
plt.title("Average Commute Trips per Person per Weekday (2018, 2019, 2022, 2023)")
plt.ylabel("Average Comutte Trips per Person")
plt.xlabel("Year")
plt.xticks(rotation=0)  # Keep the x-tick labels horizontal
plt.legend(title="Weekday", bbox_to_anchor=(1.05, 1), loc='upper left')  # Move the legend to the right side
plt.tight_layout()  # Adjust layout to avoid clipping
plt.show()