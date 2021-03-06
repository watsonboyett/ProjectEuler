#
# Problem: 002
#
# Question:
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
#
# Answer: 4613732

limit = 4000000
np = 1
n = 1
s = 0
while (n < limit):
	#print n
	if n % 2 == 0:
		s = s + n
	n = n + np
	np = n - np
	
ans = s
print ans