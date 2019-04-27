#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import numpy as np
import pandas as pd


# In[3]:


#設定data_path
dir_data='./data/'


# In[4]:


f_app = os.path.join(dir_data, 'application_train.csv')
print('Path of read in data: %s' % (f_app))
app_train = pd.read_csv(f_app)
#Path of read in data: ./data/application_train.csv


# In[5]:


#for example 讀取資料
get_ipython().run_line_magic('pinfo', 'pd.read_csv')


# In[6]:


app_train.head()


# In[7]:


app_train.tail()


# In[12]:


app_train.info()


# In[13]:


s=app_train.dtypes
s


# In[14]:


i=app_train.ndim
i


# In[15]:


a=app_train.shape #row count colum count
a


# In[17]:


idx=app_train.columns
label=app_train.columns[0]
lst=app_train.columns.tolist()


# In[18]:


lst


# In[19]:


idx


# In[ ]:


# df.rename(columns={'old':'new'}, inplace=True)
# df = df.rename(columns={'a':1,'b':'x'}

