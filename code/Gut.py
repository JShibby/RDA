# -*- coding: utf-8 -*-
"""
Gut sim, using a loss function.  
Depends on data.

Created on Mon Jun  3 11:55:56 2019
@author: Justin
"""
#%%  Import
#from data import *

from numpy import random as nr
import warnings
warnings.filterwarnings("ignore", category = FutureWarning)

#%%  Presentation columns
# Max number of nutrients to show per plot.
key_nutrients = ['Protein (g)', 
                 'Fiber (g)',
                 'Vitamin A (IU)',
                 'Thiamin (B1) (mg)',
                 'Calcium (mg)']

#%%  Gut - Knapsack object
class Gut(object):
    '''
    Models a human gut as a knapsack.
    Main data is a dataframe called self.tracker.  
    Tracker index represents consumed.
    '''
    def __init__(self, df = df, calorie_limit = 2600, 
                 oversatisfaction_factor = 0.1, 
                 food_group_calories = {}):
        self.df = df
        self.calorie_limit = calorie_limit
        self.osf = oversatisfaction_factor
        self.food_group_calories = food_group_calories

        self.calories = 0
        self.it = 0   
        
        self.setup_tracker()
        self.nutrients = pd.Series(0, index = rda.index)
        self.run_sim()            

    def add_food(self, food):
        '''
        Food must be an index in the dataframe self.dfa.  
        The tracker is cumulative; previous nutrients must be added.
        '''       
        cal = round(self.calories + self.df.loc[food, 'Calories'], 1)

        if cal <= self.calorie_limit:
            self.tracker.loc[cal] = self.df.loc[food, self.tracker.columns]
            self.tracker.loc[cal, 'ID#'] = food
            self.tracker.loc[cal, rda.index] += self.nutrients
            self.nutrients = self.tracker.loc[cal, rda.index]
            self.calories = cal
            
        else:
            self.calories = self.calorie_limit
       
    def choose_food(self):
        '''
        Chooses food based on value function.
        t - target RDA level.
        r - scalar (<1) to ease penalty for oversatisfied nutrients.
        '''
        t = 1.5
        target = t * rda
        importance = (target - self.nutrients) / rda                 # Series
        importance = importance.map(lambda x: max(x, self.osf*x))
        increase = self.df[rda.index] / rda
        value = increase * importance                                    # DF
        value = value.mean(axis=1)                                   # Series
        value /= self.df.Calories
        value.sort_values(inplace=True)        
        food = value.index[-1]
        return food
    
    def continue_(self):
        '''
        Tests whether the simulation should continue.
        Test 1: Any nutrient is under the RDA.
        Test 2: The gut is not full by calories.
        '''        
        self.it += 1
        if self.it % 50 == 1:
            print('.', end = '  ')

        t1 = (self.nutrients / rda < 1).any()
        t2 = self.calories < self.calorie_limit
        return t1 and t2
    
    def get_nutrients(self):
        return self.nutrients
    
    def get_tracker(self):
        return self.tracker.iloc[1:]
    
    def get_unsatisfied(self):
        '''
        Returns a series of rda nutrients.  
        Unsatisfied nutrients denoted by 1, satisfied 0.
        '''
        x = self.nutrients / rda
        x = x < 1
        return x.map(int)

    def plot_nutrients(self, columns = key_nutrients, 
                       title_word = 'Selected Nutrients'):
        d2 = self.tracker[columns]
        d2 /= rda[columns]
        
        plt.figure()
        ax = d2.plot.line()
        ax.axhline(y=1, color='tab:gray', linestyle='--')
        ax.set_title(title_word + ' (Relative to RDA)', fontsize = 16)
        ax.set_ylim([0,1.5])  
        ax.set_xlabel('Calorie Point')
        ax.set_ylabel('Fraction RDA')
        
    def plot_satisfaction(self):
        t2 = self.tracker[rda.index] / rda
        t2 = t2.applymap(lambda x: int(x))
        t2 = t2.applymap(lambda x: min(1, x))
        count = t2.sum(axis=1)
        plt.figure()
        count.plot.line()
        plt.xlabel('Calorie Point')
        plt.ylabel('Nutrients Satisfied')
        plt.title('Nutrients Satisfied in Gut')
                  
    def run_sim(self):
        while self.continue_():
            food = self.choose_food()
            self.food = food
            self.add_food(food)
        print('Complete. \n')            
        self.show_results()

    def setup_tracker(self):
        '''
        Sets up an empty dataframe representing gut contents.
        index represents calories.
        '''
        columns = ['ID#', 'Food'] + list(rda.index)
        self.tracker = pd.DataFrame(columns = columns)
        self.tracker.loc[0] = 0
        self.tracker.loc[0, 'Food'] = '(Start)'
        
        
    def show_results(self):
        # The last entry in the tracker is the final cumulative values.
        s = self.tracker.iloc[-1][rda.index] / rda
        s = nutrient_names.map(s)
        s = s.astype(float).round(2)
        s.sort_values(ascending = False, inplace = True)
        
        med = s.describe()['50%'].round(2)
        print('Median satisfaction:', med)
        unsatisfied = (s < 1).value_counts()[True]
        print('Unsatisfied nutrients:', unsatisfied, '/', len(s))
                
        return s
    
        
    def __str__(self):
        return 'Gut with ' + str(self.calories) + ' calories.'


#%%  Run
recal_df(df, 50, 'Mass (g)')
dfa = df.copy()

calories = 2600
choice_method = 'value'

osf = 0.1
g = Gut(calorie_limit = calories,  
        oversatisfaction_factor = osf, 
        df = dfa)

tracker = g.get_tracker()
tracker
tracker.Food.value_counts()

g.plot_nutrients()
g.plot_satisfaction()
   
#%%  Export
#tracker.Food.value_counts().to_csv('data/diet data.csv')

