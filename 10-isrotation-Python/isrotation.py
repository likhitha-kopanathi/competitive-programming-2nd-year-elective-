# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.


def isrotation(x, y):
	# Your code goes here
	x=str(x)
	y=str(y)
	if(len(x)!=len(y)):
		return False
	for i in range(len(x)):
		if x[i:len(x)]+x[0:i] == y : 
			return True
		ans = ''.join(reversed(x[i:len(x)])) + ''.join(reversed(x[0:i]))
		if ans==y:
			return True
	
	return False