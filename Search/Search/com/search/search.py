'''
Created on Feb 18, 2019

@author: dr.aarij
'''
import os
#os.chdir('//fileserver/Elibrary/Lectures/Duaa Baig/AI/Python/code/Search/');
#print(os.getcwd())
import node
import eightPuzzleProblem
import breadthFirstSearchStrategy

class Search(object):
    '''
    classdocs
    '''


    def __init__(self, searchProblem, searchStrategy):
        '''
        Constructor
        '''
        self.searchProblem = searchProblem
        self.searchStrategy = searchStrategy
        
    def solveProblem(self):
        node1 = node.Node(self.searchProblem.initialState(), None, 0, 0, '')
        self.searchStrategy.addNode(node1)
        
        duplicateMap = {}
        duplicateMap[node1.state.stringRep()] = node1.state.stringRep()
        
        result = None
        
        while not  self.searchStrategy.isEmpty():
            currentNode = self.searchStrategy.removeNode()
            
            if self.searchProblem.isGoal(currentNode.state):
                result = currentNode
                break
            
            nextMoves = self.searchProblem.succesorFunction(currentNode.state)
            
            for nextState in nextMoves:
                if nextState.stringRep() not in duplicateMap:
                    newNode = node.Node(nextState, currentNode, currentNode.depth + 1, currentNode.cost + nextState.cost, nextState.action) 
                    self.searchStrategy.addNode(newNode)
                    duplicateMap[newNode.state.stringRep()] = newNode.state.stringRep()             
        return result
    
    def printResult(self,result):
        if result.parentNode is None:
            print("Game Starts")
            print("Initial State : %s" % result.state.getCurrentState())
            return
        self.printResult(result.parentNode)
        print("Perform the following action %s, \n    New State is  %s,  cost is %d"%(result.action,result.state.getCurrentState(),result.cost))

if __name__ == "__main__":
    searchProblem = eightPuzzleProblem.EightPuzzleProblem([[3,1,0],[6,7,2],[4,5,8]], [[1,2,3],[4,5,6],[7,8,0]])
    searchStrategy = breadthFirstSearchStrategy.BreadthFirstSearchStrategy()
    search = Search(searchProblem, searchStrategy)
    result = search.solveProblem()
    if result is not None:
        search.printResult(result)
 
        