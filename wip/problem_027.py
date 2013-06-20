#
# Problem: 027
#
# Question: 
# Euler discovered the remarkable quadratic formula: n^2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
# However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
# The incredible formula  n^2 + 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. 
# The product of the coefficients, 79 and 1601, is 126479.
# Considering quadratics of the form: n^2 + an + b, where |a| < 1000 and |b| < 1000
# where |n| is the modulus/absolute value of n (e.g. |11| = 11 and |-4| = 4)
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
#
# Answer: -59231


# setup import path to 'utils' folder
import os, sys
file_dir = os.path.dirname(sys.argv[0])
lib_path = os.path.abspath(os.path.join(file_dir,'..','utils'))
sys.path.append(lib_path)

import PrimeUtils
import numpy as np

N = 10000
primes = PrimeUtils.primes(N)

K = 8
pows = [pow(k, 2) for k in range(0,K)]

a_UB = 40
b_UB = 40
coeffs = np.zeros((2*a_UB, 2*b_UB))
for a in xrange(a_UB):
	for b in xrange(b_UB):
		for n in xrange(K):
			c1 = pows[n]
			c2 = a*n
			
			c = c1 + c2 + b
			if c in primes:
				coeffs[2*a][2*b] += 1
		
			c = c1 + c2 - b
			if c in primes:
				coeffs[2*a][b] += 1
		
			c = c1 - c2 + b
			if c in primes:
				coeffs[a][2*b] += 1
				
			c = c1 - c2 - b
			if c in primes:
				coeffs[a][b] += 1
		
ix = np.argmax(coeffs, 0)
iy = np.argmax(coeffs[ix], 0)


