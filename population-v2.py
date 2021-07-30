#!/usr/bin/env python
# coding: utf-8

# In[33]:


import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[34]:


data : [] = list()
home : [] = list()
away : object = None
result_name = ''


# In[35]:


#data1=pd.read_csv('./data/202106_202106_연령별인구현황_월간.csv', index_col=0, encoding='UTF-8', thousands=',')
#data1.to_csv('./data/202106_202106_연령별인구현황_월간_without_comma.csv', na_rep='NaN', sep=',')
data = csv.reader(open('./data/202106_202106_population.csv','rt',encoding='UTF-8'))
next(data)
data = list(data)


# In[38]:


#print(data)


# In[37]:


arr = []
[arr.append(int(j)) for i in data if '필동' in i[0] for j in i[3:]]
print([i for i in arr])


# In[30]:


plt.style.use('ggplot')
plt.plot(arr)


# In[31]:


[home.append(int(j)) for i in data if '필동' in i[0] for j in i[3:]]
print(home)


# In[32]:


plt.title('Pildong Population')
plt.plot(arr)


# In[ ]:


mn = 1
result = 0
home = []
result_name = ''
for i in data:
    if '필동' in i[0]:
        foo = np.array(i[3:], dtype=int)/int(i[2])

home = foo
away = None
for i in data:
    bar = np.array(i[3:], dtype=int) / int(i[2])
    s = np.sum((home - bar) ** 2)
    if s < mn and '필동' not in i[0]:
        mn = s
        result_name = i[0]
        result = bar
away = result

