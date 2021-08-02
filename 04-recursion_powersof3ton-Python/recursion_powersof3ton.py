# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def recursion_powersof3ton(n, nextPower=0, newL = None):
	# Your code goes here
	if newL == None:
		newL = []
	if nextPower == 0:
		newL.append(1)
	if n < 1:
		return None
	else:
		#every time we move on our power increments by 1
		nextPower += 1
		nextNumber = 3**nextPower
		#if next number is greater than our number then we stop looping
		if(nextNumber > n):
			return newL
		newL.append(nextNumber)
		return recursion_powersof3ton(n, nextPower, newL)
