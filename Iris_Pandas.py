# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 12:23:38 2020

@author: Chiharu Ishida
"""

import pandas as pd
iris = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

iris.plot.scatter(x='sepal_length', y='sepal_width', title='Iris Dataset')
# =============================================================================
# #LINE CHART: in Pandas we don’t need to loop through each column because it automatically plots all available 
#numeric columns (at least if we don’t specify a specific column/s)
# =============================================================================

iris.drop(['class'], axis=1).plot.line(title='Iris Dataset')

#HISTOGRAM: In Pandas we can create a Histogram with the plot.hist method
iris['sepal_width'].plot.hist(title='Iris Dataset Sepal Width')

# =============================================================================
# Also easy to create multiple historgrams at once
# The subplots argument specifies that we want a separate plot for each feature 
# and the layout specifies the number of plots per row and column.
# =============================================================================

#changing bin size to 10
iris.plot.hist(subplots=True, layout=(2,2), figsize=(10, 10), bins=10)

# =============================================================================
# #BAR chart
# To plot a bar-chart we can use the plot.bar() method, but before we can call
# this we need to get our data. For this we will first count the occurrences using
# the value_count() method and then sort the occurrences from smallest to largest
# using the sort_index() method.
# =============================================================================

iris['sepal_length'].value_counts().sort_index().plot.bar()

#change to horizontal bar chart:
iris['sepal_length'].value_counts().sort_index().plot.barh()

#add grid. Panda's default is grid=False. Don't forget to capitalize True
iris['sepal_length'].value_counts().sort_index().plot.bar(grid=True)

#changing y-axis scale
iris['sepal_length'].value_counts().sort_index().plot.bar(grid=True, yticks=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

#creating average sepal-length bar chart

iris.groupby("class").sepal_length.mean().sort_values(ascending=False)[:5].plot.bar()
