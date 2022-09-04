#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
my_array = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
the_diagonal = np.trace(my_array)
print(the_diagonal)


