#!/usr/bin/env python
# coding: utf-8

# In[14]:


def dfs(graph,start,visited=None):
    if visited is None:
        visited=set()
        
    visited.add(start)
    print(start)
    
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)




from queue import Queue
def bfs(graph,start):
    visited=set()
    queue=Queue()
    queue.put(start)
    visited.add(start)
    
    while not queue.empty():
        vertex=queue.get()
        print(vertex)
        #visited.add(vertex)
        
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.put(neighbour)
                visited.add(neighbour)
                

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}



print("DFS is :")
dfs(graph,'A')


print("BFS is : ")
bfs(graph,'A')


# In[ ]:





# In[ ]:




