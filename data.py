# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 19:53:43 2019
@author: justin
"""
#%%  Parameters
# Serving Size.  Units in g or cal.
serving_amount = 50
# units: Mass (g), Calories
serving_unit = 'Mass (g)'

# Whether to include foods like tea, beer, and lard.
include_unusual = False
# Whether to include foods like coconut, eel, and edemame.
include_exotic = False


#%%  Packages
import pandas as pd
import string
import matplotlib.pyplot as plt

pd.set_option('mode.chained_assignment',None)


#%%  Import Data
df = pd.read_csv('data/data.csv', index_col = 'Database Number')
df.index = df.index.astype(int)
# dfo - the full dataset, reserved
dfo = df
len(df)

# Set up RDA
rda = pd.read_csv('data/RDA.csv', index_col = "Nutrient (unit)", encoding = 'latin1')
rda = rda.RDA
rda

#%%  Subset
# Curate data
food_list = pd.read_csv('data/main_idx.csv', index_col = 'Database Number')
idx = food_list.index.dropna()
food_list = food_list.loc[idx]
food_list.index = food_list.index.astype(int)
food_list.fillna(False, inplace = True)
flo = food_list.copy()

if not include_unusual:
    idx = food_list.loc[food_list.Unusual == True].index    
    food_list.drop(idx, inplace = True)

if not include_exotic:
    idx = food_list.loc[food_list.Exotic == True].index    
    food_list.drop(idx, inplace = True)

df = df.loc[food_list.index]


#%% Rename Columns
# Note - this cell triggers warning oncopy of a slice.
d = {'Food Name': 'Food'}
for frame in (df, food_list):
    frame.rename(columns = d, inplace = True)
    frame.index.rename('ID#', inplace = True)

food_list.Food

#%%  Food names
# Note - this cell triggers warning oncopy of a slice.
df.columns
long_names = df['Food'].copy()

def clip_food_name(text):
    '''
    Shortens food names to be readable.
    '''
    text = ','.join(text.split(',')[:2])
    text= text[:30]
    return text

cols = ['Food', 'Food Group']
df[cols] = df[cols].applymap(clip_food_name)
df[cols].head()

#%%  Cleaning
df = df.fillna(0)


#%%  Serving Size
df['Mass (g)'] = 100

numerics = (df.dtypes == 'float64') | (df.dtypes == 'int64')
numerics = numerics[numerics == True].index

def recal_df(df, serving_size = 50, serving_basis = 'Mass (g)'):
    '''
    Modifies dataframe to given serving size.  Returns None.
    '''
    try:
        df[numerics] = df[numerics].div(df[serving_basis], axis = 'index') * serving_size
    except:
        raise ValueError('Invalid serving_basis.  Use "Mass (g)" or "Calories."')
    return None

df['Protein (g)'].head()
df['Mass (g)'].head()
df.Calories.head()

recal_df(df, 50, 'Mass (g)')

#%%  dv - Dataframe of rda Value.
dv = df[rda.index] / rda
dv = dv.div(df.Calories, axis='index') * 50
dv = df.Food.to_frame().join(dv)
dv['Value'] = 0

#%%  Food names quick lookup
names = df.Food

#%%  Nutrient names w/out units
# Drops units from names for plots with relative values.
nutrient_names = pd.read_csv('data/rda.csv', index_col = "Stripped Name", encoding = 'latin1')
nutrient_names = nutrient_names['Nutrient (unit)']
nutrient_names

#%%  Key nutrients group
key_nutrients = ['Protein (g)', 
                 'Fiber (g)',
                 'Vitamin A (IU)',
                 'Thiamin (B1) (mg)',
                 'Vitamin C (mg)',
                 'Calcium (mg)', 
                 'Magnesium (mg)',
                 'Iron (mg)']    

#%%  Food finder
def food_finder(food_name):
    '''
    Searches dataframe for foods containing food_name
    Returns a list of IDs.
    '''
    L = []
    s = df.Food.map(str.lower)
    for i in s.index:
        if food_name.lower() in s.loc[i]:
            L.append(i)
    print(df.loc[L, 'Food'])
    if len(L) == 1:
        return L[0]
    else:
        return L

#f = food_finder('aPPle')
#df.loc[f, 'Food']     

#%%  Serving size checker
'''
Cheddar cheese
100 g ~ 404 cal
 50 g ~ 202 cal
'''

df.Calories.loc[1009]
