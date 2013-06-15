#
# Problem: 022
#
# Question:
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, 
# multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, 
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938  53 = 49714.
# What is the total of all the name scores in the file?
#
# Answer: 871198282


names = []
with open(r'C:\Users\wboyett\Desktop\names.txt', 'r') as fid:
	for line in fid:
		nms = line.split(',')
		nms = [s.strip('"') for s in nms]
		names.extend(nms)

names.sort()

A = ord('A')-1
scores = []
for i in xrange(0,len(names)):
	name = names[i].upper()
	ords = [ord(s)-A for s in name]
	score = sum(ords) * (i+1)
	scores.append(score)
	
ans = sum(scores)
print ans

