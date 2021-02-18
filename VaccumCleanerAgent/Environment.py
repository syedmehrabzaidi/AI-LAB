#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
Created on Feb 11, 2019

@author: dr.aarij
'''
from abc import abstractmethod

class Environment(object):
    '''
    classdocs
    '''
    
    @abstractmethod
    def __init__(self, n):
        self.n = n
    
    def executeStep(self,n=1):
        raise NotImplementedError('action must be defined!')
    
    def executeAll(self):
        raise NotImplementedError('action must be defined!')
    
    def delay(self, n=100):
        self.delay = n
        


# In[ ]:




