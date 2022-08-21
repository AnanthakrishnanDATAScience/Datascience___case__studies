#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Importing the Libaries:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[163]:


# Loading the datasets:
df=pd.read_csv("adult.csv")
df


# In[6]:


# Display Top 10 rows of the dataset:
df.head(10)


# In[8]:


# Display bottom 10 rows of the dataset:
df.tail(10)


# In[10]:


# Find the shape of our dataset:
df.shape


# In[12]:


print("No_of_rows:",df.shape[0])


# In[15]:


print("No_of_columns:",df.shape[1])


# In[17]:


# Getting information of the dataset:
df.info()


# In[25]:


# Fetch random samples from the dataset (50%):
df.sample(frac=0.50,random_state=100)


# In[27]:


# Check null values in the dataset:
df.isnull().sum()


# In[29]:


# check null values using heat maps :
sns.heatmap(df.isnull())


# In[31]:


# replace ? to nan values:
df.tail(20)


# In[94]:


df.isin(['?'])


# In[95]:


df.isin(["?"]).sum()


# In[96]:


df["workclass"]=df["workclass"].replace("?",np.NaN)
df["workclass"]


# In[98]:


df["occupation"]=df["occupation"].replace("?",np.NaN)
df["occupation"]


# In[99]:


df["native-country"]=df["native-country"].replace("?",np.NaN)
df["native-country"]


# In[100]:


df.isin(["?"]).sum()


# In[101]:


df.isnull().sum()


# In[102]:


sns.heatmap(df.isnull())


# In[103]:


df.dropna(how='any',inplace=True)


# In[104]:


df["workclass"].tail(20)


# In[105]:


df.shape


# In[106]:


# check and drop the duplicate values:
df.duplicated().any()


# In[107]:


df.drop_duplicates(inplace=True)


# In[108]:


df.shape


# In[109]:


# Get overall stats of the dataset:
df.describe()


# In[110]:


df.columns


# In[111]:


df.drop(["educational-num","capital-gain","capital-loss"],axis=1)


# In[113]:


df.columns


# In[118]:


# univariant Analysics:
# Distrubution for Age columns:
df["age"].describe()


# In[121]:


df["age"].hist()


# In[124]:


# Find the total no.of persons of Age having 17 and 48 using between method:
df["age"].between(17,48)


# In[127]:


sum(df["age"].between(17,48))


# In[129]:


# Distrubution of workclass columns...
df["workclass"].hist()


# In[131]:


df.columns


# In[133]:


df["education"]


# In[147]:


# How many persons having bachelor and Master degree....
df1=df[df["education"]=="Bachelor"]
df1


# In[159]:


df2=df[df["education"]=="Masters"]
df2


# In[165]:


len(df1)


# In[167]:


len(df2)


# In[ ]:





# In[ ]:




