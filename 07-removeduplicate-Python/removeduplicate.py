# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
	# Your code goes here
	newtext = ''
	for i in text:
		if i not in newtext:
			newtext+= str(i)
		else:
			continue
	return newtext