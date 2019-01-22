# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    "*** DFS implementation using Stack saving state,path and visited Nodes ***"
    #--------------------------------------------------------------------------------------------------------------
            
    #pathToGoal = list()             #... Saves Path to Reach that State(Sequence of States)
    actionsToPerform = list()       #... Saves Direction to follow to reach goal
    visitedStates = list()          #... Saves all visited nodes uptil Now So doesn't expand previous visited nodes
    
    fringe = util.Stack()           #... Use Stack from util file
    
    "*** Stack Stores Doublet as State, path from Start to this  ***"
    fringe.push((problem.getStartState(), actionsToPerform))
    
    #Using Iterative dfs
    
    while not fringe.isEmpty():
    
        #Get Top Element of Stack
        currentState, actionsToPerform = fringe.pop()
        
        if problem.isGoalState(currentState):           #... Check if State is Goal return actions
            
            return actionsToPerform
        
        visitedStates.append(currentState)          #... Append State to visited
        
        for nodeState, direction, cost in problem.getSuccessors(currentState):            #... Iterate through childs of state    
        
            if nodeState in visitedStates :         #... If State is already visited move to next successor
                
                continue
            '''
            if problem.isGoalState(nodeState) :     #... Check for Final States
                
                return actionsToPerform + [direction]
            '''
            "*** Push Element to fringe for future successor ***"
            fringe.push((nodeState, actionsToPerform + [direction]))
            
            
    return actionsToPerform
    
    #-------------------------------------------------------------------------------------------------------------------------------
    #util.raiseNotDefined()
     
"***Major Difference between DFS and BFS is time we add nodes to visited. We know that node appearing first in BFS is added but DFS add only when it has seen one***"
     
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    #-------------------------------------------------------------------------------------------------------------------------------
    #pathToGoal = list()             #... Saves Path to Reach that State(Sequence of States)
    actionsToPerform = list()       #... Saves Direction to follow to reach goal
    visitedStates = list()          #... Saves all visited nodes uptil Now So doesn't expand previous visited nodes
    
    fringe = util.Queue()           #... Use Queue from util file
    
    visitedStates.append(problem.getStartState())            #... Push the start state first
    
    "*** Queue Stores Doublet as State, path from Start to this ***"
    fringe.push((problem.getStartState(), actionsToPerform))
    
    #Using Iterative bfs
    
    while not fringe.isEmpty():
    
        #Get back Element of queue
        currentState, actionsToPerform = fringe.pop()
        
        if problem.isGoalState(currentState):           #... Check if State is Goal return actions
            
            return actionsToPerform
                
        for nodeState, direction, cost in problem.getSuccessors(currentState):            #... Iterate through childs of state    
        
            if nodeState in visitedStates :         #... If State is already visited move to next successor
                
                continue

            visitedStates.append(nodeState)          #... Append State to visited
            '''        
            if problem.isGoalState(nodeState) :     #... Check for Final States
                
                return actionsToPerform + [direction]
            '''
            "*** Push Element to fringe for future successor ***"
            fringe.push((nodeState, actionsToPerform + [direction]))
            
            
    return actionsToPerform        
    #-------------------------------------------------------------------------------------------------------------------------------
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    #-------------------------------------------------------------------------------------------------------------------------------
    actionsToPerform = list()       #... Saves Direction to follow to reach goal
    nodePath = dict()               #... Dictionary to save path uptil node
    visitedStates = list()          #... Saves all visited nodes uptil Now So doesn't expand previous visited nodes
    
    fringe = util.PriorityQueue()           #... Use PriorityQueue from util (cost as priority)
    
    "*** Push based on priority ***"
    fringe.push(problem.getStartState(), 0)          #... Push item and cost of 0 for first node
    nodePath[problem.getStartState()] = (list(), 0)          #... Stores node as key and it's Path to Reach as value
    
    while not fringe.isEmpty() :
    
        #Get least priority Element of Priorityqueue
        currentState = fringe.pop()
        actionsToPerform, costTillNode = nodePath[currentState]       #... Get the Current Path
        
        if problem.isGoalState(currentState):           #... Check if State is Goal return actions
            
            return actionsToPerform
        
        visitedStates.append(currentState)          #... Append State to visited
        
        for nodeState, direction, cost in problem.getSuccessors(currentState):            #... Iterate through childs of state    
        
        
            g_n = cost + costTillNode               #... Total Cost from Start to this node
            
            if nodeState in visitedStates :         #... If State is already visited move to next successor
                
                continue
            
            "*** Push Element to fringe for future successor ***"
            fringe.update(nodeState, g_n)           #... Insert cost got by priority
            
            "*** Update Path if Cost is less else previous cost and path are not update ***"
            if nodeState in nodePath :                
               _, costState = nodePath[nodeState]
               if costState > g_n :
                    nodePath[nodeState] = (actionsToPerform + [direction], g_n)        #... Update the Direction to Reach node
            else :
                    nodePath[nodeState] = (actionsToPerform + [direction], g_n)        #... Insert node to dictionary
                
    return actionsToPerform   
    
    #-------------------------------------------------------------------------------------------------------------------------------
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


#h_n is added only to total computational cost ,h_n is not added like g_n till node it's fixed
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    #-------------------------------------------------------------------------------------------------------------------------------
    actionsToPerform = list()       #... Saves Direction to follow to reach goal
    nodePath = dict()               #... Dictionary to save path uptil node
    visitedStates = list()          #... Saves all visited nodes uptil Now So doesn't expand previous visited nodes
    
    fringe = util.PriorityQueue()           #... Use PriorityQueue from util (cost as priority)
    
    "*** Push based on priority ***"
    fringe.push(problem.getStartState(), 0)          #... Push item and cost of 0 for first node
    nodePath[problem.getStartState()] = (list(), 0)          #... Stores node as key and it's Path to Reach as value
    
    while not fringe.isEmpty() :
    
        #Get least priority Element of Priorityqueue
        currentState = fringe.pop()
        actionsToPerform, costTillNode = nodePath[currentState]       #... Get the Current Path
        
        if problem.isGoalState(currentState):           #... Check if State is Goal and return actions
            
            return actionsToPerform
        
        visitedStates.append(currentState)          #... Append State to visited
        
        for nodeState, direction, cost in problem.getSuccessors(currentState):            #... Iterate through childs of state    
        
            "*** Get Total Cost f_n = g_n + h_n ***"
            g_n = cost + costTillNode               #... Total Cost from Start to this node
            f_n = g_n + heuristic(nodeState, problem)
            
            if nodeState in visitedStates :         #... If State is already visited move to next successor
                
                continue
            
            "*** Push Element to fringe for future successor ***"
            fringe.update(nodeState, f_n)           #... Insert cost got by priority
            
            "*** Update Path if Cost is less else previous cost and path are not update ***"
            if nodeState in nodePath :                
               _, costState = nodePath[nodeState]
               if costState > g_n :
                    nodePath[nodeState] = (actionsToPerform + [direction], g_n)        #... Update the Direction to Reach node
            else :
                    nodePath[nodeState] = (actionsToPerform + [direction], g_n)        #... Insert node to dictionary
                
    return actionsToPerform   
    
    #-------------------------------------------------------------------------------------------------------------------------------
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
