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
	
	
g2= Graph()	
#for i in range (9):
	#g.addVertex(i)
	
	
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
		
		#creator(g2)

#for v in g2:
#	for w in v.getConnections():
	#	print("( %s , %s , %s )" % (v.getId(), w.getId(), v.getWeight(w)))
		

#Hard code the graph from the exercise
		
g2.addEdge( 1 , 2 , 2 )

g2.addEdge( 2 , 1 , 1 )
g2.addEdge( 2 , 4 , 4 )

g2.addEdge( 4 , 3 , 2 )
g2.addEdge( 4 , 5 , 1 )

g2.addEdge( 3 , 1 , 3 )
g2.addEdge( 3 , 4 , 1 )
g2.addEdge( 3 , 6 , 4 )

g2.addEdge( 6 , 4 , 1 )

g2.addEdge( 5 , 2 , 2 )
g2.addEdge( 5 , 7 , 1 )

g2.addEdge( 7 , 6 , 5 )
g2.addEdge( 7 , 5 , 2 )


def findMinWeight (toVisitList, dct):
	"""We use this function to find the vertex with the minimun weight each time
	toVisitList: is the a list with vertices we have to visit
	dct : is the connections until now from the root vertex
	We sort the list in order to take each time the vertex with the minimum number"""
	minWeight = 50
	idMin = -1
	toVisitList.sort()
	for i in toVisitList:
		if dct[i][1] < minWeight:
			minWeight = dct[i][1]
			idMin = i
	return minWeight, idMin		


def dijktra (rootVertex, g):
	"""This function solves the dijktra algorithm. It takes as parameters the root Vertex and the graph"""
	
	toVisit = [] 
	haveVisited = []
	dijktaDict = {}
	#numV = len(g.getVertices())
	
	#to find the first available connections
	for j in g.getVertex(rootVertex).getConnections():
		toVisit.append(j.getId())
	
	#we create a dictionary with the form: D = { vertex : (previous vertex, total weight), vertex2 :(previous vertex, total weight), ...}
	for i in g.getVertices():            
		if i in toVisit:
			dijktaDict[i] = (g.getVertex(rootVertex).getId(),g.getVertex(rootVertex).getWeight(g.getVertex(i)) )
		elif i == rootVertex:
			continue
		else:
			dijktaDict[i] = None
	
	#lets find which vertex to visit first
	minWeight , idMin = findMinWeight(toVisit, dijktaDict)
	haveVisited.append(idMin)
	toVisit.remove(idMin)
	
	#print('First stop {} with weight {}'.format(idMin,minWeight ))
	
	# while we have verteces to visit : ...
	while len(toVisit) != 0:
		
		print('Next stop {} with weight {}'.format(idMin,minWeight ))
		lstConnidMin = []	
		#lets find the connections of the first visited vertex
		for i in g.getVertex(idMin).getConnections():						
			if i.getId() == rootVertex:
				continue
			lstConnidMin.append(i.getId())
		
		print('{} connects with {}'.format(idMin, lstConnidMin))
		
		#for each vertex in connections we find the total weight from the root vertex and if is smaller
		#we replace the root in dictionary
		for i in lstConnidMin:
			weightI = g.getVertex(idMin).getWeight(g.getVertex(i))
			sumWeight = weightI + minWeight
			if dijktaDict[i] == None or sumWeight < dijktaDict[i][1]:
				newpath = [i,idMin]
				try:
					nextV = dijktaDict[idMin][0]
					while nextV != rootVertex:
						newpath.append(nextV)
						nextV = dijktaDict[nextV][0]
					nextV = dijktaDict[nextV][0]	
				except:                                  # connection is none
					nextV = rootVertex
					newpath.append(nextV)
				
				newpath.reverse()
				dijktaDict[i]= (idMin, sumWeight)
				print('We change {} because the weight in new path is {}'.format(i,sumWeight ))
				print('The new path is :')
				print(*newpath, sep= '->')
				
				if i not in toVisit:
					toVisit.append(i)  
					
			else:
				print('In {} nothing change because the previous weight was {} and the new one is {} '.format(i, dijktaDict[i][1], sumWeight))
				
		minWeight , idMin = findMinWeight(toVisit, dijktaDict)
		haveVisited.append(idMin)
		toVisit.remove(idMin)
		print(' ')
		#print('Next stop {} with weight {}'.format(idMin,minWeight ))
		
	return dijktaDict


head = 5
djk = dijktra(head, g2)

print(' ')
print('----------------------------')
print(' ')

for verx in djk.keys():
	nextvertex = djk[verx][0]
	weight = djk[verx][1]
	if nextvertex == head:
		sortPath = [verx,nextvertex]
		
	else:
		sortPath = [verx,nextvertex]
		while nextvertex != head:
			nextvertex = djk[nextvertex][0]
			sortPath.append(nextvertex)
	sortPath.reverse()
	print('The shortest route to {vertex} is :'.format(vertex = verx))
	print(*sortPath, sep= '->')
	print('With total weight {}'.format(weight))
	print(' ')