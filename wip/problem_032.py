
ub = 987654321;
pan = "123456789"

def get_prods():
	prods = set()
	return prods
	
if __name__ == "__main__":
	#prods = get_prods()
	prods = set()

	for i in xrange(1,ub):
		str_i = str(i)
		for j in xrange(lb,ub):
			if  (i > 100000 and j > 100000):
				continue
				
			p = i * j
			numstr = str_i + str(j) + str(p)
			if (len(numstr) < 9):
				continue
			numstr = "".join(sorted(numstr))
			if (numstr == pan):
				prods.add(p)
				
	ans = sum(prods)
	print "ans: {0}".format(ans)
	