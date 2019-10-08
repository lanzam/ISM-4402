#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

Location = "Datasets/gradedata.csv"
df=pd.read_csv(Location)
df.tail()


# In[2]:


# Random sample of 500 rows
df.take(np.random.permutation(len(df))[:500])

