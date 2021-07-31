# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).
def pronic(n):
	y = 0
	while (y <= n) :
		if (n == y * (y + 1)):
			return True
		y+=1
	return False
	
def nthpronicnumber(n):
	# Your code goes here
	f = 1
	g = 0
	while(f<=n):
		g+=1
		if(pronic(g)):
			f+=1
	return g