# Name : Siddharth Nahar
# Entry No : 2016csb1043
# Date : 24/1/19

#Info : 
#   1. This File Takes list of Vertices and create a complete Graph
#   2. Create minimum Spanning Tree and calculate length of path
#   3. Path length will be our heuristic

import sys

# Using Prim's MST algorithm reference : https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
class GraphMST :

    #... Default constructor for Graph
    def __init__(self, vertices):
    
        self.vertices = vertices
        #Create a Graph using matrix representation
        self.graph = [ [0 for col in range(len(self.vertices))] for row in range(len(self.vertices)) ]
    
    #... Euclid Distance as measure of edge length
    def euclidDistance(self,i, j):
    
        point1 = self.vertices[i]
        point2 = self.vertices[j]
        
        return ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**0.5
    
    #... Assign edge length as this will be symmetric
    def assignCost(self):
    
        for i in range(len(self.vertices)):
        
            for j in range(i+1, len(self.vertices)):
                
                self.graph[i][j] = self.euclidDistance(i, j)            
                self.graph[j][i] = self.graph[i][j]
    
    
    #... Find Vertex with minimum Distance from vertices not yet selected 
    def minKey(self, key, mstSet): 
  
        # Initilaize min value 
        min = sys.maxint 
        #min_index = 0
        
        for v in range(len(self.vertices)): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 
  
        return min_index 
                  
    #... Create MST and return total length of path
    def primMST(self):
    
        self.assignCost()
        key = [sys.maxint]*len(self.vertices)           #... Key values used to pick minimum weight edge in cut 
        parent = [None]*len(self.vertices)          #... Stores mst generated
        
        key[0] = 0          #... Assign first key to 0
        mstSet = [False]*len(self.vertices)
        parent[0] = -1
    
        for i in range(len(self.vertices)):
        
            #... Pick minimum vertex from vertices not yet processed
            u = self.minKey(key, mstSet)
            
            #... Put vertex in Mst
            mstSet[u] = True
            
            #... Update Distance of Adjacent vertices distance if it's cost was greater and not yet selected
            for v in range(len(self.vertices)):
            
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                    key[v] = self.graph[u][v] 
                    parent[v] = u 
        
        totalCost = 0
        for i in range(1,len(self.vertices)): 
            totalCost = totalCost + self.graph[i][ parent[i] ]
            #print parent[i],"-",i,"\t",self.graph[i][ parent[i] ]        
        
        return totalCost
            
if __name__ == '__main__':

    vertices = [(1,0)]
    obj = GraphMST(vertices)
    
    obj.primMST()

