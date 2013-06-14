
import math
from operator import mul

# use Sieve of Eratosthenes to build boolean list of prime
# numbers less than N
def sieve(n):
	lim = int(n)
	is_prime = [True] * lim
	is_prime[0] = False
	is_prime[1] = False
	for i in xrange(2, int(math.sqrt(lim))):
		if is_prime[i]:
			for j in xrange(int(math.pow(i,2)), lim, i):
				is_prime[j] = False
	
	primes = [i for i in xrange(lim) if is_prime[i]]
	return primes
	
# find all prime factors of N
def factor(n):
	primes = sieve(n)
	
	facts = []
	while n > 1:
		d = [x for x in primes if (n % x == 0)]
		prod = reduce(mul, d)
		n = n / prod
		facts.extend(d)
		
	facts.sort()
	return facts
	
def factors(n, primes):
	facts = []
	while n > 1:
		d = [x for x in primes if (n % x == 0)]
		prod = reduce(mul, d)
		n = n / prod
		facts.extend(d)
		
	facts.sort()
	return facts
	
	
	
if __name__ == "__main__":
	print factors(630)