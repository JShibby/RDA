# -*- coding: utf-8 -*-
"""
Explores top foods by total nutrient density.

Created on Wed Jun 19 08:04:39 2019
@author: Justin
"""
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

#%%  Top foods by nutrient density (50 cal)
# Value column
dv['Value'] = (dv[rda.index].mean(axis=1))

title = 'Top Foods by Mean Nutrient Density (50 cal)'
s = plot_top_foods(dv, title)
s.head(10)

#%%  Top foods by median nutrient density
# Rewrite the total density value column.
dv['Value'] = (dv[rda.index].median(axis=1))

title = 'Top Foods by Median Nutrient Density (50 cal)'
s = plot_top_foods(dv, title)
s.head(10)

#%%  Top foods by mass
d2 = df.Food
d2 = d2.to_frame().join(df[rda.index])
d2[rda.index] /= rda
d2['Value'] = (d2.mean(axis=1))

title = 'Top Foods, Mean Nutritional Value by Mass (50 g)'
s = plot_top_foods(d2, title)
s.head(10)

#%%  Review Foods
food = food_finder('oyster')
s = analyze_food(food)
s