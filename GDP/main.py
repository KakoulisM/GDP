import pandas as pd

read_df = pd.read_csv("Real GDP per capita.csv")
pop_df = pd.read_csv("population.csv", skiprows=2)

read_df = read_df.rename(columns={r'geo\TIME_PERIOD': 'Year'})
read_df = read_df.rename_axis("Country Name", axis=1)
read_df = read_df.set_index("Year")
read_df = read_df.drop(columns="#", axis=1)

selected_df = read_df[["EL: Greece", "DK: Denmark"]]
selected_df = selected_df.copy()
selected_df['GDP Difference'] = selected_df['EL: Greece'] - selected_df['DK: Denmark']
selected_df['Greece_diff'] = selected_df['EL: Greece'].diff()
selected_df['Denmark_diff'] = selected_df['DK: Denmark'].diff()
final_df = selected_df[['DK: Denmark', 'Denmark_diff', 'EL: Greece', 'Greece_diff', 'GDP Difference']]

selected_pop_df = pop_df[pop_df['Country Name'].isin(['Greece', 'Denmark'])]
selected_pop_df.columns = selected_pop_df.columns.map(str)
year_range = [str(year) for year in range(1995, 2022)]
final_pop_df = selected_pop_df[['Country Name'] + year_range]

pop_long = final_pop_df.set_index('Country Name').T
pop_long.index.name = 'Year'
pop_long.reset_index(inplace=True)
pop_long['Year'] = pop_long['Year'].astype(int)
pop_long = pop_long.set_index('Year')
pop_long['Greece_pop_diff'] = pop_long['Greece'].diff()
pop_long['Denmark_pop_diff'] = pop_long['Denmark'].diff()

final_df['Greece_pop'] = pop_long['Greece']
final_df['Denmark_pop'] = pop_long['Denmark']
final_df['Greece_pop_diff'] = pop_long['Greece_pop_diff']
final_df['Denmark_pop_diff'] = pop_long['Denmark_pop_diff']
final_df = final_df[[
    'EL: Greece',
    'DK: Denmark',
    'GDP Difference',
    'Greece_diff',
    'Denmark_diff',
    'Greece_pop',
    'Denmark_pop',
    'Greece_pop_diff',
    'Denmark_pop_diff'
]]
print(final_df)

final_df.to_csv("gdp_analysis_output.csv")


