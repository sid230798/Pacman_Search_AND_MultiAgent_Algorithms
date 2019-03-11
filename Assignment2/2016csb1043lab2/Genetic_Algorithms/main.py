'''

Name :- Siddharth Nahar
Entry No :- 2016csb1043
Date :- 05/03/19
Purpose :- 

	1. This file is driver code to cll Genetic Algorithm
	2. This also read files accordingly.

'''

import sys
import geneticAlgo

if __name__ == '__main__' :

    #Read input from file
    gen_input = open(sys.argv[1] ,'r')
    
    #Stores in list the data
    cityDict = list()
    
    startLocation = (0, 0)
    max_gen = 100
    seed = 1
    
    for index, line in enumerate(gen_input):
    
        line = line.split()
        
        if line[0] == 'START_LOCATION' :
            startLocation = (float(line[1]), float(line[2]))
            
        elif line[0] == 'MAX_GEN' :
            max_gen = int(line[1])
        
        elif line[0] == 'RANDOM_SEED' :
            seed = int(line[1])
        
        elif line[0] == 'CUSTOM_NO' :
            continue
        
        else : 
        
            cityDict.append((line[0], (float(line[1]), float(line[2]))))
            
    geneticAlgo.startAlgo(startLocation, seed, max_gen, cityDict)
