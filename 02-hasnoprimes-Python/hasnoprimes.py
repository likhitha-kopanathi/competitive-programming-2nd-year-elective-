# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def prime(n):
	if n<2:
		return False
	for i in range(2,n):
		if(n%i == 0):
			return False
	return True

def fun_hasnoprimes(l):
	for r in range(len(l)):
		for c in range(len(l[r])):
			if(prime(l[r][c])):
				return False
	return True


	return True

