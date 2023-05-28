#!/usr/bin/env python
# coding: utf-8

# In[18]:


def selection(nums):
    length=len(nums)
    for i in range(length-1):
        minpos=i
        for j in range(i+1,length):
            if(nums[j]<nums[minpos]):
                minpos=j

        temp=nums[minpos]
        nums[minpos]=nums[i]
        nums[i]=temp

        print(nums)
        
        
nums=[1,15,5,3,8,6,7,2]
selection(nums)


# In[ ]:





# In[ ]:




