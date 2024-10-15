import pandas as pd

# Load the cleaned commuting data
df = pd.read_csv('FinalCommuteData/total_commuting_data.csv')

# Filter data for chosen years and weekdays
df_years = df[df['Year'].isin([2018, 2019, 2022, 2023])]
df_weekdays = df_years[df_years['Trip characteristics'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])]

# Group per year and weekday and generate table
df_weekdays_cartrip = df_weekdays.groupby(['Year', 'Trip characteristics'])['CarTrips'].mean().unstack()

# Calculate the total average for weekdays
df_weekdays_cartrip['Total'] = df_weekdays_cartrip.sum(axis=1) / 5

# Adjust order, layout and labels
order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
df_weekdays['Trip characteristics'] = pd.Categorical(df_weekdays['Trip characteristics'], categories=order, ordered=True)
df_weekdays_cartrip = df_weekdays_cartrip.round(3)
df_weekdays_cartrip.columns.name = 'Average car trip/person/weekday'

print("The average of car trips per person per weekday for 2018, 2019, 2022 and 2023 is the following: \n", df_weekdays_cartrip)