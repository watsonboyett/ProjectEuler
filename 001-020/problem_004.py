
# Problem: 04
# Question: A palindromic number reads the same both ways. 
# 			The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
# 			Find the largest palindrome made from the product of two 3-digit numbers.
#
# Answer: 906609

start = 999
stop = 100
cands = []

# exhaustive search
for i1 in xrange(start, stop, -1):
	for i2 in xrange(start, stop, -1):
		n = i1 * i2
		nr = int(str(n)[::-1])
		if n == nr:
			cands.append(n)

n = max(cands)	
print n