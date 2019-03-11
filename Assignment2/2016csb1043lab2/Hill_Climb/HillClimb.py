'''

Name :- Siddharth Nahar
Entry No :- 2016csb1043
Date :- 05/03/19
Purpose :- 

1. This file contains Hill Climbing Algorithm.
2. At each Iteration Route Distance is Heurestic

'''

#Eucleidan Distance for two points
def euclideanDistance(pt1, pt2):

    return ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)**0.5

#Get path dist in O(1)
def getNewPathDist(originalPath, i, j):

    #Get path that's gone be substrated
    pathSub = euclideanDistance(originalPath[i][1], originalPath[i-1][1]) + euclideanDistance(originalPath[i][1], originalPath[i+1][1])

    #Check for corner cases j = n-1
    if(j == len(originalPath)-1):
        pathSub += euclideanDistance(originalPath[j][1], originalPath[j-1][1]) + euclideanDistance(originalPath[j][1], originalPath[0][1])
    else:
        pathSub += euclideanDistance(originalPath[j][1], originalPath[j-1][1]) + euclideanDistance(originalPath[j][1], originalPath[j+1][1])
        
    return pathSub


#This function swap two position and calculates new path distance in O(1)
def swapPosPath(originalPath, originalSum, i, j):

    #Get path that's gonna be reduced
    pathSub = getNewPathDist(originalPath, i, j)
        
    #Swap their position to create new path  
    temp = originalPath[i]
    originalPath[i] = originalPath[j]
    originalPath[j] = temp

    #Get path that's gonna be added
    pathAdd = getNewPathDist(originalPath, i, j)

    newPathDist = originalSum - pathSub + pathAdd

    return originalPath, newPathDist      

#Print path as per suggesting in lab
def printPath(cityDict):

    x = ""
    y = ""

    for name, cord in cityDict:

        x += str(cord[0]) + "  "
        y += str(cord[1]) + "  "
        
    print "  "+x+"\n  "+y+'\n'

#Main code called from main.py
def hillClimb(cityDict):

    #Iterate till we get better solution
    sumPath = 0

    #Get Original Length of Path
    for i in range(1, len(cityDict)):

        sumPath += euclideanDistance(cityDict[i-1][1], cityDict[i][1])
        
    sumPath += euclideanDistance(cityDict[-1][1], cityDict[0][1])

    #print sumPath

    #Variables for loop invariant and storing minPath, cost, indices to swap
    check = 1

    bestI = -1
    bestJ = -1

    minPath, minCost = cityDict, sumPath
        
    #Iterate indefinitely till we dont find a better solution    
    while check == 1 :

        check = 0
        print 'Path : \n'
        printPath(cityDict)
        print 'Length : '+str(sumPath)
        
        #Check for each pair for better solution
        for i in range(0, len(cityDict)-1):
            for j in range(i+1, len(cityDict)):
                
                #Get new PAth and it's length
                newPath, newsumPath = swapPosPath(cityDict[:], sumPath, i, j)
                
                #Check if it's a better solution
                if(newsumPath < minCost):
                    check = 1
                    minPath = newPath
                    minCost = newsumPath
                    bestI = i
                    bestJ = j
                    
        if check == 1:
            print '\nSwap Nodes at position '+str(bestI+1)+' and '+str(bestJ+1)+'\n'    
        cityDict, sumPath = minPath, minCost
    	    
        

