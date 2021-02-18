#!/usr/bin/env python
# coding: utf-8

# In[1]:




'''
Created on Feb 11, 2019

@author: dr.aarij
'''

import Agent

class VaccumAgent(Agent.Agent):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass

    def sense(self,env):
        self.environment = env
    
    def act(self):
        if self.environment.currentRoom.status == 'dirty':
            return 'clean'
        if self.environment.currentRoom.location == 'A':
            return 'right'        
        return 'left'
            
            



# In[ ]:





# In[ ]:





# In[ ]:




