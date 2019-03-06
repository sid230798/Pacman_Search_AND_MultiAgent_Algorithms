'''

    Name :- Siddharth Nahar
    Entry No :- 2016csb1043
    Date :- 06/03/19
    
    Purpose :- 
    
        1. Computes MinMax Algorithm call for minMax
        2. Get Call from Pacman

'''

def minValue(currentState, depth, agentIndex):
        
    #This function calls for Ghosts action
    
    #Get all Actions for ghosts
    actionGhosts = currentState.getLegalActions(agentIndex)
    
    if(len(actionGhosts) == 0):
        return ("", self.evaluationFunction(currentState))
            
    minValAction = ("", float('Inf'))
    for action in actionGhosts:
    
        newState = currentState.generateSuccessor(agentIndex, action)
        v_val = minMax(newState, depth, agentIndex+1)
        
        if(v_val[1] <= minValAction[1]):
            minValAction = (action, v_val[1])
            
    return minValAction
    
def maxValue(currentState, depth, agentIndex):

    #Get all Actions for Pacman
    actionPacman = currentState.getLegalActions(agentIndex)
    
    if(len(actionPacman) == 0):
        return ("", self.evaluationFunction(currentState))
            
    maxValAction = ("", -float('Inf'))
    for action in actionPacman:
    
        newState = currentState.generateSuccessor(agentIndex, action)
        v_val = minMax(newState, depth, agentIndex+1)
        
        if(v_val[1] >= maxValAction[1]):
            maxValAction = (action, v_val[1])
            
    return maxValAction
    
def minMax(currentState, depth, agentIndex):

    #Change to pacman if agentIndex is greater
    if agentIndex >= currentState.getNumAgents() :

        agentIndex = 0
        depth += 1
        
    if(self.depth == depth or currentState.isWin() or currentState.isLose()):
        return ("", self.evaluationFunction(currentState))
    
    if(agentIndex == 0):
        return maxValue(currentState, depth, agentIndex)
    else:
        return minValue(currentState, depth, agentIndex)
