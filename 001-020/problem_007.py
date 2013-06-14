#
# Problem: 7
# Question: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#			What is the 10 001st prime number?
#
# Answer: 104743

N = 10001
primes = [2,3]
i = primes[-1]
while len(primes) < N:
	i = i + 2
	is_prime = True
	for p in primes:
		if i % p == 0:
			is_prime = False
			break
	if is_prime:
		primes.append(i)

ans = primes[N-1]
print ans
