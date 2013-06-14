#
# Problem: 5
# Question: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#			What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
# Answer: 232792560

max = 20
nums = range(1, max+1)
ans = 0
while True:
	ans = ans + max
	is_even = True
	for j in nums:
		if (ans % j > 0):
			is_even = False
			break
	
	if is_even:
		break

print ans