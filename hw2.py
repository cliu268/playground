import math

# # Q1
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

# Q2
def isPrime(n):
    if n < 2: # 0 and 1
        return(False)
    elif n < 4: # 2 and 3
        return(True)
    else:
        x = 2
        while x < n:
            if n % x == 0:
                return(False)
            x+=1
        return(True)

def isCircularPrime(n):
    x = 1
    input = n
    while n % pow(10, x) < n:
        x+=1
    while isPrime(n):  
        n = 10 * (n % pow(10, x-1)) + (n // pow(10, x-1))
        if n == input:
            return(True)
    return(False)

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
print(nthCircularPrime(35))
print(isCircularPrime(197))

# def nthPalindromicPrime(n):
#     return