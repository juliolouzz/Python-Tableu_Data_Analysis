import pandas as pd

# file_name = pd.read_csv('file.csv') <--- how to read csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

#summary of the data
data.info()

#working with calculations
#Defining variables
#CostPerTransction = CostPerItem * NumberofItemsPurchases
#Call input from column --> variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransction = CostPerItem * NumberOfItemsPurchased

#adding new column to a dataframe

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales per transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales - Cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (sales - cost)/cost [This is the percentage that you sold above]

data['Markup'] = (data['ProfitPerTransaction']) / data['CostPerTransaction']

#Rounding the decimals to only 2 decimals in Markup

data['Markup'] = round(data['Markup'], 2)

#Combining data columns (fields) year, month, day
#Converting data types  int to str 

data['DateOfPurchase'] = data['Day'].astype(str) + '-' + data['Month'] + '-' + data['Year'].astype(str)

#Using the split to split clients Keywords
#new_var = column.str.split('sep' , expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand = True)

#creating new columns with the data splited

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#using replace function to clear things on columns

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']' , '')

#using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files
#bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merge_df =pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#removing columns that you don't need more
#df = df.drop('column_name' , axis = 1)

data = data.drop(['Day', 'Month', 'Year'], axis = 1)

#export into CSV

data.to_csv('ValueInc_Cleaned.csv', index = False)




