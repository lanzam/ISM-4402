#!/usr/bin/env python
# coding: utf-8

# # Axis Auto Sales
# ---
# ### Analysis Exercise 2

# In[27]:


import pandas as pd 
import seaborn as sns
Location = 'Datasets/axisdata.csv'
df= pd.read_csv(Location)
df.head()


# In[2]:


# Average cars sold per month 
df['Cars Sold'].mean()


# In[3]:


# Max cars sold per month 
df['Cars Sold'].max()


# In[4]:


# Min cars sold per month 
df['Cars Sold'].min()


# In[5]:


# Average cars sold per month by gender
pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[6]:


# Average hours worked by people selling > 3 cars per month
df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[7]:


# Average years of experience
df['Years Experience'].mean()


# In[8]:


# Average years of experience for people selling > 3 cars per month
df[df['Cars Sold']>3]['Years Experience'].mean()


# In[9]:


# average cars sold per month by whether or not they have had sales training
pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[10]:


df['Fullname']= df['Lname'] + ', ' + df['Fname']
df.head()


# In[11]:


df = df.sort_values(by='Fullname', ascending=True)
df


# ## Visualization 1

# In[12]:


g=sns.catplot(x="Cars Sold", y="Hours Worked", hue="SalesTraining", aspect=1.5, kind="swarm", data=df)
g.savefig("Viz1.png") # Save graph 


# In[23]:


g=sns.catplot("Cars Sold", data=df, aspect=4.0, kind='count',
                       hue='SalesTraining')
g.set_ylabels('Total Cars Sold')


# ## Visualization 2

# In[39]:


g = sns.lineplot(x="Cars Sold",y="Hours Worked",
                         hue='SalesTraining',
                         data=df
                         ).set_title('Sales Performance by Hours Worked and Sold Cars')
plt.show()


# In[ ]:




