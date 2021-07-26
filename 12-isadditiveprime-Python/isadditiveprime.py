def prime(n):
    if(n<2):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

def add(n):
    sum = 0
    while(n>0):
        rem = n%10
        sum+=rem
        n//=10
    return sum

def isadditiveprime(n):
    if(prime(n) and prime(add(n))):
        return True
    return False