#
# Problem: 033
# Question: 
#
# Answer: 


def get_digits(n):
	digs = []
	while (n > 0):
		d = n % 10
		digs.append(d)
		n = n / 10
	return digs

fracs_quot = []
fracs_num = []
fracs_den = []
for num in xrange(1,9):
	for den in xrange(num+1,9):
		f = float(num) / float(den)
		fracs_num.append(num)
		fracs_den.append(den)
		fracs_quot.append(f)
		
for num in xrange(10,99):
	if (num % 10 == 0):
		continue
	num_digs = get_digits(num)
	
	for den in xrange(num+1,99):
		if (num % 10 == 0):
			continue
		den_digs = get_digits(den)
		
		if (len(set(num_digs).intersection(den_digs)) > 0):		
			f = float(num) / float(den)
			if (f in fracs_quot):
				fracs_quot.index(f)
				print "{0} / {1} = {2}".format(num, den, f)