# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def prime(n):
	if n<2:
		return False
	for i in range(2, n):
		if(n%i == 0):
			return False
		return True

def Happynum(n):
	sum = 0
	while(n!=0):
		sum += (n%10)**2
		n//=10
	if sum == 1:
		return True
	elif sum<10:
		return False
	else:
		return Happynum(sum)

def happyprime(n):
	if(prime(n)==True and Happynum(n)==True):
		return True
	return False

def fun_nth_happy_prime(n):
	f = 0
	g = 0
	while(f<=abs(n)):
		g+=1
		if(happyprime(g)):
			f+=1
	return g

 