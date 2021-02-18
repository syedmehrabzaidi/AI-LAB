'''
Created on Feb 18, 2019

@author: dr.aarij
'''
import searchStrategy
from queue import Queue

class BreadthFirstSearchStrategy(searchStrategy.SearchStrategy):
    '''
    classdocs
    '''
    

    def __init__(self):
        self.queue = Queue()
        
    def isEmpty(self):
        return self.queue.empty()

    def addNode(self,node):
        return self.queue.put(node)

    def removeNode(self):
        return self.queue.get() 