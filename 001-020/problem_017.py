#
# Problem: 017
# Question: If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#			If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#			NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
#			115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
#
# Answer: 21124

import math

ones_strs = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
teens_strs = {0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen', 6: 'sixteen', 7: 'seventeen', 8: 'eighteen', 9: 'nineteen'}
tens_strs = {2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
hund_str = 'hundred'
thou_str = 'thousand'

N_lb = 1
N_ub = 1000

all_strs = ''
strs_list = []
for num in xrange(N_lb, N_ub+1):
	# determine digit for each place
	num_str = str(num)
	place_nums = [int(s) for s in num_str]
	
	# concatenate substrings
	cur_str = ''
	pn = len(place_nums)
	is_teen = False
	for p in range(pn):
		i = pn - p
		n = place_nums[p]
		has_more = sum(place_nums[p+1:]) > 0
		if n > 0 or is_teen:
			if i == 4:
				tmp_str = '{0} {1}'.format(ones_strs[n], thou_str)
			if i == 3:
				tmp_str = '{0} {1}'.format(ones_strs[n], hund_str)
			if i == 2:
				if n > 1:
					tmp_str = '{0}'.format(tens_strs[n])
				else:
					is_teen = True
			if i == 1:
				if is_teen:
					tmp_str = '{0}'.format(teens_strs[n])
				else:
					tmp_str = '{0}'.format(ones_strs[n])
			
			if not (i == 2 and is_teen):
				if len(cur_str) > 0 and len(place_nums) > 2 and not has_more:
					cur_str = '{0} and {1}'.format(cur_str, tmp_str)
				else:
					cur_str = '{0} {1}'.format(cur_str, tmp_str)
				
	
	cur_str = cur_str.strip()
	print cur_str
	all_strs = '{0} {1}'.format(all_strs, cur_str)
	strs_list.append(cur_str)
	
comp_str = all_strs.replace(' ', '')
ans = len(comp_str)
print ans

