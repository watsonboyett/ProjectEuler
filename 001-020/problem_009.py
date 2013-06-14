#
# Problem: 9
# Question: A Pythagorean triplet is a set of three natural numbers, a  b  c, for which, a^2 + b^2 = c^2
#			For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#			There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#			Find the product abc.
#
# Answer: 31875000

import math

con = math.pow(1000,2)
for a in xrange(1,1000):
	b = (con - 2000.*a) / (2000. - 2.*a)
	if b > 0 and b % 1 == 0:
		c = math.sqrt( math.pow(a,2) + math.pow(b,2) )
		break
		
print "a: {0}, b: {1}, c: {2}".format(a, b, c)

prod = a * b * c
print prod