# Import Libraries:
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the data by using the read_csv method on the Pandas library and passing
# it the location of our data.
dataset = pd.read_csv('boston.csv')

# =============================================================================
# #Alternatively try reading from URL by entering the script below:
# url="https://raw.githubusercontent.com/chiharuishida/DataVisualization/main/Boston.csv"
# dataset = pd.read_csv(url)
# 
#Note: if using github, it has to be the *raw*. You should use the url given by the Raw link in the github page for getting raw csv response
# =============================================================================


# The next step is to look at what our data contains and it shape
#\n inserts an extra line
print('\nFirst 5 entries\n')
print(dataset.head(5))

print('First 5 entries')
print(dataset.head(5))

#want to know how many rows and how many columns?
total_row, total_col = dataset.shape
print('Total rows    : ', total_row)
print('Total columns : ', total_col)

#print summary statistics
print (dataset.describe())

#if columns are truncated, then use this. where says "none" change to any number if you like
pd.set_option('display.max_columns', None)
print (dataset.describe())

# =============================================================================
# In the Boston dataset, the first column did not have a header (hence 'unnamed: 0')
# #Note: axis=1 indicates columns. axis=0 indicates index (roughly the same as rows)
# # we are using X to refer to predictor vairables, and Y to Target. Here we are including all
# #columns/variables besides the 'unnamed' and 'medv'
# =============================================================================

x = dataset.drop(['Unnamed: 0', 'medv'], axis=1)
y = dataset['medv']

# To split our dataset into train and test splits (test here refers to validation dataset as we previously learned)
#For more about how Skleanr's train_test_split works, go to https://www.bitdegree.org/learn/train-test-split'
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# importing the model
regressor = LinearRegression()

# Regression
regressor.fit(x_train, y_train)


import statsmodels.api as sm

model = sm.OLS(y_train, x_train).fit()
## Inspect the results
print(model.summary())