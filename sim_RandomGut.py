# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 20:52:24 2019

@author: justi
"""

#%%  Simulation
columns = ['Median', 'Unsatisfied'] 
tracker = pd.DataFrame(columns = columns)
unsat = pd.Series(0, index = rda.index)

nr.seed(0)
its = 1000

t = time.time()
print('Simulating', end = '  ')
for it in range(its):
    if it % 100 == 1:
        print('.', end = '  ')        
    r = RandomGut(df = dfa, food_group_calories = food_group_calories)
    tracker.loc[it] = r.get_results()
    unsat += r.get_unsatisfied()

tracker.Unsatisfied = tracker.Unsatisfied.astype(int)
unsat /= its
unsat = round(unsat, 2)
print()
print('Complete.')

t = time.time() - t
t = round(t/60, 1)
print('Time (min):', t)
#print('\a')

#%%  Histograms
tracker.Median.mean()
tracker.Unsatisfied.mean()

fig, axes = plt.subplots(nrows=1, ncols=2, figsize = (10, 4))
# With one row, you only need the one index label.
tracker.Median.plot.hist(ax = axes[0], title = 'Median Satisfaction')
#tracker.Unsatisfied.plot.hist(ax = axes[1], title = 'Number Unsatisfied')

s = tracker.Unsatisfied.astype(int).value_counts()
s.sort_index(inplace = True)
s.plot.bar(ax = axes[1], title = 'Number Unsatisfied Nutrients', color = 'b')
        
plt.tight_layout()
plt.show()

#%%  Unsatisfied Nutrients
plt.figure()
u = unsat[unsat > .05].sort_values()
u.plot.barh()
