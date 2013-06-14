
import math

def nchoosek(n, k):
	return math.factorial(n) / ( math.factorial(n - k) * math.factorial(k) )