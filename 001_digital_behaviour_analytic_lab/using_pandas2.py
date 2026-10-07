'''Pandas is a Python library used for working with, cleaning, analyzing,
and manipulating structured data, especially data in tables such as CSV and Excel files.'''

from pathlib import Path

import pandas as pd

# Loading data
# read_csv() is a method used to read data from a CSV file
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / 'digital_behaviour.csv'

df = pd.read_csv(CSV_PATH)

# Inspection
print(df.head())
print(df.tail())
print(df.shape)
print(list(df.columns))  # Converts column names into a list
print(df.describe())  # Gives count, mean, std, min, 25%, 50%, 75%, and max

print(df[['Instagram_Minutes', 'YouTube_Minutes']].describe())
# Gives the statistical description of the two columns

col_name = ['Instagram_Minutes', 'YouTube_Minutes']
print(df[col_name].describe())

# Picking columns
print(df['Instagram_Minutes'])
print(df[['Date', 'Instagram_Minutes']])
print(df['Instagram_Minutes'].sum())
print(round(df['Study_Minutes'].mean()))
print(df['YouTube_Minutes'].max())

# Filtering
print(df[df['Instagram_Minutes'] > 100])
print(df[df['Study_Minutes'] > 180])

insta_high = df[
    (df['Instagram_Minutes'] > 100) &
    (df['Study_Minutes'] < 100)
]
print(insta_high)

print(df[df['Study_Minutes'] < df['Instagram_Minutes']])

# Sorting->sort values first then pick top 5
top_insta = df.sort_values(
    by='Instagram_Minutes',
    ascending=False
).head(5)


print(top_insta)

top_study = df.sort_values(by='Study_Minutes', ascending = False).head(5)

print(top_study)

df['Total_Screen_Time'] = (df['Instagram_Minutes'] + df['Study_Minutes'] + df['YouTube_Minutes'])

print(df)


df['Screen_Hours'] = round(df['Total_Screen_Time']/60,2)#->.round(2)   # series division

df['Digital_Balance'] = (df['Study_Minutes']/df['Total_Screen_Time']).round(2)#Series Division

#Classification
df['Day_Type'] =  'Normal'
df.loc[df["Total_Screen_Time"]>300, 'Day_Type'] = "Heavy"#Inplace

#Mask
'''df["Total_Screen_Time">300]['Day_Type'] = 'Heavy'        
        Temporary data is being modified = Standard'''

df['Day_Type'].value_counts()

print(df[['Instagram_Minutes', 'Youtube_Minutes', 'Video_Minutes', 'Study_Minutes']].sum())
print(df[['Instagram_Minutes', 'Youtube_Minutes', 'Video_Minutes', 'Study_Minutes']].max())


app_totals = {"Instagram" : df["Instagram_Minutes"].sum(),
              "Youtube" :df['YouTube_Minutes'].sum()}