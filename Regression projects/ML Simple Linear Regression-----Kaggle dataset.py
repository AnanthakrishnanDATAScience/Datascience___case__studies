#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Simple Linear regression
# Project-----01
# Salary prediction....


# In[20]:


#Importing the required Libaries:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[21]:


df=pd.read_csv("Salary_Data.csv")
df


# In[22]:


df.info()


# In[23]:


df.describe()


# In[25]:


x=df.values[:,:-1]
x


# In[28]:


y=df.values[:,-1]
y


# In[29]:


#Plotting the points in Graph with scatter plot:
df.plot(kind="scatter",x="YearsExperience",y="Salary",title="Salaryprediction")
plt.show()


# In[31]:


# Importing train_test_split:
from sklearn.model_selection import train_test_split


# In[32]:


x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.7,random_state=42)


# In[62]:


#Importing Linear Regression:
from sklearn.linear_model import Ridge,LinearRegression


# In[34]:


model=LinearRegression()
model.fit(x_train,y_train)
result=model.score(x_train,y_train)
print("Accuary mean:","%3f"%result)


# In[35]:


result=model.score(x_test,y_test)
print("Accuary mean:","%3f"%result)


# In[36]:


# Predicting the salary for test values:
y_pred=model.predict(x_test)


# In[72]:


# Importing r2_score libaries:
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error


# In[73]:


#Using built_In functions:
print("R Squared using built-In function:",r2_score(y_test,y_pred))


# In[74]:


print("Mean_Absolute_error:",mean_absolute_error(y_test,y_pred))
print("Mean_squared_error:",mean_squared_error(y_test,y_pred))
print("Root_mean_squared_error:",np.sqrt(mean_squared_error(y_test,y_pred)))


# In[75]:


# Finding the fitting line:
model.fit(x,y)
print("Intercept:",model.intercept_)
print("Coefficient:",model.coef_)


# In[76]:


# plotting the fiitest line:
plt.figure(figsize=(12,6))
plt.scatter(x,y,color="black")
plt.plot(x,model.predict(x),color="blue",linewidth=3)
plt.xlabel("YearExperience")
plt.ylabel("Salary")
plt.title("SalaryPrediction")
plt.show()


# In[ ]:





# In[ ]:




