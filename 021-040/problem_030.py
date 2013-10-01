#
# Problem: 030
# Question: 
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
#
# Answer: 443839


D = 5

terms = set()
digits = [0]*(D+1)
keep_alive = True
while (keep_alive):
	s = 0
	n = 0
	for i in xrange(len(digits)):
		s = s + pow(digits[i], D)
		n = n + digits[i] * pow(10,i)
		
	if (n == s):
		terms.add(n)
	
	digits[0] = digits[0] + 1
	for i in xrange(len(digits)):
		if (digits[i] > 9):
			if (i == len(digits)-1):
				keep_alive = False
				digits[i] = -1
				break
			else:
				digits[i+1] = digits[i+1] + 1
				digits[i] = 0
			
	
#print terms
ans = sum(terms) - 1
print ans