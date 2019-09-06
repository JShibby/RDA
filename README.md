# RDA Project Overview
This project performs several analyses, all related to the topics of nutrition and dietary recommendations.
1. Analyzes foods for nutrient density.
2. Tests the RDA for 26 nutrients, to determine whether all are satisfiable by natural foods on a maintenance calorie intake.
3. Constructs an ideal diet.
4. Tests the US MyPlate dietary recommendations for average RDA satisfaction.

The project uses a selected subset of foods from the USDA's SR28 nutritional database.  The central code to the project is the creation of Gut and RandomGut Python classes, which simulate a person selecting and eating foods in small serving sizes (usually 50 grams) and absorbing their nutrients.  The construction of an ideal diet is treated as a complex version of the knapsack problem, and a complex, greedy version of knapsack algorithm is constructed to favor foods by nutrient density.

This project is an exercise in coding and data analysis; it does not represent nutrition science or medical advice.  

This repository contains all data and Python files needed for the project.  

## Explore the Data
This project **will contain** a Jupyter Notebook, which provides the user the opportunity to 
* Explore the dataset. 
* Visualize the nutritional contents of foods.
* Construct idealized diets by varying basic parameters of the Gut objects.
* Review full dietary results of Gut simulations.

