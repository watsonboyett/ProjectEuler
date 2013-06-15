#
# Problem: 067
#
# Question: 
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom in triangle.txt
#
# Answer: 7273



import matplotlib.pyplot as plt
import networkx as nx

tri = []

# load triangle numbers into list
filename = r'C:\Users\wboyett\Desktop\ProjectEuler\061-080\problem_067_triangle.txt'
with open(filename, 'r') as fid:
	for line in fid:
		line_strs = line.strip().split(' ')
		line_nums = [int(s) for s in line_strs]
		tri.append(line_nums)

		
# build a graph for easy traversal
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

