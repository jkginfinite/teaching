# Exercise 7.23
import pandas as pd

temps = {
    'Maxine': [98.6, 96.9, 97.7], 
    'James': [98.9, 100.3, 101.1], 
    'Amanda': [98.5, 98.3, 98.7]
}

temperatures = pd.DataFrame(temps)

temperatures

temperatures

temperatures = pd.DataFrame(temps, 
                            index=['Morning', 'Afternoon','Evening'])

temperatures

temperatures.Maxine

temperatures.loc['Morning']

temperatures.loc[['Morning', 'Evening']]

temperatures.loc[:, ['Amanda', 'Maxine']]

temperatures.loc['Morning':'Afternoon', ['Amanda', 'Maxine']]

temperatures.describe()

temperatures.T

temperatures.sort_index(axis=1)
