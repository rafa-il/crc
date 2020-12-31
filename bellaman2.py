#!/usr/bin/env python3

print(' ')
print(' ')
print('---- Start ---- ')
print(' ')

class Vertex:
	def __init__(self,key):
		self.id = key
		self.connectedTo = {}
		
	def addNeighbor(self,nbr,weight=0):
		self.connectedTo[nbr]=weight
		
		#def __str__(self):
		#return str(self.id) + ' connectedTo ' + str([x.id for x in self.connectedTo])
		
	def getConnections(self):
		return self.connectedTo.keys()
	
	def getId(self):
		return self.id
	
	def getWeight(self, nbr):
		return self.connectedTo[nbr]
	
class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0
		
	def addVertex(self, key):
		self.numVertices += 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex
	
	def getVertex(self,n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None
		
	def __contains__(self,n):
		return n in self.vertList
	
	def addEdge(self, frm, to, weight =0):
		if frm not in self.vertList:
			newV = self.addVertex(frm)
		if to not in self.vertList:
			newV = self.addVertex(to)
		self.vertList[frm].addNeighbor(self.vertList[to], weight)
		
	def getVertices(self):
		return self.vertList.keys()
	
	def __iter__(self):
		return iter(self.vertList.values())
	
	
def creator(graph):
	"""We use this function to create the graph"""
	
	numVertices = int(input('How many vertices ?'))
	while True:
		f = input('from :')
		t = input('to :')
		w = input('weight :')
		
		con = input("continue? y or n ?  ")
		while  con != 'y' and  con !='n':
			con = input("continue? y or n ?")
		if con == 'n':
			graph.addEdge(f,t,w)
			break
		graph.addEdge(f,t,w)
		
		
		
		
g= Graph()

g.addEdge( 1 , 2 , 1 )
g.addEdge( 1 , 4 , 1 )

g.addEdge( 2 , 1 , 1 )
g.addEdge( 2 , 4 , 1 )
g.addEdge( 2 , 5 , 3 )
g.addEdge( 2 , 3 , 7 )

g.addEdge( 3 , 2 , 7 )
g.addEdge( 3 , 5 , 3 )
g.addEdge( 3 , 6 , 1 )

g.addEdge( 4 , 1 , 1 )
g.addEdge( 4 , 2 , 1 )
g.addEdge( 4 , 5 , 3 )
g.addEdge( 4 , 7 , 1 )

g.addEdge( 5 , 3 , 3 )
g.addEdge( 5 , 2 , 3 )
g.addEdge( 5 , 4 , 3 )
g.addEdge( 5 , 7 , 2 )
g.addEdge( 5 , 6 , 1 )

g.addEdge( 6 , 3 , 1 )
g.addEdge( 6 , 5 , 1 )
g.addEdge( 6 , 8 , 1 )
g.addEdge( 6 , 9 , 1 )

g.addEdge( 7 , 4 , 1 )
g.addEdge( 7 , 5 , 2 )
g.addEdge( 7 , 8 , 1 )

g.addEdge( 8 , 7 , 1 )
g.addEdge( 8 , 6 , 1 )
g.addEdge( 8 , 9 , 2 )

g.addEdge( 9 , 6 , 1 )
g.addEdge( 9 , 8 , 2 )



def bellman(rootVertex, g):
	
	bellDict = {}
	listToVisit = []
	
	#we find the verteces with one hop distance
	for i in g.getVertex(rootVertex).getConnections():
		listToVisit.append(i.getId())
		
		
	#lets create the bellman dictionary 
	#D = { vertex : (previous vertex, total weight), vertex2 :(previous vertex, total weight), ...}
		
	for i in g.getVertices(): 
		if i in listToVisit:
			bellDict[i] = (g.getVertex(rootVertex).getId(),g.getVertex(rootVertex).getWeight(g.getVertex(i)) )
		elif i == rootVertex:
			continue
		else:
			bellDict[i] = None
		
		
	while len(listToVisit) != 0:
		i=0
		vertToVisit = listToVisit[i]
		listToVisit.remove(vertToVisit)
		weight = bellDict[vertToVisit][1]
		
		for j in g.getVertex(vertToVisit).getConnections():
			v = j.getId()
			
			if v == rootVertex:
				continue
			else:
				totalWeight = g.getVertex(vertToVisit).getWeight(g.getVertex(v)) + weight
				if bellDict[v] == None or totalWeight < bellDict[v][1] :
					bellDict[v] = (vertToVisit,totalWeight)
					if v not in listToVisit : listToVisit.append(v) 

	return bellDict

root = 3
belDct = bellman(root,g)

print(' ')
print(' - - - - - - - - - - - - - - - - - ')
print(' ')
print(belDct)
for verx in belDct.keys():
	nextvertex = belDct[verx][0]
	weight = belDct[verx][1]
	if nextvertex == root:
		sortPath = [verx,nextvertex]
		
	else:
		sortPath = [verx,nextvertex]
		while nextvertex != root:
			nextvertex = belDct[nextvertex][0]
			sortPath.append(nextvertex)
	sortPath.reverse()
	print('The shortest route to {vertex} is :'.format(vertex = verx))
	print(*sortPath, sep= '->')
	print('With total weight {}'.format(weight))
	print(' ')
	