


def subset_sum_recursive(numbers, target, partial):
    s = sum(partial)

    #check if the partial sum is equals to target
    if s == target: 
        print "sum(%s)=%s"%(partial,target)
    if s >= target:
        return # if we reach the number why bother to continue
        
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum_recursive(remaining, target, partial + [n]) 

def subset_sum(numbers, target):
    #we need an intermediate function to start the recursion.
    #the recursion start with an empty list as partial solution.
    subset_sum_recursive(numbers, target, list())

if __name__ == "__main__":
    #subset_sum([1,2,5,10,20,50,100], 201)
    subset_sum([3,9,8,4,5,7,10], 25)
    
    #Outputs:
    #sum([3, 8, 4])=15
    #sum([3, 5, 7])=15
    #sum([8, 7])=15
    #sum([5, 10])=15
    