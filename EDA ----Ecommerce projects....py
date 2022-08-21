#!/usr/bin/env python
# coding: utf-8

# In[2]:


# importing Required Libaries...
import pandas as pd


# In[4]:


#Loading the dataset...
df=pd.read_csv("Ecommerce Purchases")
df


# In[6]:


# Display Top 10 rows of dataset:
df.head(10)


# In[8]:


# Display last 10 rows of Dataset:
df.tail(10)


# In[13]:


# check Datatype of each column:
df.info()


# In[16]:


# Check null values of the Dataset:
df.isnull().sum()


# In[19]:


# How many rows and columns in our dataset:
df.shape


# In[21]:


print("Number of rows:",df.shape[0])


# In[23]:


print("Number of columns:",df.shape[1])


# In[26]:


# Displaying the rows and columns:
df.columns


# In[28]:


len(df.columns)


# In[30]:


len(df)


# In[32]:


# Highest and lowest purchcase price:
df.head(5)


# In[35]:


df["Purchase Price"].max()


# In[37]:


df["Purchase Price"].min()


# In[39]:


# Average purchase price:
df["Purchase Price"].mean()


# In[41]:


# How many people have fr as langauge:
df["Language"]=="fr"


# In[46]:


df["Language"].value_counts()


# In[48]:


# Job contains Engineer:
df


# In[56]:


len(df[df["Job"].str.contains("engineer",case=False)])


# In[61]:


# Find the Email of the person who IP address having 132.207.160.22:
df[df["IP Address"]=="132.207.160.22"]["Email"]


# In[63]:


# How many people have mastercard as their  credit card provider and made a purchase above 50:
df.columns


# In[71]:


df[(df["CC Provider"]=="Mastercard")& (df["Purchase Price"]>50)]


# In[73]:


len(df[(df["CC Provider"]=="Mastercard")& (df["Purchase Price"]>50)])


# In[78]:


# Find the Email of the person with the following credit card number:4664825258997302
df[df["Credit Card"]==4664825258997302]["Email"]


# In[80]:


# How many people purchase during AM and how many people purchase during PM????
df


# In[86]:


df["AM or PM"].value_counts()


# In[88]:


# How many people have credit card have Expires in 2020:
df


# In[101]:


def fun():
    count=0
    for date in df["CC Exp Date"]:
        if date.split("/")[1]=="20":
            count+=1
    print(count)


# In[103]:


fun()


# In[106]:


# Top 5 most popular Email Id in the dataset (eg:.....@gmail.com,.......@yahoo.com)
list1=[]
for email in df["Email"]:
    list1.append(email.split("@")[1])


# In[108]:


df["temp"]=list1


# In[110]:


df["temp"]


# In[114]:


df["temp"].value_counts().head(5)

