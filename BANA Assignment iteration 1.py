#!/usr/bin/env python
# coding: utf-8

# ### Import important packages like pandas and numpy

# In[1]:


import pandas as pd
import numpy as np


# ### Store your directory and file names in a variable for code reusability

# In[37]:


location='C://Backup//DataPartition//RIT Course Work//BANA//Assignment 1//'
file1='NCHS_-_Leading_Causes_of_Death__United_States.csv'
file2='nst-est2018-01.xlsx'


# ### Reading the file into data frames

# In[40]:


df1=pd.read_csv(location+file1)
df2=pd.read_excel(location+file2,header=None)


# ### Exploring and viewing the data

# In[27]:


df1.head()


# In[53]:


df2.head()


# In[32]:


df1.info()


# In[33]:


df2.info()


# ### Drop the first two rows for data cleaning purposes

## Pull the column title "Geographic Area"
label = df2.iloc[2,0]

## Pull the remainder row containing the header
headers = df2.iloc[3:4]

## Pull the values within the rows
headers.values

## Create new column header array
newColumnHeaders = []

## Add the first value to it
newColumnHeaders.append(label)

## Add the remainder values to it
for x in headers.values[0]:
    if isinstance(x, float):
        if np.isnan(x):
            continue
        newColumnHeaders.append(int(x))
        continue
    newColumnHeaders.append(x)

newColumnHeaders

## Make the clean data frame with the values from United States to Puerto Rico
cleanDF = pd.DataFrame(df2.iloc[4:-5])
## Assign the new column headers
cleanDF.columns = newColumnHeaders
## Get rid of row number 60 as it was just an empty row
cleanDF.dropna()
