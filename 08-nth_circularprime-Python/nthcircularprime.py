# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).


def prime(n):
	if n<2:
		return False
	for i in range(2,n):
		if(n%i==0):
			return False
	return True

def circularprime(n):
	l = len(str(n))
	count = l
	while count>0:
		rem=n%10
		n//=10
		n=rem*(10**(l-1))+n
		if(prime(n)):
			count-=1
		else:
			return False
	return True


def nthcircularprime(n):
	# Your code goes here
	f=1
	g=0
	while(f<=n):
		g+=1
		if(circularprime(g)):
			f+=1
	return g