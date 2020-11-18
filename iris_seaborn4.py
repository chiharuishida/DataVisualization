# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 13:10:24 2020

@author: Chiharu Ishida
"""

# =============================================================================
# Seaborn is a Python data visualization library based on Matplotlib. It provides 
# a high-level interface for creating attractive graphs.
#Seaborn has a lot to offer. You can create graphs in one line that would take 
#you multiple tens of lines in Matplotlib. Its standard designs are awesome and 
#it also has a nice interface for working with pandas dataframes.
# =============================================================================
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#first, read the data file stored locally. 
iris = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
#Alternatively, you can read data directly from my URL:
# url="https://https://raw.githubusercontent.com/chiharuishida/DataVisualization/main/iris.csv"
# iris = pd.read_csv(url)

# =============================================================================
# We can use the .scatterplot method for creating a scatterplot, and just as in 
# Pandas we need to pass it the column names of the x and y data, but now we also
#  need to pass the data as an additional argument because we aren’t calling the 
#  function on the data directly as we did in Pandas.
# =============================================================================

#to obtain descriptive stats, run this:
print (iris.describe())

sns.scatterplot(x='sepal_length', y='sepal_width', data=iris)

# =============================================================================
# We can also highlight the points by class using the hue argument, which is a 
# #lot easier than in Matplotlib.
# =============================================================================
sns.scatterplot(x='sepal_length', y='sepal_width', hue='class', data=iris)

# =============================================================================
# To create a line-chart the sns.lineplot method can be used. The only required 
#argument is the data, which in our case are the four numeric columns from 
#the Iris dataset. We could also use the sns.kdeplot method which rounds of 
#the edges of the curves and therefore is cleaner if you have a lot of outliers 
#in your dataset.
# =============================================================================

sns.lineplot(data=iris.drop(['class'], axis=1))


# =============================================================================
# #To create a histogram in Seaborn we use the sns.distplot method. We need to pass 
# it the column we want to plot and it will calculate the occurrences itself. 
# =============================================================================

#Bar chart. 
sns.countplot(iris['sepal_width'])

#change color to red
sns.countplot(iris['sepal_width'], color='r')


#heatmap
sns.heatmap(iris.corr(), annot=True)

cor = iris.corr()
plt.figure(figsize=(12,6))
sns.heatmap(cor, annot=True)
plt.title('Correlation in Iris Data')
plt.show()

#if you don't like the size of heatmap, change plt.figure(figsize=(12,6)) from 
#12 and 6 to larger number

#Change colors to Blue
#https://python-graph-gallery.com/92-control-color-in-seaborn-heatmaps/
cor = iris.corr()
plt.figure(figsize=(12,6))
sns.heatmap(cor, annot=True, cmap="Blues")
plt.title('Correlation in Iris Data')
plt.show()

#pair plot
sns.pairplot(iris)