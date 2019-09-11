# -*- coding: utf-8 -*-
"""
Explores top foods by total nutrient density.

Created on Wed Jun 19 08:04:39 2019
@author: Justin
"""


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