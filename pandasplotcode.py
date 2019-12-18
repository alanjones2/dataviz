# # An Introduction to Data Visualization with Pandas

# ## Importing the libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ## Getting the data

weather = pd.read_csv('https://raw.githubusercontent.com/alanjones2/dataviz/master/london2018.csv')
print(weather)

# ## A first Pandas Plot

weather.plot(y='Tmax', x='Month')
plt.show()

# ## Simple charts

weather.plot(y=['Tmax','Tmin'], x='Month')
plt.show()

weather['Tmed'] = (weather['Tmax'] + weather['Tmin'])/2

weather.plot(y=['Tmax','Tmin','Tmed'], x='Month')
plt.show()

# ### Bar Charts

weather.plot(kind='bar', y='Rain', x='Month')
plt.show()

weather.plot(kind='barh', y='Rain', x='Month')
plt.show()

weather.plot(kind='bar', y=['Tmax','Tmin'], x='Month')
plt.show()

weather.plot(kind='bar', y=['Tmax','Tmed','Tmin'], x='Month')
plt.show()

# ### Scatter Plot

weather.plot(kind='scatter', x='Sun', y='Rain')
plt.show()

# ### Pie charts

weather.plot(kind='pie', y='Sun')
plt.show()

weather.index=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
weather.plot(kind='pie', y = 'Sun', legend=False)
plt.show()

# ## Statistical charts and spotting unusual events

more_weather = pd.read_csv('https://raw.githubusercontent.com/alanjones2/dataviz/master/londonweather.csv')
print(more_weather[0:48])

print(more_weather.Rain.describe())

more_weather.plot.box(y='Rain')
plt.show()

# ## Histograms

more_weather.plot(kind='hist', y='Rain')
plt.show()

# #### More bins

more_weather.plot(kind='hist', y='Rain', bins=[0,25,50,75,100,125,150,175])
plt.show()

more_weather.plot.hist(y='Rain', bins=[0,25,75,175])
plt.show()

# ## Pandas Plot utilities

# ### Multiple charts

weather.plot(y=['Tmax', 'Tmin','Rain','Sun'], subplots=True, layout=(2,2), figsize=(10,5))
plt.show()

weather.plot(kind='bar', y=['Tmax', 'Tmin','Rain','Sun'], subplots=True, layout=(2,2), figsize=(10,5))
plt.show()

weather.plot(kind='pie', y=['Tmax', 'Tmin','Rain','Sun'], subplots=True, legend=False, layout=(2,2), figsize=(10,10))
plt.show()

# ### Saving the Charts

weather.plot(kind='pie', y='Rain', legend=False)
plt.show()
plt.savefig("pie.png")
