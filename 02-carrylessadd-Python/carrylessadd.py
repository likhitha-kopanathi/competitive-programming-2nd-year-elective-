# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.



def digitCount(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n = n // 10
        count = count + 1
    return count

def fun_carrylessadd(x, y):
	max_digit = max(digitCount(x), digitCount(y))
	output = 0
	for i in range(max_digit):
		last_1 = x // (10**i) % 10
		last_2 = y // (10**i) % 10
		output += (last_1 + last_2) % 10 * (10 ** i)
	return output

