


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits import mplot3d

import os
import warnings
Filter Specific Warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
with warnings.catch_warnings():
    warnings.simplefilter("ignore", RuntimeWarning)


data_frame = pd.read_csv('/kaggle/input/corona-virus-report/country_wise_latest.csv')
data_frame
data_frame.head(10)
data_info= data_frame.info()
print(data_info)
print('Data frame columns are summerize as- \n:')
data_frame.describe()
data_frame.isnull()
print(data_frame.isnull().sum())
df_cleaned = data_frame.dropna()
total_confirmed = data_frame['Confirmed'].sum()
total_recovered = data_frame['Recovered'].sum()
total_death = data_frame['Deaths'].sum()
print("Total Conformed case", total_confirmed)
print("Total Recovered case", total_recovered)
print('Total Death case', total_death)
sort_confirmed = data_frame.sort_values(by = 'Confirmed', ascending = False)
print(sort_confirmed.head(5))
print(sort_confirmed.tail(5))
sort_deaths = data_frame.sort_values(by = 'Deaths', ascending = False)
print(sort_deaths.head(5))
print(sort_deaths.tail(5))
sort_recovered = data_frame.sort_values(by = 'Recovered', ascending = False)
print(sort_recovered.head(5))
print(sort_recovered.tail(5))
sort_active = data_frame.sort_values(by = 'Active', ascending = False)
print(sort_active.head(5))
print(sort_active.tail(5))
plt.style.use('dark_background')
plt.style.use('ggplot')
plt.figure(figsize= (15, 4))
plt.plot(data_frame['Country/Region'],data_frame['Confirmed'])
plt.xlabel("Country/Region")
plt.ylabel('Confirmed')
plt.title('Confirmed case countrywise', fontsize=16, fontweight='bold', style='italic')
plt.show()
plt.figure(figsize = (15,6))
plt.style.use('dark_background')


plt.plot(data_frame['Country/Region'], data_frame['Confirmed'],linestyle = '-',color = '#051282',label = 'Confirmed',lw = 3)


plt.plot(data_frame['Country/Region'], data_frame['Deaths'],linestyle = '-.',color = '#ed0231',label = 'Deaths')


plt.plot(data_frame['Country/Region'], data_frame['Recovered'],linestyle = '--',color = '#30c90e',label = 'Recovered',lw = 2)


plt.plot(data_frame['Country/Region'], data_frame['Active'],linestyle = ':',color = 'w',label = 'Active',lw = 2)
plt.xlabel('Country/Region')
plt.ylabel('No: of cases (in millions)')
plt.title('Global Trend of Covid Cases')
plt.legend()
plt.show()
plt.style.use('dark_background')
plt.style.use('ggplot')
plt.figure(figsize= (15, 4))
sns.lineplot(x = "Deaths", y = "Confirmed", data = data_frame)
plt.title('Confirmed case vs Deathcase')
plt.show()
plt.style.use('dark_background')
plt.style.use('ggplot')
plt.figure(figsize= (15, 4))
sns.lineplot(x = "Recovered", y = "Confirmed", data = data_frame)
plt.show()
plt.style.use('ggplot')
plt.figure(figsize= (15, 4))
sns.lineplot(x = "Active", y= 'Confirmed', data = data_frame)
plt.show()
plt.figure(figsize = (15,6))
plt.style.use('dark_background')


plt.plot(data_frame['Country/Region'], data_frame['New cases'],linestyle = '-',color = '#051282',label = 'New_cases',lw = 3)


plt.plot(data_frame['Country/Region'], data_frame['New deaths'],linestyle = '-.',color = '#ed0231',label = 'New_deaths')


plt.plot(data_frame['Country/Region'], data_frame['New recovered'],linestyle = '--',color = '#30c90e',label = 'New_recovered',lw = 2)
plt.xlabel('Country')
plt.ylabel('No: of cases')
plt.title('Global Trend of New Covid Cases')
plt.legend()
plt.show()
Who_regionscon = data_frame.groupby('WHO Region')['Confirmed'].sum().sort_values()
print(Who_regionscon)



#bar graph
plt.style.use('ggplot')
plt.style.use('dark_background')
plt.figure(figsize=(9, 4))
sns.barplot(x="WHO Region", y= 'Confirmed',data = data_frame, palette='pastel')


plt.figure(figsize=(4, 4))
plt.pie(Who_regionscon, labels=Who_regionscon.index, autopct='%1.1f%%', startangle=140,colors=sns.color_palette('pastel'))
plt.title("Confirmed case vs Who Region")
plt.show()
Who_regionsdea = data_frame.groupby('WHO Region')['Deaths'].sum().sort_values()
print(Who_regionsdea)




plt.style.use('ggplot')
plt.style.use('dark_background')
plt.figure(figsize = (8,4))
sns.barplot(x="WHO Region", y= 'Deaths',data = data_frame, palette='magma')


plt.figure(figsize=(4, 4))
plt.pie(Who_regionsdea, labels=Who_regionsdea.index, autopct='%1.1f%%', startangle=140,colors=sns.color_palette('magma'))
plt.show()
Who_regionsrec = data_frame.groupby('WHO Region')['Recovered'].sum().sort_values()
print(Who_regionsrec)





plt.style.use('ggplot')
plt.style.use('dark_background')
plt.figure(figsize = (8,4))
sns.barplot(x="WHO Region", y= 'Recovered',data = data_frame, palette='cubehelix')


plt.figure(figsize=(4, 4))
plt.pie(Who_regionsrec, labels=Who_regionsrec.index, autopct='%1.1f%%', startangle=140,colors=sns.color_palette('cubehelix'))
plt.show()
Who_regionsact = data_frame.groupby('WHO Region')['Active'].sum().sort_values()
print(Who_regionsact)




plt.style.use('ggplot')
plt.style.use('dark_background')
plt.figure(figsize=(9, 4))
sns.barplot(x="WHO Region", y= 'Active',data = data_frame, palette='pastel')


plt.figure(figsize=(4, 4))
plt.pie(Who_regionscon, labels=Who_regionscon.index, autopct='%1.1f%%', startangle=140,colors=sns.color_palette('pastel'))
plt.title("Active case vs Who Region")
plt.show()
plt.style.use('ggplot')
plt.figure(figsize= (15, 4))
sns.lineplot(x='1 week % increase', y= "WHO Region", data = data_frame)
plt.show()
nepal = data_frame[data_frame['Country/Region'] == 'Nepal']
print(nepal)



plt.figure(figsize= (15, 4))
sns.barplot(nepal, orient = 'h')
plt.xlabel("Count")
plt.title('Nepal')
plt.show()
