'''

Name :- Siddharth Nahar
Entry No :- 2016csb1043
Date :- 05/03/19
Purpose :- 

	1. This file runs actual genetic algorithm.

'''

import random
#from matplotlib import pyplot as plt 

#Global Variables used in almost every function call
cityList = []
startPos = (0,0)

#---------------------------------------------------------

#Just to show Results Graphically
'''
def showGraph(gen, PathCost):

    #Plt functions called
    plt.plot(gen, PathCost)
    plt.xlabel('Generation')
    plt.ylabel('Path Cost')
    plt.savefig('Genetic.jpg')
    
    plt.show()
'''

#-------------------------------------------------------------

#Function to calculate eucledian distance between two points
def euclideanDistance(pt1, pt2):

    return ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)**0.5

#------------------------------------------------------------------

#Fitness for function to evaluate indivisual 1/pathCost for staying with conventions    
def fitness(chromosome):

    sumPath = 0

    #Get new Length of Path
    for i in range(1, len(chromosome)):

        sumPath += euclideanDistance(cityList[chromosome[i-1]][1], cityList[chromosome[i]][1])
    
    sumPath += euclideanDistance(cityList[chromosome[0]][1], startPos) + euclideanDistance(cityList[chromosome[-1]][1], startPos)
        
    #Return inverse for fitness proportonal to best child    
    return 1.0/sumPath

#----------------------------------------------------------------------

#Ordered Crossover method
#Select two indices i,j randomly
#Create two offspring have same characteristc from two parent between i,j
#Put Relative ordereing of Second parent to first child and First parent to second child

def getCrossover(parent1, parent2):

    #Select Randomly two indices
    i = random.randint(0, len(parent1))
    j = random.randint(0, len(parent1))
    
    i, j = min(i, j), max(i, j)
    
    #i, j = 3, 6 
    
    #Get Relative ordering of filling childrens  
    cycled_parent1 = parent1[j:] + parent1[:j]
    cycled_parent2 = parent2[j:] + parent2[:j]
    
    #Offspring contains i,j part intact from  both parents
    offspring1 = parent1[i:j]
    offspring2 = parent2[i:j]
    
    temp1 = []
    temp2 = []
    
    #Fill OffSpring in order of opposite parent Offspring1 derived from parent2
    for a in cycled_parent2 :
    
        if a not in offspring1 :
     
            temp1.append(a)
    
    #Offspring2 derived from parent1
    for a in cycled_parent1 :
    
        if a not in offspring2 :
            
            temp2.append(a)
    
    #Append results to offspring to fill empty places        
    offspring1 = temp1[(len(parent1)-j):] + offspring1 + temp1[:(len(parent1)-j)]
    offspring2 = temp2[(len(parent1)-j):] + offspring2 + temp2[:(len(parent1)-j)]
    
    #Return most optimal child produced
    if(fitness(offspring1) >= fitness(offspring2)):
        return offspring1
    
    return offspring2        

#---------------------------------------------------------------------------------

#Get mutation of indivisual    
#Select two indices i,j randomly
#Mutaion list[:i] + rev(list[i:j]) + list[j:]

def mutation(indivisual):

    #Get two indices randomly
    i = random.randint(0, len(indivisual))
    j = random.randint(0, len(indivisual))
    
    i, j = min(i, j), max(i, j)      

    #Reverse list between i,j and keep rest of parts intact
    if i == 0:
        return indivisual[:i] + indivisual[j::-1] + indivisual[j+1:]
        
    return indivisual[:i] + indivisual[j:i-1:-1] + indivisual[j+1:]

#---------------------------------------------------------------------------------- 

#Get two random indices by weights of fitness function
#Each index prob = fitness/sum(fitness)

def getTwoRandomIntegerByWeights(weights):

    #Get two random values
    u = random.random()
    v = random.random()
    
    u, v = min(u, v), max(u, v)
    i = 0
    j = 0
    
    sum_weight = weights[0]
    
    #If index is at that probablity select that
    for index in range(1, len(weights)):
    
        if sum_weight > u : 
            i = index
            break
            
    #Similarly select index with v probablity
    for index in range(1, len(weights)):
        
        if sum_weight > v :
            j = index
            break
    
    #Return two indices        
    return i, j

#----------------------------------------------------------------------------------

#Functions generate new generation
#Calculate probablity of each indivisual bu fitness/sum(fitness)
#Generate two random integer
#Do crossover by corssover probablity
#Do mutation by mutation probab lity
    
def getNewGen(population, fitness_dash):

    #Get indiviusal probablity
    weights = [ x/sum(fitness_dash) for x in fitness_dash ]
       
    newPop = list()
    
    #print fitness(population[0])
    while len(newPop) < len(population) :
    
        #Get two random indices
        cross_prob, mut_prob = 0.9, 0.1
        i, j = getTwoRandomIntegerByWeights(weights)
        
        #Select best of two parents if crossover is not selected
        a, b = fitness(population[i]), fitness(population[j])
        if(a >= b):
            off = population[i]
        else:
            off = population[j]
        
        #Perform crossover by crossover prob     
        if(random.random() <= cross_prob):
            
            #off = population[0]
            off= getCrossover(population[i], population[j])
            #newPop.append(off)
        
        #Perform mutation of offspring by nutation prob
        if(random.random() <= mut_prob):
            off = mutation(off)
            
        newPop.append(off)
        
    #Return new Population    
    return newPop
    
#-------------------------------------------------------------------    

#Start Algo is driver code gets call from main function
#Assigns different values depending upon problem
#Call next generation for max_gen
#Draws a graph for it

def startAlgo(startLocation, seed, max_gen, cityDict) :

    #Assign global list of city and start position
    global cityList, startPos
    cityList = cityDict
    startPos = startLocation
    
    #Initial List , Population, assign Random seed
    initial_list = range(len(cityList))
    population_n = 5
    populations = [initial_list]
    
    random.seed(seed)
    
    print cityList
    #Generates initial population
    for i in range(1, population_n):
    
        temp = populations[i-1][:]
        random.shuffle(temp)
        populations.append(temp)
    
    #print populations
    
    current_state = populations
    #fitness_dash = [ 1/fitness(x) for x in current_state ]
    #fitness_dash = sorted(fitness_dash, reverse = True)
    #print current_state, fitness_dash    
    
    gen = []
    pathCost = []
    
    #Call for each generation and sort according to fitness values
    for i in range(max_gen+1):
    
        gen.append(i)
        
        #Sort population by fitness and prints its value
        current_state = sorted(current_state, key = fitness, reverse = True)
        fitness_dash = [ fitness(x) for x in current_state ]
        fitness_dash = sorted(fitness_dash)
        print "Index : "+str(i)+", Fitness : "+str(1/fitness_dash[0]) 
        pathCost.append(1/fitness_dash[0]) 
        current_state = getNewGen(current_state, fitness_dash)
        
        
    #showGraph(gen, pathCost)

#-----------------------------------------------------------------------

if __name__ == '__main__':

    #startAlgo((0,0),1, 1, [(1,(1,1)),(2,(2,2)),(3,(3,3)),(4,(4,4))])
    getCrossover([3,4,8,2,7,1,6,5],[4,2,5,1,6,8,3,7])
            
