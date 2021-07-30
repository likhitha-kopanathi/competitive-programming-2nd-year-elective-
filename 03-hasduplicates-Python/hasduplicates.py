# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	# Your code goes here
	
	ele=[]
	c=0
	for row in range(len(L)):
		for col in range(len(L[0])):
			if(L[row][col] not in L):
				ele.append(L[row][col])
				c=c+1
	ele=set(ele)
	l=len(ele)
	if(l==c):
		return False
	else:
		return True
