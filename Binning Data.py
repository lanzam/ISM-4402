#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Location = "Datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[5]:


## Bin dividers for master's program that requires a grade
#  of 80 or above
bins=[0,80,100]
# Create Two name groups for passing and failing
status_names=['Pass', 'Fail']

df['status'] = pd.cut(df['grade'], bins, labels=status_names)

# View Fail and Pass counts by bin
pd.value_counts(df['status'])

