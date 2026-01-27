import pandas as pd
import numpy as np
# SERIES
# val = [67,11,26,78]
# val2 = ['A','B','C','D']
# s = pd.Series(val,val2)
# print(s)
# print(s['A'])

# cars = {'tesla':2 , 'mercedes':4, 'BMW': 6}--- shortcut
# my_var = pd.Series(cars)
# print(my_var)
# print(my_var['tesla'])

# DATAFRAMES:

# from numpy.random import randn
# my_data = randn(4,3) #rows and column
# my_rows = ['A','B','C','D']
# my_col = ['Monday','Tuesday','Wednesday']

# my_df = pd.DataFrame(my_data,my_rows,my_col)
# print(my_df)

# my_df = pd.read_csv('dog_data.csv') # for specific row
# print(my_df.loc[[0,5,3]])
 
# print(my_df.head())
# print(my_df.tail())
# print(my_df.info())
# print(my_df.shape)
# print(my_df.ndim)
# print(my_df.dtypes)
# print(my_df.describe())
# print(my_df['Breed'].describe())-- describe a specific column 
# print(my_df['Breed'])  -- select a specific column using brackets
# print(my_df.iloc[:,1]) -- specific column using location 
# print(my_df['Country of Origin'].value_counts(normalize = True)) --- give the relative frequency - percentage 
# print(my_df['Country of Origin'].value_counts()['Germany'])  -- counts the no of items
# print(my_df.groupby('Country of Origin').count()) -- counts the items alphabetically 

# CREATE A NEW COLUMN :
# gender = ['male' ,'female', 'male','male','female','male','female','female',]
# my_df["Gender"] = gender
# print(my_df)

# my_df["alive/dead"]= [True]*len(my_df)-- add the default value
# print(my_df)

# my_df["show dog"] = [np.nan]*len(my_df)
# print(my_df)
# my_df.insert(1,"adopted",[True]*len(my_df))
# print(my_df)

# my_df2 = my_df.assign(horse = [False]*len(my_df))
# print(my_df2)
# print(my_df)

# print(my_df.drop("Gender",axis=1)) -- delete column temp
# print(my_df.drop("Gender",axis=1,inplace = True))-- delete the column permenantely
# print(my_df)

# print(my_df.drop(7,axis = 0)) -- delete the row temp


# my_df2 = my_df.loc[[1,4],['Country of Origin','Breed']]--- for specific name u want form column 
# print(my_df2)

# my_df2= (my_df == 'Germany')  #conditional statement
# # my_df2 = (my_df[my_df=='Germany'])
# print(my_df2)

# FILTERING:
# EG-1
# data = {
#     "name" : ['rohan' , 'harsh','atharv','om'],
#     "age" : [27,26,24,21],
#     "city": ['pune','bhusawal','nashik','mumbai']
# }
# df = pd.DataFrame(data)
# #filter the row based on condition

# new_data = df[df["age"]>=25]
# print(new_data)

# EG-2
# data = {
#     'name' : ['rohan','sai','meet','anas','vedant','monu','heet'],
#     'score': [98 , 94, 88, 78 , 45, 90, 75]
    
# }
# df = pd.DataFrame(data)
# df = df[(df['score'] >=80) &(df['score']<=95) ]
# print(df)

data = {
    'name' : ['rohan','sai','meet','anas','vedant','monu','heet'],
    'score': [98 , 94, 88, 78 , 45, 90, 75]
    
}
df = pd.DataFrame(data)
# df.loc[(df["score"] > 40 ) & (df["score"]<=80)]
# df.loc[df['score'].between(40,80)] -- easy and better way 
print(df)





