#
# Problem: 018
# Question: Too long to include here...
#
# Answer: 1074

import matplotlib.pyplot as plt
import networkx as nx

tri1 = [ \
[75], \
[95,64], \
[17,47,82]]

tri = [ \
[75], \
[95,64], \
[17,47,82], \
[18,35,87,10], \
[20,4,82,47,65], \
[19,1,23,75,3,34], \
[88,2,77,73,7,63,67], \
[99,65,4,28,6,16,70,92], \
[41,41,26,56,83,40,80,70,33], \
[41,48,72,33,47,32,37,16,94,29], \
[53,71,44,65,25,43,91,52,97,51,14], \
[70,11,33,28,77,73,17,78,39,68,17,57], \
[91,71,52,38,17,14,91,43,58,50,27,29,48], \
[63,66,4,68,89,53,67,30,73,16,69,87,40,31], \
[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]


edgeMax = max([max(x) for x in tri])

G = nx.DiGraph()
for i in range(len(tri)):
	for j in range(len(tri[i])):
		s = "{0}.{1}".format(i, j)
		if (i < len(tri)-1):
			for k in [0,1]:
				t = "{0}.{1}".format(i+1, j+k)
				w = edgeMax - tri[i][j]
				G.add_edge(s,t, weight=w)
		else:
			t = "{0}.{1}".format(i+1, 0)
			w = edgeMax - tri[i][j]
			G.add_edge(s,t, weight=w)

s = "0.0"
t = "{0}.{1}".format(len(tri), 0)
path = nx.dijkstra_path(G, s, t)
#print path

ans = 0
for i in range(len(path)-1):
	e = G[path[i]][path[i+1]]
	v = edgeMax - e['weight']
	ans = ans + v
	
	#print "{0}->{1} : {2}".format(path[i], path[i+1], v)
	
print "ans: {0}".format(ans)