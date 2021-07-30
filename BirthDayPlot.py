#!/usr/bin/env python
# coding: utf-8

# In[63]:


import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import random


# In[19]:


data = csv.reader(open('data/seoul.csv', 'rt', encoding='UTF-8'))


# In[24]:


next(data)


# In[25]:


ls = list(data)


# In[49]:


#print([i for i in ls])


# In[ ]:


"""
next() 는 두가지 포맷으로 사용된다
function 구조로 사용되면 header 만 리턴한다
consumer 구조로 사용 되면 data 에서 header를 제거한다

data : [] = list() 는 list 타입의 data 를 list()로 초기화 시키는 것이다.
단, 한 메소드 내에서만 사용하면 로컬에서 초기화 한다. 예제는 다음과 같아.
data :[] = None
def save_highest_temperatures(self):
    data = list()
그러나, 여러 메소드에서 사용하면 필드에서 초기화 한다.


"""


# In[51]:


#print([i[-1] for i in ls])


# In[50]:


highest_temperatures = []
[highest_temperatures.append(float(row[-1])) for row in ls if row[-1] !='']
print(f'총{len(highest_temperatures)}개')


# In[38]:


plt.figure(figsize=(10,2))
plt.plot(highest_temperatures, 'r')


# In[40]:


high = [] #최고기온
low = [] #최저기온


# In[41]:


for i in ls:
    if i[-1] !='' and i[-2] !='':
        if 1983 <= int(i[0].split('-')[0]):
            if i[0].split('-')[1]=='02' and i[0].split('-')[2]== '14':
                high.append(float(i[-1]))
                low.append(float(i[-2]))


# In[48]:


plt.rc('font', family='malgun Gothic')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False
plt.title('mybrithdayhighest_temperatures')
plt.plot(high,'hotpink', label='high')
plt.plot(low, 'skyblue',label='low')


# In[64]:


arr = []
[arr.append(random.randint(1, 1000))for i in range(13)]
plt.boxplot(arr)
plt.show()


# In[66]:


month = [[], [], [], [], [], [], [], [], [], [], [], []]
# for i in arr:
#     if i[-1] != '':
#         month[int(i[0].split('-')[1])-1].append(float(i[-1]))
[month[int(i[0].split('-')[1]) - 1].append(float(i[-1])) for i in ls if i[-1] != '']
plt.boxplot(month)
plt.show()


# In[68]:


day = []
[day.append([]) for i in range(31)]
[day[int(i[0].split('-')[2]) -1].append(float(i[-1]))
     for i in ls
        if i[-1] != ''
            if i[0].split('-')[1] == '08']
plt.style.use('ggplot') # Graph Style
plt.figure(figsize=(10, 5), dpi=300) # Graph Size
plt.boxplot(day, showfliers=False) # Omit Outlier
plt.show()

