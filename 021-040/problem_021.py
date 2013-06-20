#
# Problem: 021
#
# Question:
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.
#
# Answer: 31626


# setup import path to 'utils' folder
import os, sys
file_dir = os.path.dirname(sys.argv[0])
lib_path = os.path.abspath(os.path.join(file_dir,'..','utils'))
sys.path.append(lib_path)

import PrimeUtils


amic_UB = 10000
amic_nums = []
primes = PrimeUtils.primes(amic_UB*2)
for n in range(4, amic_UB):
	b = PrimeUtils.proper_divs_sum(n, primes)
	if b <= 1:
		continue
	a = PrimeUtils.proper_divs_sum(b, primes)
	
	if n == a and b != a:
		amic_nums.append(n)

amic_sum = sum(amic_nums)
ans = amic_sum
print ans


