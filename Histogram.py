#!/usr/bin/env python
# coding: utf-8

# # Visualizing Data - Histogram
# ___
# Graph a Dataset: Create an age histogram categoized by gender

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
#Load data
Location = "Datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


df.hist()


# In[6]:


df.hist(column="age", color="skyblue")


# In[5]:


#Categorize "age" by "gender"
df.hist(column="age", by="gender")

