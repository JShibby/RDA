# -*- coding: utf-8 -*-
"""
Shows which food is the best source for each nutrient.
Builds a dataframe of best sources and exports it.
Can show the top sources for a single nutrient.
Depends on data, explore.

Created on Wed Jun 19 08:04:39 2019
@author: Justin
"""
#%%  Import
import matplotlib.pyplot as plt

#%%  Best sources - build dataframe.
nutrients = rda.index
foods = []
values = []

for nutr in nutrients:
    # Takes the top food for a given nutrient.
    a = dv[nutr].sort_values(ascending = False).head(1)
    foods.append(names[a.index[0]])
    values.append(a.iloc[0].round(2))
    
best_sources = pd.DataFrame(
        {'Food': foods,
         'Prop. RDA': values}, 
         index = nutrient_names.index)
best_sources 

# food_sum (summary) - just the foods that appear as best sources.
food_sum = best_sources.Food.value_counts()
food_sum

#%%  Review Best Sources
# short shows the number of nutrients that share a best-source food
short = food_sum.loc[food_sum > 1]
food_sum.sum()
short.sum()

food = food_sum.index[0]
best_sources.loc[best_sources.Food == food]

food = 'Mushrooms, morel'
best_sources.loc[best_sources.Food == food]

#%%  Top sources, single nutrient.
nutrient = 'Calcium (mg)'
s = dv[['Food', nutrient]]
s.set_index('Food', inplace = True)
s[nutrient].sort_values().tail(10).plot.barh()
plt.title('Top Sources for ' + nutrient)
plt.title('Top Sources for Calcium per Calorie')
plt.ylabel('')

#%%  Export
#best_sources.to_csv('data/best sources.csv')
#short.to_csv('data/best sources - short.csv')


