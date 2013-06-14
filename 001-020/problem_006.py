#
# Problem: 6
# Question: The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
# 			The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 552 = 3025
# 			Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# 			Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#
# Answer: 25164150

import math

limit = 100
nums = xrange(1, limit+1)
# brute force!!
s1 = sum([math.pow(x, 2) for x in nums])
s2 = math.pow(sum([x for x in nums]), 2)
ans = s2 - s1
print ans
