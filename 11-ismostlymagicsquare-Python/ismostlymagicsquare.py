# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.
def sumofrow(a):
	rowsum = 0
	for i in range(len(a)):
		rowsum+=a[0][i]
	for i in range(len(a)):
		val = 0
		for j in range(len(a)):
			val+=a[i][j]
		if val == rowsum:
			return True

def sumofcol(a):
	colsum = 0
	for i in range(len(a)):
		colsum+=a[i][0]
	for i in range(len(a)):
		val = 0
		for j in range(len(a)):
			val+=a[i][j]
		if val == colsum:
			return True

def sumofdiagonals(a):
	d1 = 0
	d2 = 0
	for i in range(len(a)):
		d1+=a[i][1]
		d2+=a[len(a)-i-1][len(a)-i-1]
	if d1==d2:
		return True
	else:
		return False


def ismostlymagicsquare(a):
	if(sumofrow(a)==True and sumofcol(a)==True and sumofdiagonals(a)==True):
		return True
	return False