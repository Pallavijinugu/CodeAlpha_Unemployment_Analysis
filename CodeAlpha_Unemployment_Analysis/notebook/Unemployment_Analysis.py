#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')


# In[4]:


df = pd.read_csv(r"C:\Users\Jinugu Pallavi\OneDrive\Desktop\CodeAlpha_Unemployment_Analysis\data\Unemployment in India.csv")


# In[5]:


df.head()


# In[6]:


df.shape


# In[7]:


df.info()


# In[8]:


df.columns


# In[9]:


df.columns = [
    'States',
    'Date',
    'Frequency',
    'Estimated_Employed',
    'Estimated_Labour_Participation_Rate',
    'Estimated_Unemployment_Rate',
    'Region'
]


# In[10]:


df.isnull().sum()


# In[11]:


df = df.dropna()


# In[12]:


df.isnull().sum()


# In[13]:


df['Date'] = pd.to_datetime(df['Date'])


# In[14]:


df['Month'] = df['Date'].dt.month


# In[15]:


df['Year'] = df['Date'].dt.year


# In[16]:


df.describe()


# In[17]:


df['Estimated_Unemployment_Rate'].mean()


# In[18]:


df['Estimated_Unemployment_Rate'].max()


# In[19]:


plt.figure(figsize=(12,6))
sns.lineplot(x='Date', y='Estimated_Unemployment_Rate', data=df)

plt.title('Unemployment Rate Over Time')
plt.xticks(rotation=45)
plt.show()


# In[20]:


plt.figure(figsize=(14,8))

sns.barplot(
    x='Estimated_Unemployment_Rate',
    y='States',
    data=df
)

plt.title('State-wise Unemployment Rate')
plt.show()


# In[21]:


covid_df = df[df['Date'] >= '2020-03-01']


# In[22]:


plt.figure(figsize=(12,6))

sns.lineplot(
    x='Date',
    y='Estimated_Unemployment_Rate',
    data=covid_df
)

plt.title('Covid-19 Impact on Unemployment')
plt.xticks(rotation=45)

plt.show()


# In[23]:


monthly = df.groupby('Month')['Estimated_Unemployment_Rate'].mean()

monthly.plot(kind='bar', figsize=(10,5))

plt.title('Monthly Average Unemployment')
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')

plt.show()


# In[24]:


plt.figure(figsize=(10,6))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap='coolwarm'
)

plt.title('Correlation Heatmap')

plt.show()


# In[25]:





# In[ ]:




