#!/usr/bin/env python
# coding: utf-8

# ### Import important packages like pandas and numpy

# In[216]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ### Store your directory and file names in a variable for code reusability

# In[217]:


location='C://Backup//DataPartition//RIT Course Work//BANA//Assignment 1//'
file1='NCHS_-_Leading_Causes_of_Death__United_States.csv'
file2='nst-est2018-01.xlsx'


# ### Reading the file into data frames

# In[218]:


df1=pd.read_csv(location+file1)
df2=pd.read_excel(location+file2,header=None)


# ### Exploring and viewing the data

# In[5]:


df1.head()


# In[6]:


df2.head()


# In[12]:


df1.info()


# In[7]:


df2.info()


# ### Drop first two cells for data cleaning purposes

# In[219]:


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


# Use markdown to add your important comments 
# to create a markdown,add a cell above comment
# change the option from code to markdown
# use # for heading 1, ## for heading two and so on...(one space after #)
# ## please delete this before submitting

# # Question1 Sub question 2
# 
# 
# ## What are top 4 leading causes of death?

# In[232]:


# df1
# df1.columns

# ### Get the four leading causes of Deaths

## Should it be by year? should we just aggregate all deaths specific to a cause name?

# ### Get the Years column sorted
df1_sorted_by_year = df1.sort_values(by=['Year'])

df1_sorted_by_year # 10296 rows

# ### Get all the unique causes: 11 Unique Causes (936 each)
df1_sorted_by_year.iloc[0:, 1].value_counts()
"""
All Causes                                                               936
Alzheimer's disease (G30)                                                936
Chronic lower respiratory diseases (J40-J47)                             936
Nephritis, nephrotic syndrome and nephrosis (N00-N07,N17-N19,N25-N27)    936
Malignant neoplasms (C00-C97)                                            936
Accidents (unintentional injuries) (V01-X59,Y85-Y86)                     936
Diabetes mellitus (E10-E14)                                              936
Cerebrovascular diseases (I60-I69)                                       936
Influenza and pneumonia (J09-J18)                                        936
Intentional self-harm (suicide) (*U03,X60-X84,Y87.0)                     936
Diseases of heart (I00-I09,I11,I13,I20-I51)                              936
Name: 113 Cause Name, dtype: int64
"""

## Display only these three columns 
df1_causes_and_death = df1_sorted_by_year[['113 Cause Name', 'Cause Name', 'Deaths']]
# df1_causes_and_death

#####################################################################
### The Below was used to help understand one type of cause of death

## Find the unique count of the causes
# df1_causes_and_death.iloc[0:, 1].value_counts()


## Get the deaths for a specific cause name
# clrd_deaths = df1_causes_and_death[df1_causes_and_death.iloc[0:,1].isin(['CLRD'])]
# clrd_deaths

## Get the cumulative count: 4869452 Deaths by CLRD
# clrd_deaths.iloc[0:,2].agg('sum')
#####################################################################

## Use pivot table to help aggregate all the causes and summing their deaths
total_deaths_per_causes = pd.pivot_table(df1_causes_and_death,
                                         values='Deaths',
                                         index=['Cause Name'],
                                         #columns=['113 Cause Name'],
                                         aggfunc=np.sum)

#total_deaths_per_causes

## Sort the pivot table in descending order
deaths_descending = total_deaths_per_causes.sort_values(by=['Deaths'], ascending=False)
# deaths_descending

## Display the top 4
top_4_deaths = deaths_descending.iloc[1:5]
top_4_deaths


# # Question1 Sub question 3
# 
# 
# ## Do individual states show the same four leading causes of death??

# In[319]:


df1.head()


##Picking up data only for deaths,states and cause name

df1_deaths_states_all=df1.loc[:,['Deaths','State','Cause Name']]

###Sort the data with death 
df1_deaths_states_all=df1_deaths_states_all.sort_values(by='Deaths',ascending=False)

df1_deaths_states_all=df1.groupby(['State','Cause Name'],as_index=False)['Deaths'].


# # Question 1 Part 1
# ## Are Americans facing increasing, decreasing, or steady likelihood of death?

# In[31]:


df1.head()

df1_likelihood=df1.groupby('Year').agg('sum')
df1_likelihood


# ##  plot and check if there is a increase, decrease or steady likelihood of deaths

# In[71]:


plt.figure()
plt.ylabel("Deaths per Year")
plt.xlim(1998,2016)
plt.ylim(50000,100000)
plt.xlabel("Year")
plt.title("Deaths likelihood for every year from 1999 to 2006")

plt.plot(df1_likelihood.index,df1_likelihood.values)


plt.show()


# As you can see there is a decrease in deaths from year 1998 to 2016

# ## Q1 Question 4 Are there year-by-year changes in the four leading causes of death nationwide

# In[270]:


df1.head()
df1_yearly_leading_causes=df1.loc[:,['Year','Cause Name','Deaths']]
df1_yearly_leading_causes=df1.groupby(['Cause Name','Year'],as_index=False)['Deaths'].agg(sum)
df1_yearly_leading_causes=pd.DataFrame(df1_yearly_leading_causes)

df1_yearly_leading_causes=df1_yearly_leading_causes[df1_yearly_leading_causes['Cause Name'].isin(top_4_deaths.index)]
df1_yearly_leading_causes


# In[322]:


plt.figure()
plt.ylabel("Year")
plt.xlim(1998,2016)
plt.ylim(50000,100000)
plt.xlabel("Deaths")
plt.title("Year wise trend of leading four causes of death")
#for_plot_purposes=df1_yearly_leading_causes.groupby(['Cause Name','Year'])['Deaths'].agg(sum)
#for_plot_purposes
plt.plot(y=df1_yearly_leading_causes.iloc[3],data=df1_yearly_leading_causes)
plt.show()

