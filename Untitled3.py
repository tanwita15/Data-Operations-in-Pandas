#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd;
import numpy as np;


# In[3]:


dataFrame = pf.read_csv("C:\Users\User\Downloads\Notebooks\Lesson_10_Practices\Create Pandas Dataframe\Pandas-SalaryGender.csv");


# In[4]:


import os;


# In[5]:


os.getcwd();


# In[6]:


os.chdir("C:\Users\User\Downloads\Notebooks\Lesson_10_Practices\Create Pandas Dataframe\Pandas-SalaryGender.csv");


# In[8]:


data=pd.read_csv(r"C:\Users\User\Downloads\Notebooks\Lesson_10_Practices\Create Pandas Dataframe\Pandas-SalaryGender.csv");


# In[9]:


data.info();


# In[10]:


data.describe();


# In[11]:


data


# In[12]:


data['Gender']=data['Gender'].replace(['1'],'Male')
data['Gender']=data['Gender'].replace(['0'],'Female')


# In[13]:


data


# In[15]:


data.replace(to_replace=0, value='Female')
data.replace(to_replace=1, value='Male')


# In[16]:


#to find the max and min salary 
max=data['Salary'].loc[data['Salary'].idxmax()]
print(max)


# In[17]:


min=data['Salary'].loc[data['Salary'].idxmin()]
print(min)


# In[18]:


#to find the number of men with 'phD'
data['PhD'].value_counts()


# In[22]:


#to create dataframe with gender and phd
data[['Age','PhD']]


# In[ ]:





# In[32]:


#to remove the people without phd
indexData= data[(data['PhD']==0)].index


# In[30]:


data.drop(indexData, inplace=True)


# In[31]:


data.head(15)


# In[33]:


#to find the number of people holding phd
data['PhD'].value_counts()


# In[34]:


data


# In[35]:


#sort the dataframe on the basis of salary
data.sort_values(by=['Salary'])


# In[ ]:




