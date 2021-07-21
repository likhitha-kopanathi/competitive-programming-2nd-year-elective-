# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def prime(n):
	if(n<2):
		return False
	for i in range(2,n):
		if(n%i==0):
			return False
	return True
def add(n):
	sum=0
	while(n>0):
		rem=n%10
		sum=sum+rem
		n=n//10
	return sum


def fun_nth_additive_prime(n):
	f=0
	g=0
	while(f<=n):
		g+=1
		if(prime(g) and prime(add(g))):
			f+=1
	return g