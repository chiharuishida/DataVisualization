# Import Libraries:
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

url="https://raw.githubusercontent.com/chiharuishida/DataVisualization/main/Boston.csv"
dataset = pd.read_csv(url)

#to view the first 15 rows of data
dataset.head(15)

#for a quick view of the variables in the dataset:
dataset.info()

#to view descriptive stats for the continous variables
dataset.describe()

# =============================================================================
# In the Boston dataset, the first column did not have a header (hence 'unnamed: 0')
# Note: axis=1 indicates columns. axis=0 indicates index (roughly the same as rows)
# we are using X to refer to predictor vairables, and Y to Target. Here we are including all
# columns/variables besides the 'unnamed' and 'medv'
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

