#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd


# In[202]:


df=pd.read_csv("Salaries.csv")


# In[203]:


df


# In[8]:


# Display Top 10 rows of the dataset:
df.head(10)


# In[10]:


# Display bottom 10 rows of the dataset:
df.tail(10)


# In[12]:


# Find the shape of our dataset:
df.shape


# In[14]:


# Display the no.of.rows & no.of.columns in our dataset:
print("No_of_rows:",df.shape[0])
print("No_of_columns:",df.shape[1])


# In[16]:


# Getting information about our dataset:
df.info()


# In[19]:


# check null values in the dataset:
df.isnull().sum()


# In[40]:


# Drop ID ,Notes,Agency, and status columns:
df


# In[24]:


df.columns


# In[128]:


df=df.drop(['Id','Notes','Agency','Status'],axis=1)
df


# In[129]:


# Get overall statistics of all dataframe:
df.describe(include='all')


# In[47]:


df.describe()


# In[49]:


# Find the occurances of the Employee Name dataset: Top 5 
df.columns


# In[130]:


df["EmployeeName"].value_counts().head(5)


# In[131]:


# Find the number of unique job_titles:
df["JobTitle"].nunique()


# In[132]:


# Total no of job title contains captain:
df["JobTitle"]=="captain"


# In[133]:


df[df["JobTitle"].str.contains("CAPTAIN")]


# In[71]:


len(df[df["JobTitle"].str.contains("CAPTAIN",case=False)])


# In[73]:


df[df["JobTitle"].str.contains("CAPTAIN",case=False)].count()


# In[78]:


# Display all the employee names from Fire Department:
df.columns


# df["JobTitle"].str.contains("fire Department",case=False)

# In[82]:


df[df["JobTitle"].str.contains("Fire Department",case=False)]["EmployeeName"]


# In[86]:


# Find the maximum,minmum and average basepay:
df["BasePay"].describe()


# In[88]:


# replace "Not provided" EmployeeName column to NaN
df.columns


# In[144]:


import numpy as np
df["EmployeeName"].replace("Not provided",np.nan)


# In[164]:


# Drop the rows having 5 missing values:
df=df.drop(df[df.isnull().sum(axis=1)==5].index,axis=0)
df


# In[139]:


# Find the job title of ALBERT PARDINI:
df[df["EmployeeName"]=="ALBERT PARDINI"]["JobTitle"]


# In[165]:


# How much ALBERT PARDINI make (include Benefits):
df[df["EmployeeName"]=="ALBERT PARDINI"]


# In[175]:


# Display name of the person who has highest basepay???
import numpy as np
df["BasePay"].replace("Not Provided",np.NaN)
df


# In[204]:


import numpy as np
df["BasePay"].replace("Not Provided",np.NaN)


# In[213]:


df.drop(df[df["BasePay"]=="Not Provided"].index,inplace=True)


# In[214]:


df


# In[ ]:





# In[ ]:





# In[ ]:




