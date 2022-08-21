#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Simple Linear Regression
# Sales Prediction
# project-02


# In[2]:


# Importing required Libaries:
# supress warnings:
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df=pd.read_csv("advertising.csv")
df


# In[7]:


df.info()


# In[9]:


df.describe()


# In[12]:


# Data cleaning 
# Checking null values
df.isnull().sum()


# In[17]:


# Outlier Analysics:
fig,axs=plt.subplots(3,figsize=(5,5))
plt1=sns.boxplot(df["TV"],ax=axs[0])
plt2=sns.boxplot(df["Newspaper"],ax=axs[1])
plt3=sns.boxplot(df["Radio"],ax=axs[2])
plt.tight_layout()


# In[21]:


#EDA Exploratry Data Analysics:
# how salers are releated to other variables:
sns.pairplot(df,x_vars=["TV","Newspaper","Radio"],y_vars=["Sales"],height=4,aspect=1,kind="scatter")
plt.show()


# In[26]:


# Correlations between two variables:
import statsmodels.api as sm

corr=df.corr()
sm.graphics.plot_corr(corr,xnames=list(corr.columns))
plt.show()

print(corr)


# In[28]:


# Building Model:
x=df["TV"]
x


# In[30]:


y=df["Sales"]
y


# In[32]:


#Train_test_split:
from sklearn.model_selection import train_test_split


# In[34]:


x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.7,random_state=42,shuffle=True)


# In[36]:


x_train.head()


# In[38]:


y_train.head()


# In[42]:


#Building a model:
X_train=sm.add_constant(x_train)

# Fit the regression line with OLS
lr=sm.OLS(y_train,X_train).fit()


# In[44]:


lr.params # list the parameters for intercept and slope for the regression line


# In[46]:


print(lr.summary())


# In[48]:


plt.scatter(x_train,y_train)
plt.plot(x_train,7.2066+0.0548*x_train,color="red")
plt.show()


# In[51]:


#Model Evaluation
# Residual analysics..  Formulae for residuals=y-ypredict
y_train_predict=lr.predict(X_train)
res=(y_train-y_train_predict)


# In[63]:


# Error Distrubutions:
fig=plt.figure()
sns.distplot(res,bins=15)
fig.suptitle("Error_distrubutions",fontsize=20)
plt.xlabel("y_train-y_train_predict")
plt.show()


# In[66]:


#predict the test values:
x_test=sm.add_constant(x_test)
y_test_predict=lr.predict(x_test)


# In[75]:


# Find MAE,RMAE:
import sklearn.metrics as metrics
print("Train MAE:",metrics.mean_absolute_error(y_train,y_train_predict))
print("Train MSE:",np.sqrt(metrics.mean_squared_error(y_train,y_train_predict)))


# In[87]:


# r2_score:
y_predict=lr.predict(x_test)
print("R_square_value:",r2_score(y_test,y_predict))


# In[ ]:




