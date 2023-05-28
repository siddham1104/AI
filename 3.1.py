#!/usr/bin/env python
# coding: utf-8

# In[3]:


from heapq import *
def dijkstra(graph,start,visited,distance,parent):
    bag=[]
    distance[start]=0
    parent[start]=-1
    heappush(bag,[0,start])
    
    while bag:
        d,n=heappop(bag)
        if not visited[n]:
            visited[n]=1
            for cd,cn in graph[n]:
                if (d+cd)<distance[cn] and not visited[cn]:
                    distance[cn]=d+cd
                    parent[cn]=n
                    heappush(bag,[(d+cd),cn])
    print(distance)
    print(parent)


# In[4]:


ipt =[[1,3,2],[1,2,1],[2,3,1],[2,5,1],[3,4,2],[5,4,3]]

n=5
graph ={}
distance={}
visited={}
parent={}

for i in range (1,n+1):
    graph[i]=[]
    distance[i]=10**8+1
    visited[i]=0
    parent[i]=None
    
for u,v,d in ipt:
    graph[u].append([d,v])
    #graph[v].append([d,u])

start=1 # this is source
print(graph)
dijkstra(graph,start,visited,distance,parent)


# In[ ]:




