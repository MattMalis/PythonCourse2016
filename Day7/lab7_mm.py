"""Data Structures
Working with Graphs/Networks"""

def makeLink(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1
  return G 

# Ring Network
ring = {} # empty graph 

n = 5 # number of nodes 

# Add in edges
for i in range(n):
  ring = makeLink(ring, i, (i+1)%n)

# How many nodes?
print len(ring)

# How many edges?
print sum([len(ring[node]) for node in ring.keys()])/2 


# Grid Network
# TODO: create a square graph with 256 nodes and count the edges 
# TODO: define a function countEdges


def makeSquareGraph(num_nodes):
	G = {}
	sqrt_n = num_nodes**(.5)
	for i in range(num_nodes):
		if ( (i%sqrt_n)!=(sqrt_n - 1) ) :
			makeLink(G, i, i+1)
		if ( (i//sqrt_n)!=(sqrt_n - 1) ):
			makeLink(G, i, i+int(sqrt_n))
	return G

sq_gr = makeSquareGraph(256)

def makeRectGraph(num_row, num_col):
	R = {}
	for i in range(num_row * num_col):
		if ( (i%num_col) != (num_col-1) ): # if it's not on the far right of the graph
			makeLink(R, i, i+1)
		if ( (i//num_col) != (num_row - 1) ): # if it's not at the bottom of the graph
			makeLink(R, i, i+num_col)
	return R


def print_graph(g):
	for key in g.keys():
		print "node: " + str(key) + ", links: " + str(g[key])

def count_edges(g):
	sum = 0
	for node in g.keys():
		for i in g[node].keys():
			sum+=1
	return sum/2

	

# Social Network
class Actor(object):
  def __init__(self, name):
    self.name = name 
  def __repr__(self):
    return self.name 

ss = Actor("Susan Sarandon")
jr = Actor("Julia Roberts")
kb = Actor("Kevin Bacon")
ah = Actor("Anne Hathaway")
rd = Actor("Robert DiNero")
ms = Actor("Meryl Streep")
dh = Actor("Dustin Hoffman")

movies = {}

makeLink(movies, dh, rd) # Wag the Dog
makeLink(movies, rd, ms) # Marvin's Room
makeLink(movies, dh, ss) # Midnight Mile
makeLink(movies, dh, jr) # Hook
makeLink(movies, dh, kb) # Sleepers
makeLink(movies, ss, jr) # Stepmom
makeLink(movies, kb, jr) # Flatliners
makeLink(movies, kb, ms) # The River Wild
makeLink(movies, ah, ms) # Devil Wears Prada
makeLink(movies, ah, jr) # Valentine's Day

# How many nodes in movies?
# How many edges in movies?

def tour(graph, nodes):
  for i in range(len(nodes)):
    node = nodes[i] 
    if node in graph.keys():
      print node 
    else:
      print "Node not found!"
      break 
    if i+1 < len(nodes):
      next_node = nodes[i+1]
      if next_node in graph.keys():
        if next_node in graph[node].keys():
          pass 
        else:
          print "Can't get there from here!"
          break 

# TODO: find an Eulerian tour of the movie network and check it 
#movie_tour = [] 
#tour(movies, movie_tour)



#print findPath(movies, jr, ms)

def EulerExists(graph):
	# Euler Path exists iff exactly zero or two edges have odd number of vertices
	num_odd=0
	for node in graph.keys():
		if len(graph[node])%2:
			num_odd+=1
	if ( num_odd!=0 and num_odd!=2 ):
		print "Graph has %s odd vertices; no Euler Circuit exists" %num_odd
		return False
	return True

def EulerPath(graph):
	eulers = []
	for node in graph.keys():
		path = EulerFromStart(graph, node)
		if path: eulers.append(path)
	print "len(eulers): " + str(len(eulers))
	if (len(eulers)>0):
		return eulers
	print "Euler Path does not exist"
	return None

def EulerFromStart(graph, start, path=[]):
	if start in path:
		return None
	path = path+[start]
	if sorted(path)==sorted(graph.keys()):
		print "path: " + str(path)
		return path
	if not graph.has_key(start):
		print "Key '%s' not in graph" %(start)
		return None
	for node in graph[start]:
		try_this = 	EulerFromStart(graph, node, path)
		if try_this: 
			return try_this



# TODO: implement findShortestPath()
# print findShortestPath(movies, ms, ss)

def findPath(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = findPath(graph, node, end, path)
                if newpath: return newpath
        return None

def findAllPaths(graph, start, end, cur_path=[], all_paths=[]):
        cur_path = cur_path + [start]
        if start == end:
        	all_paths.append(cur_path)
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in cur_path:
                newpaths = findAllPaths(graph, node, end, cur_path, all_paths)
              	#print "cur_path: %s \n newpath: %s" %(cur_path, newpaths)
                if (len(newpaths)>0): 
                	for p in newpaths:
                		if len(p)>0:
                			if not p in all_paths:
		                		all_paths.append(p)
        return all_paths
#print "all_paths: %s" %(all_paths)

jr_ah = findAllPaths(movies, jr, ah)

print "jr_ah:  %s" %(jr_ah)
print "len(jr_ah): %s" %(len(jr_ah))
jr_dh = findAllPaths(movies, jr, dh)

print "jr_dh:  %s" %(jr_dh)
print "len(jr_dh): %s" %(len(jr_dh))


def findShortestPath(graph, start, end):
	all_paths = findAllPaths(graph, start, end)
	shortest = all_paths[0]
	for p in all_paths:
		if len(p) < len(shortest):
			shortest = p
	return shortest

print "findShortestPath(movies, jr, ah): " 

print findShortestPath(movies, jr, ah)

print "findShortestPath(movies, jr, dh): " 

print findShortestPath(movies, jr, dh)

# TODO: implement findAllPaths() to find all paths between two nodes
# allPaths = findAllPaths(movies, jr, ms)
# for path in allPaths:
#   print path




# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.