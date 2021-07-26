def vowelcount(s):
    count = 0
    for c in s:
        if(c in 'aeiouAEIOU'):
            count+=1
    return count