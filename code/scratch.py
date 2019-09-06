# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import numpy as np
import numpy.linalg as nl
import matplotlib.pyplot as plt
import random
import string
from random import choice

import pandas as pd




#%%  Empty dataframe
'''
Save this stuff
'''
dt = pd.DataFrame(columns=['Damage', 'Health', 'DPS'])
dt

dt.loc['Obs'] = 'Null'
dt.loc['Critter'] = 1
dt.loc['Marine'] = [6, 40, 8]
dt

#%%  Renaming columns
r = {'Damage': 'Dmg',
     'Health': 'H',
     'DPS': 'Dabbus'}
r = pd.Series(r)
dt.rename(columns = r)


#%%  Tracker
# Have the tracker use Calories as the index.
columns = ['Food Name'] + list(rda.index)
columns

tracker = pd.DataFrame(columns = columns)
tracker

cal = 0
tracker.loc[cal] = np.zeros(len(columns))
tracker

food = df.iloc[0]
cal += food['Calories']
tracker.loc[cal] = food[columns]
tracker

food = df.iloc[10]
cal += food['Calories']
tracker.loc[cal] = food[columns]
tracker

#%%  Tracker Redux
# Have the tracker use Calories as the index.
columns = ['Food Name'] + list(rda.index)
tracker = pd.DataFrame(columns = columns)

cal = 0
tracker.loc[cal] = np.zeros(len(columns))

#%%  Adding food
food = df.iloc[0]
cal += food['Calories']
tracker.loc[cal] = food[columns]


#%%  Defining a function from previous parameters.

a = 5
def f(b):
    return a + b

del a
b = 2
print(f(b))


#%%  Using a function as a loop condition - works.
def continue_(num):
    return num < 6

numbers = [i+1 for i in range(6)]

choice(numbers)
lista = []
random.seed(1)

def test(num = 1):
    while continue_(num):
        num = choice(numbers)
        lista.append(num)
    return num
    
test()
#lista

#%%
lst_to_string = ['The','Python','Tutorials']
' '.join(lst_to_string)
