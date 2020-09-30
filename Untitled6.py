#!/usr/bin/env python
# coding: utf-8

# In[75]:


def my_reduce(a1,a2):
    return (a1,a2)


# In[76]:


def add(a,b):
    c=a+b
    return c


# In[77]:


list1 = ['jinal','jain']


# In[78]:


my_reduce (lambda a,b: add,list1)


# In[ ]:




