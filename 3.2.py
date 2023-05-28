#!/usr/bin/env python
# coding: utf-8

# In[26]:


jobs=[['Job1',2,15],['Job2',3,27],['Job3',3,10],['Job4',3,100],['Job5',4,150]]


# In[27]:


jobs=sorted(jobs,key=lambda jobs : jobs[2],reverse=True)## The tasks get arranged in descending order according to profit


# In[28]:


jobs


# In[29]:


scheduled=[]
total_profit=0
time=0
for i in jobs:
    job_id=i[0]
    job_profit=i[2]
    job_deadline=i[1]
    
    if time<job_deadline:
        scheduled.append(job_id)
        total_profit+=job_profit
        time+=1
        
print(scheduled)
print(total_profit)


# In[ ]:




