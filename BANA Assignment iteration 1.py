#!/usr/bin/env python
# coding: utf-8

# ### Import important packages like pandas and numpy

# In[1]:


import pandas as pd
import numpy as np


# ### store your directory and file names in a variable for code reusability

# In[37]:


location='C://Backup//DataPartition//RIT Course Work//BANA//Assignment 1//'
file1='NCHS_-_Leading_Causes_of_Death__United_States.csv'
file2='nst-est2018-01.xlsx'


# ### reading the file into data frames

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


# ### Drop first two cells for data cleaning purposes

# In[52]:


new_df2=df2.copy()
new_df2=new_df2.drop(new_df2.loc[0:2])
new_df2

