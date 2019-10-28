#!/usr/bin/env python
# coding: utf-8

# # Visualizing Data - Pie Chart
# ___
# Graph a Dataset: What if instead of highlighting the worst student we put a spotlight on the best one? 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

names = ['Bob','Jessica','Mary','John','Mel']
absences = [3,0,1,0,8]
detentions = [2,1,0,0,1]
warnings = [2,1,5,1,2]

GradeList = zip(names,absences,detentions,warnings)
columns=['Names', 'Absences', 'Detentions', 'Warnings']
df = pd.DataFrame(data = GradeList, columns=columns)

df


# In[2]:


df['TotalDemerits'] = df['Absences'] + df['Detentions'] + df['Warnings']
df


# In[3]:


# Plot TotalDemetrits dataframe
plt.pie(df['TotalDemerits'])


# In[20]:


plt.pie(df['TotalDemerits'],
       labels=df['Names'],
       explode=(0,0,0,0.30,0),#Pie slice to highlight John, exploted out to show best student
       startangle=150,#Rotate the chart to 150* degrees
       autopct='%1.1f%%')

plt.axis('equal')
plt.show()

