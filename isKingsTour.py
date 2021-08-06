# Background:  in Chess, a King can move from any square to
# any adjacent square.  A King’s Tour is a series of legal King
# moves so that every square is visited exactly once. 
# We can represent a Kings Tour in a 2d list where the 
# numbers represent the order the squares are visited, going 
# from 1 to N2.  For example, consider these 2d lists:

#    [ [  3, 2, 1 ],    	[ [  1, 2, 3 ],  	[ [ 3, 2, 1 ],
#  	[  6, 4, 9 ],      	[  7, 4, 8 ],    	[ 6, 4, 0 ],
#  	[  5, 7, 8 ] ]     	[  6, 5, 9 ] ]   	[ 5, 7, 8 ] ]

# The first is a legal Kings Tour but the second is not, 
# because there is no way to legally move from the 7 to the 8, 
# and the third is not, because it contains a 0 which is out
#  of range.  With this in mind, write the function 
# isKingsTour(board) that takes a 2d list of integers, 
# which you may assume is NxN for some N>0, and 
# returns True if it represents a legal Kings Tour 
# and False otherwise.

def getRowCol(L, i):
    for row in range(len(L)):
        for col in range(len(L[0])):
            if (L[row][col] == i):
                return [row,col]
    return (-1,-1)

def isValid (r1, c1, r2, c2):
    if ((abs(r1 - r2) <= 1) and (abs(c1 - c2) <= 1)):
        return True
    return False

def isKingsTour(board):
    # Your code goes here...
    l1 = len(board)
    l2 = len(board[0])
    for row in range(l1):
        for col in range(l2):
            if (board[row][col] == 0):
                return False
    i = 1
    while (i < (l1 * l2)) :
        r1, c1 = getRowCol(board, i)
        r2, c2 = getRowCol(board, i + 1)
        if (r1 == -1 or c1 == -1):
            return False
        i = i + 1
        if (isValid(r1, c1, r2, c2) == False):
            return False
    return True

a = [ [  3, 2, 1 ], [  6, 4, 9 ], [  5, 7, 8 ] ]
assert(isKingsTour(a) == True)
a = [ [  2, 8, 9 ], [  3, 1, 7 ], [  4, 5, 6 ] ]
assert(isKingsTour(a) == True)
a = [ [  7, 5, 4 ],
          [  6, 8, 3 ],
          [  1, 2, 9 ] ]
assert(isKingsTour(a) == True)
a = [ [  7, 5, 4 ],
          [  6, 8, 3 ],
          [  1, 2, 1 ] ]
assert(isKingsTour(a) == False)
a = [ [  3, 2, 9 ],
          [  6, 4, 1 ],
          [  5, 7, 8 ] ]
assert(isKingsTour(a) == False)
a = [ [  3, 2, 1 ],
          [  6, 4, 0 ],
          [  5, 7, 8 ] ]
assert(isKingsTour(a) == False)
a = [ [  1, 2, 3 ],
          [  7, 4, 8 ],
          [  6, 5, 9 ] ]
assert(isKingsTour(a) == False)
a = [ [ 3, 2, 1 ],
          [ 6, 4, 0 ],
          [ 5, 7, 8 ] ]
assert(isKingsTour(a) == False)
print("Passed!")