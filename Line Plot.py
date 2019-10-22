#!/usr/bin/env python
# coding: utf-8

# # Line Plot
# Dataset used in an example from the book. Then, we'll add an annotation to Bob's 76 that will says "Wow!".

# In[1]:


import pandas as pd

names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,83,77,78,95]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns=['Names', 'Grades'])

get_ipython().run_line_magic('matplotlib', 'inline')
df.plot()


# In[6]:


# Graph "y" location to be 76 that Bob got on the previous dataset. Then, move text 'Wow!!!' up and center.
import matplotlib.pyplot as plt

df.plot()
displayText = "Wow!!!"
xloc = 0
yloc = 76
xtext = 180
ytext = 100
plt.annotate(displayText, 
            xy=(xloc, yloc), 
            xytext=(xtext,ytext),
            xycoords=('axes fraction', 'data'),
            textcoords='offset points')


# In[8]:


# Add an arrow to the graph to point "Wow!!!" 
df.plot()
displayText = "Wow!!!"
xloc = 0
yloc = 76
xtext = 180
ytext = 100    
plt.annotate(displayText, 
            xy=(xloc, yloc), 
            arrowprops=dict(facecolor='black', shrink=0.05),   
            xytext=(xtext,ytext),
            xycoords=('axes fraction', 'data'),
            textcoords='offset points')

