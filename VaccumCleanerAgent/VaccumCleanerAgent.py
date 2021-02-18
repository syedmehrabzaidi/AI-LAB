#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
Created on Feb 11, 2019

@author: dr.aarij
'''

#import os
#os.chdir('/Desktop/Lab3')

import Environment 
import Room
import VaccumAgent

class TwoRoomVaccumCleanerEnvironment(Environment.Environment):
    '''
    classdocs
    '''
    def __init__(self, agent):
        '''
        Constructor
        '''
        self.r1 = Room.Room('A','dirty')
        self.r2 = Room.Room('B','dirty')
        self.agent = agent
        self.currentRoom = self.r1
        self.delay = 1000
        self.step = 1
        self.action = ""
    
    def executeStep(self,n=1):
        for _ in range(0,n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res
            if res == 'clean':
                self.currentRoom.status = 'clean'
            elif res == 'right':
                self.currentRoom = self.r2
            else:
                self.currentRoom = self.r1
            self.displayAction()
            self.step += 1
        
    
    def executeAll(self):
        raise NotImplementedError('action must be defined!')
    
    def displayPerception(self):
        print("Perception at step %d is [%s,%s]" %(self.step,self.currentRoom.status,self.currentRoom.location))
        
    def displayAction(self):
        print("------- Action taken  at step %d is [%s]" %(self.step,self.action))
    
    def delay(self, n=100):
        self.delay = n
        
if __name__ == '__main__':
    vcagent = VaccumAgent.VaccumAgent() 
    env = TwoRoomVaccumCleanerEnvironment(vcagent)
    env.executeStep(50) 
    
    
    
    
    
    


# In[ ]:




