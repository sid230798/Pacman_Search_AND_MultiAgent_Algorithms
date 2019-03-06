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
import collections

if __name__ == '__main__' :

	#Reading Input from file
	hill_climb = open('TspInput.txt', 'r')

	# This dictionary saves elements as City name ,(x,y)	
	cityDict = dict()
	
	for line in hill_climb :
	
		#Naming cities with capital Letters
		count = 65
		
		#Split line in according to space
		line = line.split()
		
		#Iterate through coordinates
		for cord in line:
			
			xtuple = (float(cord),)
			
			#Create Dictionary as city name and it's coordinates
			if chr(count) in cityDict:
				cityDict[chr(count)] = cityDict[chr(count)] + xtuple
			else:
				cityDict[chr(count)] = xtuple
				
			count += 1
	
	cityDict = collections.OrderedDict(sorted(cityDict.items()))
	print cityDict
	HillClimb.getSolution(cityDict)
