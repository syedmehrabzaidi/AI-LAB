'''
Created on Apr 3, 2019

@author: dr.aarij
'''


import game
import adversarialNode
import sys
import simpleMinimax


class MinimaxTreeGame(game.Game):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        
                                    A
                    B                C            D
                E    F    G    H    I    J    K    L    M
                3    12   8    2    4    6    14    5    2
        '''
        
        bottom1 = [adversarialNode.AdversarialNode(3,"E",True,[]),
                   adversarialNode.AdversarialNode(12,"F",True,[]),
                   adversarialNode.AdversarialNode(8,"G",True,[])]
        
        bottom2 = [adversarialNode.AdversarialNode(2,"H",True,[]),
                   adversarialNode.AdversarialNode(4,"I",True,[]),
                   adversarialNode.AdversarialNode(6,"J",True,[])]

        bottom3 = [adversarialNode.AdversarialNode(14,"K",True,[]),
                   adversarialNode.AdversarialNode(5,"L",True,[]),
                   adversarialNode.AdversarialNode(2,"M",True,[])]
        
        b = adversarialNode.AdversarialNode(-sys.maxsize - 1,"B",False,bottom1)
        c = adversarialNode.AdversarialNode(-sys.maxsize - 1,"C",False,bottom2)
        d = adversarialNode.AdversarialNode(-sys.maxsize - 1,"D",False,bottom3)
        
        a = adversarialNode.AdversarialNode(-sys.maxsize - 1,"A",True,[b,c,d])
        
        self._root = a
        
    def getInitialState(self):
        return self._root
    
    def getPlayer(self,state):
        return state.isMax()
    
    def getActions(self,state):
        return [x for x  in range(len(state._children))]
         
    def getResult(self, state, action):
        return state._children[action]
     
    def terminalTest(self,state):
        return state.isLeaf()
     
    def utility(self,state,player):
        return state._value
            
    def getAgentCount(self): 
        return 2
    
    def printState(self,state):
        toPrintNodes = []
        toPrintNodes.append(state)
        while len(toPrintNodes) > 0:
            node = toPrintNodes[0]
            del toPrintNodes[0]
            print("Name = %s, value = %d"%(node._name,node._utility))
            toPrintNodes += node._children
        
    
    
if __name__ == "__main__":
    game = MinimaxTreeGame()    
    minimax = simpleMinimax.SimpleMinimax(game)
    initialState = game.getInitialState()
    minimax.minimax_decision(initialState) 
    game.printState(initialState)
    