#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


df=pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
print('Shape:',df.shape)
print('Data:',df.head())
print('Missing Values')
print(df.isnull().sum())


# In[3]:


#Countplot for Attrition
sns.countplot(x='Attrition',data=df)
plt.show()


# In[13]:


#Countplot for Attrition
sns.countplot(x='OverTime',hue='Attrition',data=df)
plt.show()


# In[8]:


#Countplt for Attrition by Dept
sns.countplot(data=df,x='Department',hue='Attrition')
plt.xticks(rotation=45)
plt.show()


# In[10]:


#Monthly Income Vs Attriction
sns.boxplot(data=df,x='Attrition',y='MonthlyIncome')
plt.show()


# In[14]:


#Age Distribution
sns.histplot(data=df,x='Age',hue='Attrition',kde=True,bins=20)
plt.show()


# In[16]:


df.to_csv('HR Attrition_clean.csv',index=False)
print('csv cleaned sucessfully.')


# In[ ]:




