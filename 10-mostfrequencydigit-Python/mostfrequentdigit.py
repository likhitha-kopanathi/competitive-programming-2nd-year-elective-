# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def digitcount(n, d):
	count = 0
	while(n > 0):
		if(n%10 == d):
			count = count + 1
		n = n //10
	return count
def mostfrequentdigit(n):
	digit = 0
	freq = 0
	for d in range(0 , 10):
		count = digitcount(n , d)
		if(count > freq):
			freq = count
			digit = d			
	return digit
