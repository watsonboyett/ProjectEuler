#
# Problem: 020
#
# Question:
# n! means n  (n  1)  ...  3  2  1
# For example, 10! = 10 + 9 + ... + 3 + 2 + 1 = 3628800, 
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!
#
# Answer: 648


N = 100

fact_sum = 1
for n in xrange(N, 0, -1):
	fact_sum = fact_sum * n
	
fact_str = str(fact_sum)

dig_sum = 0
for i in fact_str:
	dig_sum = dig_sum + int(i)
	
ans = dig_sum
print ans




