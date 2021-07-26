# Write the function fun_nth_palindromic_prime(n) that takes 
# a non-negative int n and returns the nth palindromic Prime, 
# which is a palidrome number such that 
# it is also a prime. 

# For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) 
# returns 2

def prime(n):
	if n<2:
		return False
	for i in range(2, n):
		if(n%i == 0):
			return False
	return True

def palidrome(n):
	n = str(n)
	if n[:] == n[::-1]:
		return True
	return False

def fun_nth_palindromic_prime(n):
	f = 0
	g = 0 
	while(f<=n):
		g+=1
		if(prime(g) and palidrome(g)):
			f+=1
	return g