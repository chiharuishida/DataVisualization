# Import Libraries:
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

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

# importing the model
regressor = LinearRegression()

# Regression
regressor.fit(x, y)

model = sm.OLS(y, x).fit()
## Inspect the results
print(model.summary())