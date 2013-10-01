
ways = set()

def subset_sum_recursive(numbers, target, partial):
	numstr = str(partial)
	if (numstr in ways):
		return
	
	# check if the partial sum is equal to target sum
	s = sum(partial)
	if s == target: 
		print "{0} = {1}".format(numstr, target)
		ways.add(numstr)
	if s >= target:
		return
		
	for i in range(len(numbers)):
		n = numbers[i]
		remaining = numbers
		partialnew = partial + [n]
		partialnew.sort()
		subset_sum_recursive(remaining, target, partialnew)

def subset_sum(numbers, target):
	#we need an intermediate function to start the recursion.
	#the recursion start with an empty list as partial solution.
	subset_sum_recursive(numbers, target, list())

if __name__ == "__main__":
	#subset_sum([1,2,5,10,20,50,100], 200)
	subset_sum([1,2,5,10], 10)
	
	ans = len(ways)
	print "ans: {0}".format(ans)
	