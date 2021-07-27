# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	# your code goes here
	if len(a)==0:
		return None
	elif((len(a))%2 == 0):
		mid1 = a[len(a)//2]
		mid2 = a[(len(a)//2)-1]
		return (mid1 + mid2)/2
	else:
		return a[len(a)//2]