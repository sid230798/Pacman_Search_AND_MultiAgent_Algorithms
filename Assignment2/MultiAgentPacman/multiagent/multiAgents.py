# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        powerPellet = successorGameState.getCapsules()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        
        '''
        
        	I will use :
        		1. Sum of distance of foods
        		2. Number of foods as this represents if it is at food 
        		2. Minimum distance from non-scared ghosts
        		
        		f(s) = w1*f1(s) + w2*f2(s)
        '''
        
        foodList = newFood.asList()

        if(successorGameState.isWin()):
	        return float('Inf')

        distFood = [util.manhattanDistance(newPos, pos) for pos in foodList]
        minGhost = float('Inf')

        for ghost in newGhostStates :
	        
	        if(ghost.scaredTimer <= 0):
	        
		        tempDist = util.manhattanDistance(newPos, ghost.getPosition())
		        if(tempDist < minGhost):
			        minGhost = tempDist	

        if(minGhost == 0):
        
             return -float('Inf')

        if(minGhost >= 3):
            return 1.0/sum(distFood) + 3.0/len(distFood) + random.random()*0.001
        else:
            return 1.0/sum(distFood) + 3.0/len(distFood) - 4.0/minGhost
           
        #print score

        #return score
        "*** YOUR CODE HERE ***"
        #return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
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
                
        actionList = minMax(gameState, 0, 0)
        
        return actionList[0]
            
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def minValue(currentState, depth, agentIndex, alpha, beta):
        
            #This function calls for Ghosts action
            
            #Get all Actions for ghosts
            actionGhosts = currentState.getLegalActions(agentIndex)
            
            if(len(actionGhosts) == 0):
                return ("", self.evaluationFunction(currentState))
                    
            minValAction = ("", float('Inf'))
            for action in actionGhosts:
            
                newState = currentState.generateSuccessor(agentIndex, action)
                v_val = minMax(newState, depth, agentIndex+1, alpha, beta)
                
                if(v_val[1] <= minValAction[1]):
                    minValAction = (action, v_val[1])
                    
                if(v_val[1] < alpha):
                    return minValAction
                    
                if(v_val[1] < beta):
                    beta = v_val[1]
                    
            return minValAction
            
        def maxValue(currentState, depth, agentIndex, alpha, beta):
        
            #Get all Actions for Pacman
            actionPacman = currentState.getLegalActions(agentIndex)
            
            if(len(actionPacman) == 0):
                return ("", self.evaluationFunction(currentState))
                    
            maxValAction = ("", -float('Inf'))
            for action in actionPacman:
            
                newState = currentState.generateSuccessor(agentIndex, action)
                v_val = minMax(newState, depth, agentIndex+1, alpha, beta)
                
                if(v_val[1] >= maxValAction[1]):
                    maxValAction = (action, v_val[1])
                
                if(v_val[1] > beta):
                    return maxValAction
                    
                if(v_val[1] > alpha):
                    alpha = v_val[1]
                    
            return maxValAction
            
        def minMax(currentState, depth, agentIndex, alpha, beta):
        
            #Change to pacman if agentIndex is greater
            if agentIndex >= currentState.getNumAgents() :
       
                agentIndex = 0
                depth += 1
                
            if(self.depth == depth or currentState.isWin() or currentState.isLose()):
                return ("", self.evaluationFunction(currentState))
            
            if(agentIndex == 0):
                return maxValue(currentState, depth, agentIndex, alpha, beta)
            else:
                return minValue(currentState, depth, agentIndex, alpha, beta)
                
        actionList = minMax(gameState, 0, 0, -float('Inf'), float('Inf'))
        
        return actionList[0]
            
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        
        def expectMinValue(currentState, depth, agentIndex):
        
            #This function calls for Ghosts action
            
            #Get all Actions for ghosts
            actionGhosts = currentState.getLegalActions(agentIndex)
            prob = 1.0/len(actionGhosts)
            
            if(len(actionGhosts) == 0):
                return ("", self.evaluationFunction(currentState))
                    
            minValAction = ("", 0)
            score = 0
            for action in actionGhosts:
            
                newState = currentState.generateSuccessor(agentIndex, action)
                v_val = expectMinMax(newState, depth, agentIndex+1)
                
                '''
                if(v_val[1] <= minValAction[1]):
                    minValAction = (action, v_val[1])
                '''
                score += prob*v_val[1]
                minValAction = (action, score)
                    
            return minValAction
            
        def maxValue(currentState, depth, agentIndex):
        
            #Get all Actions for Pacman
            actionPacman = currentState.getLegalActions(agentIndex)
            
            if(len(actionPacman) == 0):
                return ("", self.evaluationFunction(currentState))
                    
            maxValAction = ("", -float('Inf'))
            for action in actionPacman:
            
                newState = currentState.generateSuccessor(agentIndex, action)
                v_val = expectMinMax(newState, depth, agentIndex+1)
                
                if(v_val[1] > maxValAction[1]):
                    maxValAction = (action, v_val[1])
                    
            return maxValAction
            
        def expectMinMax(currentState, depth, agentIndex):
        
            #Change to pacman if agentIndex is greater
            if agentIndex >= currentState.getNumAgents() :
       
                agentIndex = 0
                depth += 1
                
            if(self.depth == depth or currentState.isWin() or currentState.isLose()):
                return ("", self.evaluationFunction(currentState))
            
            if(agentIndex == 0):
                return maxValue(currentState, depth, agentIndex)
            else:
                return expectMinValue(currentState, depth, agentIndex)
                
        actionList = expectMinMax(gameState, 0, 0)
        
        return actionList[0]
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    successorGameState = currentGameState
    newPos = successorGameState.getPacmanPosition()
    newFood = successorGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    powerPellet = successorGameState.getCapsules()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    
    '''
    
    	I will use :
    		1. Sum of distance of foods
    		2. Number of foods as this represents if it is at food 
    		2. Minimum distance from non-scared ghosts
    		
    		f(s) = w1*f1(s) + w2*f2(s)
    '''
    
    foodList = newFood.asList()

    if(successorGameState.isWin()):
        return float('Inf')

    distFood = [util.manhattanDistance(newPos, pos) for pos in foodList]
    minGhost = float('Inf')

    for ghost in newGhostStates :
        
        if(ghost.scaredTimer <= 0):
        
	        tempDist = util.manhattanDistance(newPos, ghost.getPosition())
	        if(tempDist < minGhost):
		        minGhost = tempDist	

    if(minGhost == 0):
    
         return -float('Inf')

    if(minGhost >= 3):
        return 1.0/sum(distFood) + 3.0/len(distFood) + random.random()*0.01
    else:
        return 1.0/sum(distFood) + 3.0/len(distFood) - 4.0/minGhost
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

