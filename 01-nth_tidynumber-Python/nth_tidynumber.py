# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def tidy(n):
    x = 10
    while(n):
        rem = n%10
        if(rem>x):
            return False
        elif(x>=rem):
            x = rem
        n//=10
    return True

def fun_nth_tidynumber(n):
    f=0
    g=0
    while(f<=n):
        g+=1
        if(tidy(g)):
            f+=1
    return g