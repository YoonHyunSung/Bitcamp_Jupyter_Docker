#!/usr/bin/env python
# coding: utf-8

# In[14]:


import matplotlib.pyplot as plt


# In[15]:


import random


# In[ ]:


from modu.template import ChangedTemperaturesOnMyBirthday
from modu.template.basic_hist import highest_temperature


# In[2]:


def plot_show():
    plt.title("plotting")
    plt.plot([10,20,30,40])
    plt.show()


# In[3]:


plot_show()


# In[4]:


def plot_two_list_show():
    plt.plot([10, 20, 30, 40],[1000, 3 ,355, 3])
    plt.show()


# In[7]:


plot_two_list_show()


# In[ ]:


def plot_label():
    plt.title("plotting")
    plt.plot([10, 20, 30, 40], label='asc')
    plt.plot([40, 30, 10, 10], label='desc')
    plt.legend()
    plt.show()


# In[11]:


plot_label()


# In[ ]:


def plot_marker():
    plt.title("plotting")
    plt.plot([10, 20, 30, 40],'r.--', label='circle')
    plt.plot([40, 30, 10, 10],'g^' ,label='triangle up')
    plt.legend()
    plt.show()


# In[12]:


plot_marker()


# In[ ]:


def scatter():
    plt.title("plotting")
    plt.plot([10, 20, 30, 40], 'r.', label='circle')
    plt.plot([40, 30, 10, 10], 'g^', label='triangle up')
    plt.legend()
    plt.show()


# In[13]:


scatter()


# In[ ]:


def sorted_random_arr()-> []:
    arr = []
    [arr.append(random.randint(1, 1000)) for i in range(13)]
    return arr

def show_boxplot(arr:[]):
    plt.boxplot(arr)
    plt.show()

def show_boxplot_month(month:str):
    plt.boxplot(highest_temperature(month))
    plt.show()
def show_boxplot_all_month():
    birth = ChangedTemperaturesOnMyBirthday()
    birth.read_data()
    data = birth.data

    #monthls =[]
    #month1 = []
    month = [[],[],[],[],[],[],[],[],[],[],[],[]]
    #for row in data:
      #  if row[-1] !='':
     #       month[int(row[0].split('-')[1])-1].append(float(row[-1]))
    #print(len(month))
    #print(month)
    #[[month1[int(row[0].split('-')[1]) - 1].append(float(row[-1])) for row in data if row[-1] != ''] for i in range(12)]
    #month = []
    [[month[int(row[0].split('-')[1])-1].append(float(row[-1])) for row in data if row[-1] !=''] for i in range(12)]
    #print(month[4])
    #print(len(month))
    return month

def show_boxplot_per_date(month : str):
    birth = ChangedTemperaturesOnMyBirthday()
    birth.read_data()
    data = birth.data
    day =[]
    [day.append([]) for i in range(31)]
    [day[int(i[0].split('-')[2])-1].append(float(i[-1])) for i in data if i[-1] !='' if i[0].split('-')[1]==month]
    plt.style.use('ggplot')
    plt.figure(figsize=(10,5),dpi=300)
    plt.boxplot(day, showfliers=False)
    plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




