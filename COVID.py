# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits import mplot3d

import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
with warnings.catch_warnings():
    warnings.simplefilter("ignore", RuntimeWarning)

# Loading the dataset (Ensure the file path is correct)
data_frame = pd.read_csv('/path/to/country_wise_latest.csv')

# Displaying data
data_frame.head(10)
data_info = data_frame.info()
print(data_info)

# Summarizing the data
print('Data frame columns are summarized as- \n:')
data_frame.describe()

# Checking for missing values
print(data_frame.isnull().sum())

# Dropping rows with missing values (optional, if you want to clean the dataset)
df_cleaned = data_frame.dropna()

# Calculating totals
total_confirmed = data_frame['Confirmed'].sum()
total_recovered = data_frame['Recovered'].sum()
total_death = data_frame['Deaths'].sum()
print("Total Confirmed cases:", total_confirmed)
print("Total Recovered cases:", total_recovered)
print("Total Death cases:", total_death)

# Sorting data by different columns
sort_confirmed = data_frame.sort_values(by='Confirmed', ascending=False)
print(sort_confirmed.head(5))
print(sort_confirmed.tail(5))

sort_deaths = data_frame.sort_values(by='Deaths', ascending=False)
print(sort_deaths.head(5))
print(sort_deaths.tail(5))

sort_recovered = data_frame.sort_values(by='Recovered', ascending=False)
print(sort_recovered.head(5))
print(sort_recovered.tail(5))

sort_active = data_frame.sort_values(by='Active', ascending=False)
print(sort_active.head(5))
print(sort_active.tail(5))

# Plotting styles
plt.style.use('dark_background')
plt.style.use('ggplot')

# Line plot for confirmed cases by country
plt.figure(figsize=(15, 4))
plt.plot(data_frame['Country/Region'], data_frame['Confirmed'])
plt.xlabel("Country/Region")
plt.ylabel('Confirmed')
plt.title('Confirmed cases country-wise', fontsize=16, fontweight='bold', style='italic')
st.pyplot()

# Line plot for global trend of cases
plt.figure(figsize=(15, 6))
plt.plot(data_frame['Country/Region'], data_frame['Confirmed'], linestyle='-', color='#051282', label='Confirmed', lw=3)
plt.plot(data_frame['Country/Region'], data_frame['Deaths'], linestyle='-.', color='#ed0231', label='Deaths')
plt.plot(data_frame['Country/Region'], data_frame['Recovered'], linestyle='--', color='#30c90e', label='Recovered', lw=2)
plt.plot(data_frame['Country/Region'], data_frame['Active'], linestyle=':', color='w', label='Active', lw=2)
plt.xlabel('Country/Region')
plt.ylabel('No: of cases (in millions)')
plt.title('Global Trend of Covid Cases')
plt.legend()
st.pyplot()

# Line plot for Confirmed vs Deaths
plt.figure(figsize=(15, 4))
sns.lineplot(x="Deaths", y="Confirmed", data=data_frame)
plt.title('Confirmed cases vs Deaths')
st.pyplot()

# Line plot for Confirmed vs Recovered
plt.figure(figsize=(15, 4))
sns.lineplot(x="Recovered", y="Confirmed", data=data_frame)
plt.title('Confirmed cases vs Recovered')
st.pyplot()

# Line plot for Confirmed vs Active cases
plt.figure(figsize=(15, 4))
sns.lineplot(x="Active", y='Confirmed', data=data_frame)
plt.title('Confirmed cases vs Active')
st.pyplot()

# Line plot for new cases, deaths, and recoveries
plt.figure(figsize=(15, 6))
plt.plot(data_frame['Country/Region'], data_frame['New cases'], linestyle='-', color='#051282', label='New cases', lw=3)
plt.plot(data_frame['Country/Region'], data_frame['New deaths'], linestyle='-.', color='#ed0231', label='New deaths')
plt.plot(data_frame['Country/Region'], data_frame['New recovered'], linestyle='--', color='#30c90e', label='New recovered', lw=2)
plt.xlabel('Country')
plt.ylabel('No: of cases')
plt.title('Global Trend of New Covid Cases')
plt.legend()
st.pyplot()

# Group by WHO Region
Who_regionscon = data_frame.groupby('WHO Region')['Confirmed'].sum().sort_values()
print(Who_regionscon)

# Bar plot for confirmed cases by WHO Region
plt.figure(figsize=(9, 4))
sns.barplot(x="WHO Region", y='Confirmed', data=data_frame, palette='pastel')

# Pie chart for confirmed cases by WHO Region
plt.figure(figsize=(4, 4))
plt.pie(Who_regionscon, labels=Who_regionscon.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title("Confirmed cases vs WHO Region")
st.pyplot()

# Group by WHO Region for Deaths
Who_regionsdea = data_frame.groupby('WHO Region')['Deaths'].sum().sort_values()
print(Who_regionsdea)

# Bar plot for deaths by WHO Region
plt.figure(figsize=(8, 4))
sns.barplot(x="WHO Region", y='Deaths', data=data_frame, palette='magma')

# Pie chart for deaths by WHO Region
plt.figure(figsize=(4, 4))
plt.pie(Who_regionsdea, labels=Who_regionsdea.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('magma'))
st.pyplot()

# Group by WHO Region for Recovered
Who_regionsrec = data_frame.groupby('WHO Region')['Recovered'].sum().sort_values()
print(Who_regionsrec)

# Bar plot for recovered cases by WHO Region
plt.figure(figsize=(8, 4))
sns.barplot(x="WHO Region", y='Recovered', data=data_frame, palette='cubehelix')

# Pie chart for recovered cases by WHO Region
plt.figure(figsize=(4, 4))
plt.pie(Who_regionsrec, labels=Who_regionsrec.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('cubehelix'))
st.pyplot()

# Group by WHO Region for Active cases
Who_regionsact = data_frame.groupby('WHO Region')['Active'].sum().sort_values()
print(Who_regionsact)

# Bar plot for active cases by WHO Region
plt.figure(figsize=(9, 4))
sns.barplot(x="WHO Region", y='Active', data=data_frame, palette='pastel')

# Pie chart for active cases by WHO Region
plt.figure(figsize=(4, 4))
plt.pie(Who_regionsact, labels=Who_regionsact.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title("Active cases vs WHO Region")
st.pyplot()

# Line plot for percentage increase over 1 week
plt.figure(figsize=(15, 4))
sns.lineplot(x='1 week % increase', y="WHO Region", data=data_frame)
st.pyplot()

# Analysis specific to Nepal
nepal = data_frame[data_frame['Country/Region'] == 'Nepal']
print(nepal)

# Bar plot for Nepal
plt.figure(figsize=(15, 4))
sns.barplot(x=['Confirmed', 'Deaths', 'Recovered', 'Active'], 
            y=[nepal['Confirmed'].values[0], nepal['Deaths'].values[0], 
               nepal['Recovered'].values[0], nepal['Active'].values[0]])
plt.xlabel("Count")
plt.ylabel("Cases")
plt.title('COVID-19 Cases in Nepal')
st.pyplot()
