class Graph(): 
#Constructor of Graph
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]
        \
        for row in range(vertices)] 
#Check if the color assignment is valid for graph 
    def isValid(self, v, colour, c): 
        for i in range(self.V): 
            if self.graph[v][i] == 1 and colour[i] == c: 
                return False
        return True
      
#functions to implement graph coloring algorithm using dfs and forward checking
    def graphColour(self, m, colour, v): 
        if v == self.V: 
            return True
  
        for c in range(1, m+1): 
            if self.isValid(v, colour, c) == True: 
                colour[v] = c 
                if self.graphColour(m, colour, v+1) == True: 
                    return True
                colour[v] = 0
  
    def graphColouring(self, m): 
        colour = [0] * self.V 
        if self.graphColour(m, colour, 0) == None: 
            return False
  
        # Print the solution 
        print("Solution exist and Following are the assigned colours:")
        for c in colour: 
            print(c), 
        return True
    # pick node using MRV
    def pickNode(self, initialNode):
        maxCount = 0
        selectedNode = ''
        # the very first node
        if (initialNode == ''):
            for node, neighbourList in self.adjacencyList.items():
                if (len(neighbourList) > maxCount and self.color[node] == 0):
                    maxCount = len(neighbourList)
                    selectedNode = node
        # the other nodes
        else:
            for i in range(len(self.adjacencyList[initialNode])):
                childNode = self.adjacencyList[initialNode][i]
                if (self.color[childNode] == 0 and len(self.adjacencyList[childNode]) > maxCount):
                    maxCount = len(self.adjacencyList[childNode])
                    selectedNode = childNode

        return selectedNode
        
        
    def getNodeWithMRV(self, parentNode, colorLimit):
        selectedNode = ''
        minCount = 0
        
        for i in range(len(self.adjacencyList[parentNode])):
            childNode = self.adjacencyList[parentNode][i]
            countColor = 0
            for c in range(1, colorLimit+1):
                if(self.isValid(childNode, c) == True):
                    countColor += 1
            if (countColor < minCount):
                selectedNode = childNode
                
        return selectedNode
    
        
# Main Code 
countrymap  = Graph(3) 
# graph of countries in the form of adjacency matrix
countrymap.graph = [[0,1,0], [1,0,1], [0,1,0]] 
# col is number of colors which can totally be assigned to graph
col=3
countrymap.graphColouring(col) 
# Now using Heuristic Approach
