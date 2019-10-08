#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
# Starting Dataset
names = ['Bob','Jessica','Mary','John',"Mel"]
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]


# In[5]:


GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data = GradeList, columns=['Names', 'Grades','BS','MS','PhD'])
df


# In[6]:


df.mean()


# In[8]:


df.count()


# In[9]:


df.std()


# In[10]:


df.min()


# In[11]:


df.max()


# In[12]:


df.quantile(.75)


# In[13]:


df.quantile(.25)


# In[14]:


df.quantile(.5)

