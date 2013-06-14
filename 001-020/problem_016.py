#
# Problem: 016
# Question: 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 			What is the sum of the digits of the number 21000?
#
# Answer: 1366

import math

N = 1000
num = int(math.pow(2,N))
str = str(num)

n = 0
for s in str:
	n = n + int(s)
	
ans = n
print ans

