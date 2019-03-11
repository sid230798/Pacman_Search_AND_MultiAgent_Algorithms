'''

Name :- Siddharth Nahar
Entry No :- 2016csb1043
Date :- 05/03/19
Purpose :- 

1. This file contains Simulated Annealing Algorithm.
2. At each Iteration Route Distance is Heurestic

'''

import random
import math
#from matplotlib import pyplot as plt 

'''
def showGraph(TempList, PathCost):

    plt.plot(TempList, PathCost)
    plt.xlabel('Temperature')
    plt.ylabel('Path Cost')
    plt.savefig('Annealing.jpg')
    
    plt.show()
'''
    
#Eucleidan Distance for two points
def euclideanDistance(pt1, pt2):

    return ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)**0.5
    
#Print path as per suggesting in lab
def printPath(cityDict):

    x = ""
    y = ""

    for name, cord in cityDict:

        x += str(cord[0]) + "  "
        y += str(cord[1]) + "  "
        
    print "  "+x+"\n  "+y+'\n'
    
#This returns path sum
def getPath(path):

    sumPath = 0

    #Get new Length of Path
    for i in range(1, len(path)):

        sumPath += euclideanDistance(path[i-1][1], path[i][1])
        
    sumPath += euclideanDistance(path[-1][1], path[0][1])
    
    return sumPath
    
    
#2-opt way for list, i, k :
#Index from 0 to i-1 in forward manner
#Index from i to k in reverse
#Index from k+1 to end

def two_opt_way(originalPath, i, j):
    
    #Create new path for local search by 2-opt neighbourhood
    if i == 0 :
        newPath = originalPath[j::-1] + originalPath[j+1:]
    else :    
        newPath = originalPath[:i] + originalPath[j:i-1:-1] + originalPath[j+1:]
    
    return newPath, getPath(newPath)

#Simulate annealing algorithm run till we dont get better

def simulateAnnealing(cityDict):

    #Initial Temperature depends upon application for TsP deltaE is in range 1-5
    
    currentPath = cityDict
    currSumPath = getPath(currentPath)
    init_Temp = float(input("Enter the Initial Temperature to Set : "))
    alpha = float(input("Enter the rate of decrease : "))
    
    TempList = []
    PathCost = []
    T = init_Temp
    #Iterate till temperature it's greater than 0
    while T > 0 :
    
        print 'Path : \n'
        printPath(currentPath)
        print 'Length : '+str(currSumPath)
        print'---------------------------------------------------------------'
        
        TempList.append(T)
        PathCost.append(currSumPath)
        
        i = random.randint(1, len(cityDict))
        j = random.randint(1, len(cityDict))
        
        if i == j :
            continue
        
        p, q = min(i-1, j-1), max(i-1, j-1)
        i, j = p, q
        
        #Get new path 2-opt way local search
        newPath, sumPath = two_opt_way(currentPath[:], i, j)
        
        #Get delta_E
        deltaE = currSumPath - sumPath
        
        #If it's better path select it else select it by probablity e^(del_E/T)
        if deltaE > 0 :
        
            currentPath , currSumPath = newPath, sumPath
           
        else :
        
            prob = math.exp(deltaE/T)
            
            if(random.random() <= prob):
                currentPath, currSumPath = newPath, sumPath
        
        #Decrease Temp linearly              
        T = T - alpha          
        
    #showGraph(TempList, PathCost)           
