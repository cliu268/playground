import math
def longestDigitRun(n):
    n = abs(n)
    x = 1
    ans = n % pow(10, 1)
    count = 0
    final_ans = 0
    final_count = 0
    while True:
        current = (n % pow(10, x)) // pow(10, x-1)
        if ans == current:
            count += 1
        else:
            if count > final_count or (count == final_count and ans < final_ans):
                final_ans = ans
                final_count = count
            ans = current
            count = 1
        
        if n % pow(10, x) == n:
            if count > final_count or (count == final_count and ans < final_ans):
                return(ans)
            else:
                return(final_ans)
        x+=1
print(longestDigitRun(117773732))
print(longestDigitRun(-677886))
print(longestDigitRun(8888665544333321))

def nthCircularPrime(n):
    i = 0
    ans = 0
    while True:
        #write a function to check if the number is a circular prime
        if isCircularPrime(ans):
            if i==n:
                return(ans)
            i+=1
        ans+=1

def nthPalindromicPrime(n):