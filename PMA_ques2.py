#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd  
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[78]:


df = pd.read_excel('PMA_data.xlsx', sheet_name = 1)
df

# convert to data frame using Pandas

#uni = pd.DataFrame(df.data, comulmns = df.feature_names)
#uni.head()


# In[79]:


#delete ID number
df.drop(columns = ['ID number'])


# In[80]:


#replace blanks with mean average

df.fillna(df.mean(), inplace = True)


# In[81]:


print(df.loc[0,:])

# I dont know why Id number still exist after removing?


# In[82]:


df.to_excel('output.xlsx')


# In[84]:


#drop the rows which are empty

df = df.dropna()

df.to_excel('output.xlsx')

# add the target value (Applicants total)
#boston['MV'] = boston_dataset.target
#df['Applicants total'] = df.target
#df[0] = df.target



# In[85]:


df.isnull().sum()


# In[94]:


df.replace(to_replace=['No', 'Yes'], value=[0, 1])



# In[95]:


# create a correlation matrix rounding to one decimal point
correlation_matrix = df.corr().round(1)

# print a correlation heat map
sns.heatmap(data = correlation_matrix, annot=True)



# In[96]:


# remove the correlated variable and the Y value
# the Y value is going to be loaded separately
#df = df.drop(['Applicants total'], axis=1)

df

# why still exist No Yes when I replaced them already with numbers?
# how Applicants total column dropped?


# In[100]:


# remove the correlated variable and the Y value
# the Y value is going to be loaded separately

#df = df.drop(['Applicants total'], axis=1)  this line has an error since it was dropped somehow
df.head()

# create a separate Y value
df_Y = df.target

#I understand that DataFrame has no function Target. but since we used our data we didnt use package "sklearn" which target belong to


# In[ ]:


# split data into training and test
from sklearn.model_selection  import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(df, df_Y, test_size = 0.2, random_state=5)

