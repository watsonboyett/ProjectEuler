
import math
from operator import mul
import itertools

# use Sieve of Eratosthenes to build boolean list of prime
# numbers less than N
def primes(N):
	lim = int(N) + 1
	is_prime = [True] * lim
	is_prime[0] = False
	is_prime[1] = False
	for i in xrange(2, int(math.sqrt(lim))+1):
		if is_prime[i]:
			for j in xrange(int(math.pow(i,2)), lim, i):
				is_prime[j] = False
	
	primes = [i for i in xrange(lim) if is_prime[i]]
	return primes

# find all prime factors of N
def factor_primes(N):
	return factor_list(N, primes(N))

# find all prime factors of 'N' using 'primes' list as
# initialized list all possible primes
def factor_list(N, primes):
	facts = []
	while N > 1:
		d = [x for x in primes if (N % x == 0)]
		prod = reduce(mul, d)
		N = N / prod
		facts.extend(d)
		
	facts.sort()
	return facts
	
def proper_divs(N):
	return proper_divs_list(N, primes(N))
	
def proper_divs_list(N, primes):
	# this function is not correct
	exit()
	
	facts = factor_list(N, primes)
	
	# algorithm: http://en.wikipedia.org/wiki/Divisor_function
	pn = max(facts) + 1
	p = [0] * pn
	for f in facts:
		p[f] += 1
	
	divs = []
	x = 1
	for i in range(len(p)):
		if p[i] < 1:
			continue
		for j in range(1, p[i]+1):
			d = pow(i, j*x)
			divs.append(d)
		
	return divs

# calculate the sum of the i-th powers of the positive divisors of 'N'
# divisors list provided through 'primes' argument
def proper_divs_sum(N, primes):
	facts = factor_list(N, primes)
	
	# algorithm: http://en.wikipedia.org/wiki/Divisor_function
	pn = max(facts) + 1
	p = [0] * pn
	for f in facts:
		p[f] += 1
	
	x = 1
	prd = 1
	for i in range(len(p)):
		if p[i] < 1:
			continue
		sm = 1
		for j in range(1, p[i]+1):
			sm = sm + pow(i, j*x)
		prd = prd * sm
		
	return prd - N
	
if __name__ == "__main__":
	N = 2
	print proper_divs_sum(N, primes(N))
	
	
	