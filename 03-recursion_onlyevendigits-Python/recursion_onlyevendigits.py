# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def fun_recursion_onlyevendigits(l, newl = None, count = 0):
	if newl == None:
		newl = []
	if l == [] and count == 0:
		return l
	if len(l) == 0:
		return newl
	else:
		count += 1
		#we will call our helper fuction on every number to convert them into
		#numbers made of only even numbers
		newNumber = checkForEvens(l[0])
		newl.append(newNumber)
		return fun_recursion_onlyevendigits(l[1:], newl, count)
		
def checkForEvens(number, newNumber = 0, powerOf10 = 1):
	#base case checks if we have already loooped through the whole number
	firstDigitFromRight = number % 10
	if number <= 0:
		return newNumber
	else:
		#first we get the number from the very left
		if firstDigitFromRight % 2 == 0:
			#add the firstDigit to our newNumber
			newNumber += firstDigitFromRight * powerOf10
			number //= 10
			#strip down the number by 10
			powerOf10 *= 10
			return checkForEvens(number, newNumber, powerOf10)
		else:
			number //= 10
			return checkForEvens(number, newNumber, powerOf10)