'''
Using the data created by the file commute_data_cleanup.py, this code will organize the data for car commuting considering the weekdays and years 
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
df_weekdays_cartrip = df_weekdays.groupby(['Year', 'Trip characteristics'])['CarTrips'].mean().unstack()

# Calculate the total average for weekdays
df_weekdays_cartrip['Total'] = df_weekdays_cartrip.sum(axis=1) / 5

# Adjust order, layout and labels
df_weekdays_cartrip = df_weekdays_cartrip.round(3)
df_weekdays_cartrip.columns.name = 'Average car trip/person/weekday'

# Print table
print("The average of car trips per person per weekday for 2018, 2019, 2022 and 2023 is the following: \n", df_weekdays_cartrip)

# Visualization
# Creating the DataFrame
data = {
    'Year': [2018, 2019, 2022, 2023],
    'Monday': [0.353, 0.330, 0.280, 0.272],
    'Tuesday': [0.373, 0.350, 0.295, 0.291],
    'Wednesday': [0.339, 0.325, 0.255, 0.262],
    'Thursday': [0.349, 0.330, 0.285, 0.282],
    'Friday': [0.309, 0.285, 0.220, 0.220],
}
df_weekdays_cartrip = pd.DataFrame(data).set_index('Year')
df_weekdays_cartrip.columns.name = ''

# Plotting graph
df_weekdays_cartrip.plot(kind='bar', grid=True, figsize=(10, 6))
plt.xlabel('Year')
plt.ylabel('Average Car Trip per Person per Weekday')
plt.ylim(0, 0.8)  # Setting y-axis range from 0 to 0.8 in order to show the result clearly
plt.title('Average Car Trips per Person per Weekday (2018, 2019, 2022, 2023)')
plt.xticks(rotation=0)
plt.show()