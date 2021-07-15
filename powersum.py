# powerSum(n, k) [15 pts]
# Write the function powerSum(n, k) that takes two 
# possibly-negative integers n and k and returns the 
# so-called power sum: Specify the time complexity based 
# on the solution that you have given. [Hint: This can be 
# solved in (n * log k)  or better.

#    1**k + 2**k + ... + n**k

# If n is negative, return 0. Similarly, if k is negative, 
# return 0.

def powerSum(n, k):
    if(n==0 or k==0):
        return 0
    sum = 0
    for i in range(1, n + 1, 1):
         
        sum += pow(i, k)
 
    # Return the sum
    return sum

# Write your own test cases here...

print (powerSum(3, 2))
print (powerSum(5, 3))
print (powerSum(0, 2))
print (powerSum(1, 0))