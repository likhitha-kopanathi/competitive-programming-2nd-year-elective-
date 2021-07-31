# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22
def isPrime(num):
    for i in range(2,num):  
       if (num % i) == 0:  
           return False
       else:  
           continue
    return True

def get_prime_factors(n):
    i = 2
    sum = 0
    prime_factors = []
    while i*i <= n:
        if n%i == 0:
            sum+=digitsum(i)
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    
    if n>1:
        prime_factors.append(n)
        sum+=digitsum(n)
    return sum

def digitsum(n):
    sum = 0
    while (n > 0):
        sum += (n % 10)
        n = int(n/10)
    return sum        
          
 #Function to check whether a number is a Smith Number or not      
def smith(n):
    if(isPrime(n)):
        return False
    if(digitsum(n) == get_prime_factors(n)):
        return True
    return False



def fun_nth_smithnumber(n):
    f = 0
    g = 0
    while(f<=n):
        g+=1
        if(smith(g)):
            f+=1
    return g