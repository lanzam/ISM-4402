#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 

names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,-2,77,78,101]

GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
                 columns=['Names','Grades'])
df


# In[3]:


#Replace subzero grades with a grade of zero
df.loc[(df['Grades'] <=0, 'Grades')] = 0
df

