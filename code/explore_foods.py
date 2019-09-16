# -*- coding: utf-8 -*-
"""
Use to find top value foods, show profiles, and more.
  
Created on Wed Jun 19 08:04:39 2019
@author: Justin
"""
#%%  Key Nutrient Histograms
for n in key_nutrients:
    plt.figure()
    df[n].plot.hist()
    plt.title(n)
    
#%%  Food Plot
food = food_finder('spinach')
#food = 19296
s = analyze_food(food, short_plot = True)
s

#%%  Rote Plot
short_plot = False

s = dv.loc[food]
s = nutrient_names.map(s)

plt.figure()
s.plot.barh().invert_yaxis()


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
