# bonusPlayThreeDiceYahtzee(dice) [5pts]
# In this exercise, we will write a simplified form of the dice game Yahtzee. In this version, the 
# goal is to get 3 matching dice, and if you can't do that, then you hope to at least get 2 
# matching dice. The game is played like so:
# Roll 3 dice.
# If you do not have 3 matching dice:
# If you have 2 matching dice (a pair), keep the pair and roll one die to replace the third die.
# Otherwise, if you have no matching dice, keep the highest die and roll two dice to replace the 
# other two dice.
# Repeat step 2 one more time.
# Finally, compute your score like so:
# If you have 3 matching dice, your score is 20 + the sum of the matching dice.
# So if you have 4-4-4, your score is 20+4+4+4, or 32.
# If you only have 2 matching dice, your score is 10 + the sum of the matching dice.
# So if you have 4-4-3, your score is 10+4+4, or 18.
# If you have no matching dice, your score is the highest die.
# So if you have 4-3-2, your score is just 4.
# Our goal is to write some Python code that plays this game. It's a large task, so we will use 
# top-down design and break it up into smaller, more manageable pieces. So we'll first write some 
# helper functions that do part of the work, and then those helper functions will make our final 
# function much easier to write. 
# Also note: we will represent a hand of 3 dice as a single 3-digit integer. So the hand 4-3-2 will 
# be represented by the integer 432. With that, let's start writing some code. Be sure to write 
# your functions in the same order as given here, since later functions will make use of earlier 
# ones!
# we've made it to the last function: bonusPlayThreeDiceYahtzee(dice), the function that actually earns 
# the 2.5 bonus points! This function takes one value, the dice with all the rolls for a game of 3-Dice 
# Yahtzee. The function plays the game -- it does step1 and gets the first 3 dice (from the right), then it 
# does step2 twice (by calling playStep2, which you already wrote), and then it computes the score (by 
# calling score, which you already wrote). The function should return two values -- the resulting hand 
# and the score for that hand. For example:
# assert(bonusPlayThreeDiceYahtzee(2312413) == (432, 4))
# assert(bonusPlayThreeDiceYahtzee(2315413) == (532, 5))
# assert(bonusPlayThreeDiceYahtzee(2345413) == (443, 18))
# assert(bonusPlayThreeDiceYahtzee(2633413) == (633, 16))
# assert(bonusPlayThreeDiceYahtzee(2333413) == (333, 29))
# assert(bonusPlayThreeDiceYahtzee(2333555) == (555, 35))

def handtodice(hand):
	# your code goes here
	digit1 = hand//100
	digit2 = (hand%100)//10
	digit3 = hand%10
	return digit1, digit2, digit3
def dicetoorderedhand(a, b, c):
	# your code goes here
	largest = max(a,b,c)
	smallest = min(a,b,c)
	medium = a+b+c-largest-smallest
	return largest*(10**2) + medium*10 +smallest
def casenum(hand):
	digit1, digit2, digit3 = handtodice(hand)
	if digit1==digit2==digit3:
		return 3
	elif digit1!=digit2!=digit3:
		return 1
	else:
		return 2
def playstep2(hand, dice):
	# your code goes here
	case = casenum(hand)
	a,b,c = handtodice(hand)
	orderedHand = dicetoorderedhand(a,b,c)
	#case1
	if case == 3:
		return hand,dice
	#case2
	elif case == 2:
		num1,num2,num3 = handtodice(orderedHand)
		num4 = dice%10
		if num1 == num2:
			newHand = dicetoorderedhand(num1, num2, num4)
			return newHand, dice//10
		elif num1 == num3:
			newHand = dicetoorderedhand(num1,num3,num4)
			return newHand, dice//10
		else:
			newHand = dicetoorderedhand(num3, num2, num4)
			return newHand, dice//10
	#case3
	else:
		num1, num2, num3 = handtodice(orderedHand)
		nextrolls = dice%100
		n1, n2, n3 = handtodice(num1*100 + nextrolls)
		newHand = dicetoorderedhand(n1, n2, n3)
		return newHand, dice//100
def score(hand):
	rank = casenum(hand)
	num1, num2, num3 = handtodice(hand)
	if rank == 3:
		return 20+3*(hand//100)
	elif rank == 2:
		if num1==num2:
			return 10+2*num1
		elif num1==num3:
			return 10+2*num3
		else:
			return 10+2*num2
	else: return max(num1, num2, num3)


def bonusplaythreediceyahtzee(dice):
	# Your code goes here
	d = dice//1000
	hand = dice%1000
	hand1, d1 = playstep2(hand, d)
	hand2, d2 = playstep2(hand1, d1)
	scr = score(hand2)
	return hand2, scr
