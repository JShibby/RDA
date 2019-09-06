# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 10:55:53 2019

@author: justi
"""
#%%  Packages
import numpy.random as nr
import time

#%%  Food Groups 2
groups = {'Fruits and Fruit Juices': 'Fruits',
          'Vegetables and Vegetable Produ': 'Vegetables',
          'Cereal Grains and Pasta': 'Grains',
          'Baked Products': 'Grains',
          'Finfish and Shellfish Products': 'Protein',
          'Lamb, Veal': 'Protein',
          'Nut and Seed Products': 'Protein',
          'Poultry Products': 'Protein',
          'Beef Products': 'Protein',
          'Pork Products': 'Protein',
          'Legumes and Legume Products': 'Protein',
          'Dairy and Egg Products': 'Dairy',
          'Snacks': 'Snacks',
          'Sweets': 'Snacks',
          'Beverages': 'Snacks',
          'Fats and Oils': 'Snacks'}

#%%  Calorie goals
food_group_calories = {'Fruits': 300,
     'Vegetables': 150,
     'Grains': 1100,
     'Protein': 400,
     'Dairy': 450,
     'Snacks': 200}

#%%
class RandomGut(Gut):
    '''
    Like the Gut, but chooses foods randomly based on food groups, 
      following ChooseMyPlate.Gov.
    Relies on food_group_calories, which was extraneous in Gut.
    ''' 
    def run_sim(self):
        for food_group in food_group_calories.keys():
            food_set = self.choose_food_set(food_group)
            for food in food_set:
                self.add_food(food)
        
    def choose_food_set(self, food_group):
        '''
        Chooses a the set of foods for a whole food group.
        Returns a list of indices representing foods.
        Assumes fixed calorie goals, enforces self.calorie_limit.
        '''
        # Get defensive programming.
        s = dfa.loc[dfa['Food Group'] == food_group].index
        food_set = []
        group_calories = self.food_group_calories[food_group]
        while (group_calories > 0) and (self.calories < self.calorie_limit):
            food = nr.choice(s)
            group_calories -= dfa.Calories.loc[food]
            food_set.append(food)
#        print(dfa.Food.loc[food_set])
#        print()
        return food_set
        
    def get_results(self):
        s = self.nutrients / rda
        s = nutrient_names.map(s)
        s = s.astype(float).round(2)
        s.sort_values(ascending = False, inplace = True)
        
        med = s.describe()['50%'].round(2)
        unsatisfied = (s < 1).value_counts()[True]
        s = {'Median': med,
             'Unsatisfied': unsatisfied}
        return pd.Series(s)

#%%  Run
dfa = df.copy()
recal_df(dfa, 50, 'Calories')
dfa['Food Group'] = dfa['Food Group'].map(groups)

r = RandomGut(df = dfa, food_group_calories = food_group_calories)
tracker = r.get_tracker()
tracker.Food

