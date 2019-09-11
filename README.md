# RDA Project Overview
This project performs several analyses, all related to the topics of nutrition and dietary recommendations.
1. Analyzes foods for nutrient density.
2. Tests the RDA for 26 nutrients, to determine whether all are satisfiable by natural foods on a maintenance calorie intake.
3. Constructs an ideal diet, based purely on the numerical data.
4. Tests the US MyPlate dietary recommendations for average RDA satisfaction.

The project uses a selected subset of foods from the USDA's SR28 nutritional database.  The central code to the project is the creation of Gut and RandomGut Python classes, which simulate a person selecting and eating foods in small serving sizes (usually 50 grams) and absorbing their nutrients.  The construction of an ideal diet is treated as a complex version of the knapsack problem, and a complex, greedy version of knapsack algorithm is constructed to favor foods by nutrient density.

This project is an exercise in coding and data analysis; it does not represent nutrition science or medical advice.  

This repository contains all data and Python files needed for the project.  

## Data Report
This repository contains a data report, **"Is It Possible to Satisfy the RDA?"** (top level).  This report details the methodology and results of the project.

## Companion Jupyter Notebook 
This repository contains a Jupyter Notebook, **[RDA_Jupyter](https://github.com/JShibby/RDA/blob/master/code/RDA_Jupyter.ipynb)**.  This  provides the user the opportunity to:
* Explore the dataset.
* Visualize the nutritional contents of foods.
* Explore the best sources of nutrients.
* Simulate a random diet based on MyPlate dietary recommendations, and review that diet in detail.

At the time of writing, GitHub.com is failing to run the notebook.  If that is the case, the user can still review the notebook, but without the ability explore, here:
* [RDA_Jupyter on NBViewer](https://nbviewer.jupyter.org/github/JShibby/RDA/blob/master/code/RDA_Jupyter.ipynb)

## The Code
The code includes the following files, which may be treated as having a linear order, as later notebooks have some dependencies on earlier ones.
1. **data.py** - Imports and processes the data.  Creates these objects:
    * `df` - Pandas Dataframe of foods and nutrients.
    * `rda` - Pandas Series of nutrient RDA.
    * `food_finder()` - Helps the user locate a food by name in the dataframe.
    * `recal_df()` - Adjusts the dataframe to a new serving size, either in grams or calories.
2. **explore_functions.py** - Creates food analysis function for visualizing nutrients.
    * `analyze_food()` - Plots a foods top nutrients, and returns a sorted list of the nutrients it contains.
5. **Gut.py** - Creates the `Gut` class.  Tests satisfiability and constructs an ideal diet.
6. **RandomGut.py** - `RandomGut` is a subclass of `Gut` that chooses foods from food groups randomly, according to dietary plan.
7. **sim RandomGut.py** - Tests the MyPlate dietary recommendations by simulating `RandomGut` multiple times and aggregating results.

The code includes several data exploration scripts as well.
