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

dataset.head(15)
#print summary statistics
print (dataset.describe())

# =============================================================================
# In the Boston dataset, the first column did not have a header (hence 'unnamed: 0')
# #Note: axis=1 indicates columns. axis=0 indicates index (roughly the same as rows)
# # we are using X to refer to predictor vairables, and Y to Target. Here we are including all
# #columns/variables besides the 'unnamed' and 'medv'
# =============================================================================

x = dataset.drop(['Unnamed: 0', 'medv'], axis=1)
y = dataset['medv']

#alternative way of writing the X is:
#x = dataset[['var1','var2','var3','var4']]
#the drop function is good to know as well if you are entering lots of X variables
#and just a couple excluded from the model. That way you don't have to write all the variable names

# importing the model
regressor = LinearRegression()

model = sm.OLS(y, x).fit()
## Inspect the results
print(model.summary())



