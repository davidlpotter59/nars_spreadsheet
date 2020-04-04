#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

tips_df = pd.read_csv('/home/davep/python/python_for_data_management/content-python-for-database-and-reporting/data/tips.csv', sep=',', header=0)


# In[3]:


tips_df


# In[4]:


percent_tip = pd.Series(tips_df['tip']/tips_df['meal_total'],name='tip_percent')
tips_df = pd.concat([tips_df, percent_tip], axis=1)
tips_df.head()


# In[5]:


tips_df.to_csv('tips_percent.csv', sep=',', header=True, index=False)


# In[6]:


tips_df_from_file = pd.read_csv('./tips_percent.csv', sep=',', header=0)
tips_df_from_file.head()


# In[ ]:




