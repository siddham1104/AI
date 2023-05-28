#!/usr/bin/env python
# coding: utf-8

# In[1]:


from heapq import *


# In[2]:


def prims(graph,start,visited,distance,parent):
    bag=[]
    heappush(bag,[0,start])
    parent[start]=-1
    distance[start]=0
    
    while bag:
        d,n = heappop(bag)
        if not visited[n]:
            visited[n]=1

            for cd,cn in graph[n]:
                if distance[cn]>cd and  not  visited[cn]:
                    distance[cn]=cd
                    parent[cn]=n
                    heappush(bag,[cd,cn])
    
    print("Distance",distance)
    print("parent",parent)


# In[3]:


ipt = [[1,2,1],[2,3,4],[3,4,1],[4,5,2],[1,5,3],[2,5,2],[2,4,1]]
graph={}
visited={}
distance={}
parent={}
n=5


# In[4]:


for i in range(1,n+1):
    graph[i]=[]
    visited[i]=0
    distance[i]=8**10
    parent[i]=None


# In[5]:


for u,v,d in ipt:
    graph[u].append((d,v))
    graph[v].append((d,u))


# In[6]:


start=1
print(graph)
prims(graph,start,visited,distance,parent)


# In[ ]:





# In[ ]:




