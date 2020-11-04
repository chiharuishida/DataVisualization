# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:27:15 2020

@author: Chiharu Ishida
"""

import pandas as pd
iris = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
print(iris.head())

import matplotlib.pyplot as plt
# create a figure and axis
fig, ax = plt.subplots()

# scatter the sepal_length against the sepal_width
ax.scatter(iris['sepal_length'], iris['sepal_width'])
# set a title and labels
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')

# create color dictionary
colors = {'Iris-setosa':'r', 'Iris-versicolor':'g', 'Iris-virginica':'b'}
# create a figure and axis
fig, ax = plt.subplots()
# plot each data-point
for i in range(len(iris['sepal_length'])):
    ax.scatter(iris['sepal_length'][i], iris['sepal_width'][i],color=colors[iris['class'][i]])
# set a title and labels
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')

#In Matplotlib we can create a line chart by calling the plot method.
# We can also plot multiple columns in one graph, by looping through 
#the columns we want and plotting each column on the same axis
# get columns to plot
columns = iris.columns.drop(['class'])
# create x data
x_data = range(0, iris.shape[0])
# create figure and axis
fig, ax = plt.subplots()
# plot each column
for column in columns:
    ax.plot(x_data, iris[column], label=column)
# set title and legend
ax.set_title('Iris Dataset')
ax.legend()

# create figure and axis
#In Matplotlib we can create a Histogram using the hist method
fig, ax = plt.subplots()
# plot histogram
ax.hist(iris['petal_width'])
# set title and labels
ax.set_title('Petal widths')
ax.set_xlabel('Width')
ax.set_ylabel('Frequency')


# create a figure and axis 
#A bar chart can be created using the bar method
#The bar-chart isn’t automatically calculating the frequency of 
#a category so we are going to use pandas value_counts function 
#to do this. The bar-chart is useful for categorical data that 
#doesn’t have a lot of different categories (less than 30) because 
#else it can get quite messy.
fig, ax = plt.subplots() 
# count the occurrence of each class 
data = iris['sepal_width'].value_counts() 
# get x and y data 
sepal_width = data.index 
frequency = data.values 
# create bar chart 
ax.bar(sepal_width, frequency) 
# set title and labels 
ax.set_title('Sepal Width and Class') 
ax.set_xlabel('Width') 
ax.set_ylabel('Frequency')
