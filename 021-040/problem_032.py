#
# Problem: 032
# Question: 
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, 
# containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written 
# as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
#
# Answer: 45228


N = 9
Ns = (N/2.0)*(N+1)

prods = set()
ub = 9999

def num_len(num):
	nl = 0
	while num > 0:
		num = num / 10
		nl = nl + 1
	return nl
		
def num_digs(num):
	digs = []
	while num > 0:
		rem = num % 10
		digs.append(rem)
		num = num / 10
	return digs
	
for i in xrange(1,ub):
	ni = num_len(i)
	digs_i = num_digs(i)
	for j in xrange(i,ub):
		nj = num_len(j)

		if  (ni + nj != 5):
			continue

		ds = sum(digs_i)
		digs = set(digs_i)
		digs_j = num_digs(j)
		ds = ds + sum(digs_j)
		digs = digs.union(digs_j)
		
		p = i * j
		np = num_len(p)
		if (ni + nj + np != N):
			continue
		
		digs_p = num_digs(p)
		ds = ds + sum(digs_p)
		digs = digs.union(digs_p)
		if (len(digs) == N and ds == Ns):
			prods.add(p)
			print "{0} x {1} = {2}".format(i, j, p)
			
ans = sum(prods)
print ans
	