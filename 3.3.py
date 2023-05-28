#!/usr/bin/env python
# coding: utf-8

# In[95]:


def find(graph,a):
    if graph[a]<0:
        return a
    else:
        return find(graph,graph[a])


# In[96]:


def union(graph,a,b,answer):
    ta=a
    tb=b
    a=find(graph,a)
    b=find(graph,b)
    
    if a == b:
        pass
    else:
        answer.append([ta,tb])
        if(graph[a]<graph[b]):
            graph[a]=graph[a]+graph[b]
            graph[b]=a
            
        else:
            graph[b]=graph[a]+graph[b]
            graph[a]=b
            


# In[99]:


ipt=[[1,2,1], [1, 3, 3], [2, 6, 4], [3, 6, 2], [3, 4, 1], [4, 5, 5],
          [6, 7, 2], [6, 5, 6], [7, 5, 7]]


ipt=sorted(ipt,key=lambda ipt : ipt[2])
print(ipt)
graph={}
for i in range(8):
    graph[i]=-1
answer=[]    
for u,v,d in ipt:
    union(graph,u,v,answer)
print(answer)


# In[ ]:




