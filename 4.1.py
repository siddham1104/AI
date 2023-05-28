#!/usr/bin/env python
# coding: utf-8

# In[3]:


def nqueen(n):
    col=set()       #To check whether that column has a queen or not 
    pdiag=set()     #To check the (r+c) values
    ndiag=set()     #To check the (r-c) values
    
    res=[]
    board=[["."]*n for i in range(n)]
    
    def backtrack(r):
        
        if(r==n):
            copy=["".join(row) for row in board]
            res.append(copy)
            return
        for c in range(n):
            if c in col or (r+c) in pdiag or (r-c) in ndiag:
                continue
            else:
                col.add(c)
                pdiag.add(r+c)
                ndiag.add(r-c)
                board[r][c]='Q'
                
                backtrack(r+1)
                
                col.remove(c)
                pdiag.remove(r+c)
                ndiag.remove(r-c)
                board[r][c]='.'
            
    backtrack(0)
    return res
            
solutions=nqueen(4)
count=0
for solution in solutions:
    for row in solution:
        print(" ".join(row))
    
    print("---------------")
    count+=1
print("Total Number of possible solution are ",count)      


# In[ ]:





# In[ ]:




