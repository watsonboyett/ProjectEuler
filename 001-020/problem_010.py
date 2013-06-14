#
# Problem: 10
# Question: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 			Find the sum of all the primes below two million.
#
# Answer: 142913828922

# Sieve of Eratosthenes
lim = int(2e6)
marked = [False] * lim
value = 3
s = 2
while value < lim:
    if not marked[value]:
        s = s + value
        i = value
        while i < lim:
            marked[i] = True
            i = i + value
    value = value + 2
print s