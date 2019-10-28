#!/usr/bin/env python
# coding: utf-8

# # Visualizing Data - Scatter Plot
# ___
# Graph a Dataset: Create a scatterplot of the hours and grade data in gradedata.csv. Do you see a pattern in the data?

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
#Load data
Location = "Datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[3]:


# Assign x="hours" and y="grade" 
plt.scatter(df["hours"], df["grade"], color="skyblue")


# In the above visualization, there are notable patterns in the scatter plot from the grade dataset. For instance, we can see that as a student spends more time studyng their grades goes up, with the exception of a few outlier points. 
