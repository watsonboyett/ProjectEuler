#
# Problem: 3
# Question: The prime factors of 13195 are 5, 7, 13 and 29.
# 			What is the largest prime factor of the number 600851475143?
#
# Answer: 6857

number = 600851475143
n = number
factors = []

primes = [2]
while (n > 1):
	# check for next smallest prime factor
	for p in primes:
		if n % p == 0:
			n = n / p
			factors.append(p)
	
	# use Sieve of Eratosthenes to find next prime
	i = primes[-1]
	prime_found = False
	while not prime_found:
		i = i + 1
		is_prime = True
		for p in primes:
			if i % p == 0:
				is_prime = False
				break
		if is_prime:
			primes.append(i)
			prime_found = True
		
print factors