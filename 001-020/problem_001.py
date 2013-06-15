#
# Problem: 001
# 
# Question: 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
#
# Answer: 233168


limit = 1000

# all multiples of 3
mult3 = set()
m = 3
while (m < limit):
	mult3.add(m)
	m = m + 3
print mult3

# all multiples of 5
mult5 = set()
m = 5
while (m < limit):
	mult5.add(m)
	m = m + 5
print mult5
	
# union of the sets
mults = mult3 | mult5
ans = sum(mults)
print ans