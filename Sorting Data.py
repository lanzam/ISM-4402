#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
Location = "Datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[6]:


df = df.sort_values(by=['lname','age','grade'], ascending=[True,True,False])
df.head()


# In[ ]:




