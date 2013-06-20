#
# Problem: 026
#
# Question:
# A unit fraction contains 1 in the numerator. 
# The decimal representation of the unit fractions with denominators 2 to 10 are given:
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
# It can be seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
#
# Answer: 983
#
# Notes: could probably be solved by constructing a Suffix tree and searching for the longest subsequence

from decimal import *
import math
import time

digit_n = 2000
getcontext().prec = digit_n

dens = []
lens = []
poss = []
N = 1000
for den in range(1, N):
	frac = Decimal(1) / Decimal(den)
	frac_str = str(frac)
	den_str = frac_str[2:]
	den_len = len(den_str)
	
	len_max = 0
	pos_val = 0
	for sub_posi in range(0, (den_len/2)-1):
		sub_inc = True
		for sub_len in range(1, den_len/2):
			sub_str = den_str[sub_posi:sub_posi+sub_len]
			
			rep_n = (digit_n - sub_posi) / sub_len - 1
			for k in range(1, rep_n):
				cmp_ix = range(k*sub_len+sub_posi, (k+1)*sub_len+sub_posi)
				cmp_str = ''.join([den_str[ix] for ix in cmp_ix])
				
				#print "{0} {1} {2}".format(sub_str, cmp_str, k)
				#time.sleep(0.2)
				
				if sub_str == cmp_str:
					if sub_len > len_max:
						len_max = sub_len
						pos_val = sub_posi
					if k == (rep_n - 1):
						sub_inc = False
				else:
					break
			
			if not sub_inc:
				break
					
	dens.append(den)
	lens.append(len_max)
	poss.append(pos_val)
			
den_max = max(lens)
den_ind = lens.index(den_max)
den_val = dens[den_ind]

ans = den_val
print ans
			