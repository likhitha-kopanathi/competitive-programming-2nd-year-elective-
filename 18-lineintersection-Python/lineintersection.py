# lineintersection(m1, b1, m2, b2)[5pts]
# Write the function lineintersection(m1, b1, m2, b2) that takes four int or float values representing the 2 lines:
#     y = m1*x + b1
#     y = m2*x + b2
# This function returns the x value of the point of intersection of the two lines. If the lines are parallel, or identical, the function should return None.

def lineintersection(m1, b1, m2, b2):
	# your code goes here
	if(b1==b2 or m1==m2):
		return None
	elif(ismultiple(m1,m2) or ismultiple(m2,m1)):
		return None
	else:
		return (b2-b1)/(m1-m2)
def ismultiple(m,n):
	if m%n == 0:
		return True
	return False

