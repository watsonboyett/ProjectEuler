#
# Problem: 025
#
# Question:
# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
# The 12th term, F12, is the first term to contain three digits.
# What is the first term in the Fibonacci sequence to contain 1000 digits?
#
# Answer: 4782

digit_n = 1000
N = pow(10, (digit_n-1))

cur = 1
prv = 1
i = 2
while True:
	tmp = cur
	cur = cur + prv
	prv = tmp
	i = i + 1
	if (cur / N >= 1):
		break
		
ans = i
print ans



