# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 14:08:18 2022

@author: Julio PC
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#how to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    
#transform to dataframe
loandata = pd.DataFrame(data)

#finfing uniqe values for te pupose column
loandata['purpose'].unique()

#describe the data
loandata.describe()

#decribe the data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#uisng EXP to get annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annual_income'] = income

#FICO Score
ficocat = []
length = len(loandata)
for x in range(0, length):
    category = loandata['fico'][x]
    if category >= 300 and category < 400:
        cat = 'Very Poor'
    elif category >= 400 and category < 600:
        cat = 'Poor'
    elif category >= 601 and category < 660:
        cat = 'Fair'
    elif category >= 660 and category < 700:
        cat = 'Good'
    elif category >= 700:
        cat = 'Excellent'
    else:
        cat = 'Unknown'
    ficocat.append(cat)

ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat

#df.loc as conditional statements
# df.loc[df[column_name] condition, new_column_name] = 'value if the condition is met'

#for interest rates, a new column is wanted. rate >0.12 then high, else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

#number of loans/rows by fico.category
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar()
plt.show()

purposecount = loandata.groupby(['purpose']).size()


#scatter plots

ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint)
plt.show()

#wrinting to csv
loandata.to_csv('loan_cleaned.csv', index = True)





