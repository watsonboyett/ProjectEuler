#
# Problem: 023
#
# Question: 
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot 
# be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#
# Answer: 4179871


# setup import path to 'utils' folder
import os, sys
file_dir = os.path.dirname(sys.argv[0])
lib_path = os.path.abspath(os.path.join(file_dir,'..','utils'))
sys.path.append(lib_path)

import PrimeUtils
import itertools

# find all abundant numbers
abund_UB = 28124
primes = PrimeUtils.primes(abund_UB)
abund_nums = []
for n in xrange(12, abund_UB):
	spd = PrimeUtils.proper_divs_sum(n, primes)
	if spd > n:
		abund_nums.append(n)

# permute all combinations of two abundant sums
non_abund_vals = range(abund_UB)
for an1 in abund_nums:
	for an2 in abund_nums:
		ix = an1 + an2
		if ix >= abund_UB:
			continue
		non_abund_vals[ix] = 0

non_abund_sum = sum(non_abund_vals)
ans = non_abund_sum
print ans

