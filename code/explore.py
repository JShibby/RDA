# -*- coding: utf-8 -*-
"""
Use to find top value foods, show profiles, and more.

Created on Wed Jun 19 08:04:39 2019
@author: Justin
"""
#%%  More Nutrient Groups
macros = ['Protein (g)', 'Carbohydrates (g)', 'Fiber (g)']

vitamins_water_soluble = ['Thiamin (B1) (mg)',
       'Riboflavin (B2) (mg)', 'Niacin (B3) (mg)', 'Vitamin B5 (mg)',
       'Vitamin B6 (mg)', 'Folate (B9) (mcg)', 'Vitamin B12 (mcg)',
       'Vitamin C (mg)', 'Choline (mg)']

vitamins_fat_soluble = ['Vitamin A (IU)','Vitamin D (mcg)', 'Vitamin E (mg)']

electrolytes = ['Sodium (mg)', 'Potassium (mg)']

minerals_major = ['Calcium (mg)', 'Phosphorus (mg)', 'Magnesium (mg)']

minerals_trace = ['Copper (mg)', 'Fluoride (mcg)', 'Iron (mg)', 
       'Manganese (mg)', 'Selenium (mcg)', 'Zinc (mg)']
  
#%%  Key Nutrient Histograms
for n in key_nutrients:
    plt.figure()
    df[n].plot.hist()
    plt.title(n)
    
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

#%%  Food Plot
food = food_finder('spinach')
#food = 19296
s = analyze_food(food, short_plot = True)
s

#%%  Dataset Info
len(dfo)    # SR28
len(flo)    # Curated food list, all inclusive
len(df)     # Actual df

s = dfo['Food Group'].value_counts()
s['Beef Products']

# Plot of foods per category
s = df['Food Group'].value_counts()
plt.figure()
s.sort_values().plot.barh()
plt.title('Number of Foods per Category')


#%%  Food Means
# This cell investigates main foods from the basic diet / hypothesis test.
dv.Value = 0 
dv.Value = dv[rda.index].mean(axis = 1)

# Main foods from ideal diet.
idx = ['spinach', 'okra', 'turnips', 'honey']
[food_finder(i) for i in idx]
idx = [11457, 11279, 11565, 19296]
dv.loc[idx, ['Food', 'Value']].round(2)
