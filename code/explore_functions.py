# -*- coding: utf-8 -*-
"""
Use to find top value foods, show profiles, and more.

Created on Wed Jun 19 08:04:39 2019
@author: Justin
"""
#%%  dv - Dataframe of rda Value.
# Doubled from data script.
dv = df[rda.index] / rda
dv = dv.div(df.Calories, axis='index') * 50
dv = df.Food.to_frame().join(dv)
dv['Value'] = 0


#%%  Presentation columns
# Max number of nutrients to show per plot.
key_nutrients = ['Protein (g)', 
                 'Fiber (g)',
                 'Vitamin A (IU)',
                 'Thiamin (B1) (mg)',
                 'Calcium (mg)']

#%%  Analyze food function   
def analyze_food(food, short_plot = True):
    '''
    Plots the top nutrients for a food.
    Returns the food's data series for further analysis.
    '''
    s = dv.loc[food]
    s = nutrient_names.map(s)
    s = s.sort_values()
    
    # Prepare set for plotting.
    ss = s
    if short_plot:
        ss = s.tail()
        
    plt.figure()
    ss.plot.barh()
    plt.xlim((0,1.5))
    plt.axvline(1, c = 'gray', ls = '--')
    plt.xlabel('RDA Value Supplied')
    plt.ylabel('')
    name = df.Food[food]
    plt.title(name)
    return s.sort_values(ascending = False).astype(float).round(2)

#%%
def analyze_food(food, short_plot = True):
    '''
    Plots the top nutrients for a food.
    Returns the food's data series for further analysis.
    '''
    s = dv.loc[food]
    s = nutrient_names.map(s)
    s = s.sort_values()
    
    # Prepare set for plotting.
    ss = s
    if short_plot:
        ss = s.tail()
        
    plt.figure()
    ss.plot.barh()
    plt.xlim((0,1.5))
    plt.axvline(1, c = 'gray', ls = '--')
    plt.xlabel('RDA Value Supplied')
    plt.ylabel('')
    name = df.Food[food]
    plt.title(name)
    return s.sort_values(ascending = False).astype(float).round(2)

#%%  Analyze foods for Jupyter
kn = ['Protein', 
      'Fiber',
      'Vitamin A',
      'Vitamin B1',
      'Vitamin C',
      'Calcium', 
      'Iron']

def analyze_food_kn(food):
    '''
    Plots key nutrients for a food.
    Returns the food's data series for further analysis.
    '''
    s = dv.loc[food]
    s = nutrient_names.map(s)
    
    ss = s[kn]       
    plt.figure()
    ss.plot.barh().invert_yaxis()
    plt.xlim((0,1.5))
    plt.axvline(1, c = 'gray', ls = '--')
    plt.xlabel('RDA Value Supplied')
    plt.ylabel('')
    name = df.Food[food]
    plt.title(name)
    
    return s.astype(float).round(2)

#analyze_food(1009)
    
  #%%  Plot Top Foods
def plot_top_foods(dfa, title = ''):
    '''
    Takes a dataframe with a 'Value' column.  
    Plots a graph and produces a series of top foods.
    '''
    try:        
        dfa.sort_values('Value', inplace = True)    
    except:
        raise Exception('DataFrame needs Value column.')
    dfa.tail(8).plot.barh(x = 'Food', y = 'Value')
    plt.ylabel('')
    plt.title(title)    
    return dfa[['Food', 'Value']].sort_values('Value', ascending = False).round(2)