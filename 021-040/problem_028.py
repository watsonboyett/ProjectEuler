#
# Problem: 028
#
# Question:
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# [21] 22  23  24 [25]
#  20  [7]  8  [9] 10
#  19   6  [1]  2  11
#  18  [5]  4  [3] 12
# [17] 16  15  14 [13]
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
#
# Answer: 669171001


N = 1001
sqr_sum = 1
for sqr_i in range(3, N+1, 2):
	sqr = pow(sqr_i, 2)
	sqr_sub = [sqr-(i*(sqr_i-1)) for i in range(1,4)]
	sqr_sum = sqr_sum + sqr + sum(sqr_sub)

ans = sqr_sum
print ans

