'''

Name :- Siddharth Nahar
Entry No :- 2016csb1043
Date :- 05/03/19
Purpose :- 

	1. This file is driver code to call Hill Climbing, Simulated Annealing and Genetic Algorithm
	2. This also read files accordingly.

'''

import sys
import HillClimb


if __name__ == '__main__' :

	#Reading Input from file
	hill_climb = open(sys.argv[1], 'r')

	# This dictionary saves elements as City name ,(x,y)	
	cityDict = list()
	
	for index, line in enumerate(hill_climb) :
	
		#Naming cities with capital Letters
		count = 65
		
		#Split line in according to space
		line = line.split()
		
		#Iterate through coordinates
		for cord in line:
			
			xtuple = (float(cord),)
			
			#Create Dictionary as city name and it's coordinates
			if index == 1:
				cityDict[count-65] = (chr(count), cityDict[count-65][1] + xtuple)
			else:
				cityDict.append((chr(count), xtuple))
				
			count += 1
	
	#cityDict = collections.OrderedDict(sorted(cityDict.items()))
	#print cityDict
	HillClimb.hillClimb(cityDict)
	#SimulatedAnnealing.simulateAnnealing(cityDict)
