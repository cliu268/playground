import math

# Q1
# longestDigitRun [standard, 15 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and 
# returns the digit that has the longest consecutive run, or the smallest such digit if there is a tie. 
# So, longestDigitRun(117773732) returns 7 (because there is a run of 3 consecutive 7's), as does 
# longestDigitRun(-677886).
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
# print(longestDigitRun(117773732))
# print(longestDigitRun(-677886))
# print(longestDigitRun(8888665544333321))

# Q2
# nthCircularPrime [standard, 15 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth Circular prime,
# which is a prime number that does not contain any 0's and such that all the numbers resulting from 
# rotating its digits are also prime. 
# The first Circular primes are 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... 
# To see why 197 is a Circular prime, note that 197 is prime, as is 971 (rotated left), as is 719 
# (rotated left again).
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
# print(nthCircularPrime(35))
# print(isCircularPrime(197))

# Q3
# nthPalindromicPrime [standard, 15 pts]
# Write the function nthPalindromicPrime(n), where a palindromic prime is a number that is both prime 
# and palindromic (same forwards as backwards). See here for details. 
# So nthPalindromicPrime(0) returns 2, and nthPalindromicPrime(10) returns 313.
def currentDigit(n, x):
    return((n % pow(10, x)) // pow(10, x-1))

def isPalindromic(n):
    if n < 10:
        return(True)
    else:
        # count number of digits in n
        x = 1
        y = 1
        while n % pow(10, x) < n:
            x+=1      
        while y < x:
            # x will be the left most digit and y be the right most digit
            if currentDigit(n, x) != currentDigit(n, y):
                return(False)            
            x-=1
            y+=1
        return(True)

def nthPalindromicPrime(n):
    i = 0
    ans = 0
    while True:
        #write a function to check if the number is a palindromic prime
        if isPrime(ans) and isPalindromic(ans):
            if i==n:
                return(ans)
            i+=1
        ans+=1
    return(ans)
# print(nthPalindromicPrime(0))
# print(nthPalindromicPrime(10))
# print(nthPalindromicPrime(19))

# Q4
# carrylessAdd [required, 15 pts]
# First, you may wish to read the first page (page 44) from here about Carryless Arithmetic. 
# Or, just understand that carryless addition is what it sounds like -- regular addition, only with 
# the carry from each column ignored. So, for example, if we carryless-ly add 8+7, we get 5 (ignore 
# the carry). And if we add 18+27, we get 35 (still ignore the carry). With this in mind, write the 
# function carrylessAdd(x, y) that takes two non-negative integers x and y and returns their carryless 
# sum. As the paper demonstrates, carrylessAdd(785, 376) returns 51.
def numberOfDigits(n):
    x = 1
    while n % pow(10, x) < n:
            x+=1    
    return(x)

def carrylessAdd(x, y):
    xcount = numberOfDigits(x)
    ycount = numberOfDigits(y)
    if xcount > ycount:
        return((x // pow(10, ycount)) * pow(10, ycount) + carrylessAdd(x % pow(10, ycount), y))
    elif xcount < ycount:
        return((y // pow(10, xcount)) * pow(10, xcount) + carrylessAdd(y % pow(10, xcount), x))
    else:
        i = 1
        ans = 0
        while i <= xcount:
            ans += (currentDigit(x, i) + currentDigit(y, i)) % 10 * pow(10, i-1)
            i+=1
        return(ans)
# print(carrylessAdd(22785, 899376))

# Q5
# findZeroWithBisection [required, 15 pts]
# Write the function findZeroWithBisection(f, x0, x1, epsilon) as described below:
# In mathematics, one way to numerically (as opposed to algebraically) find a zero of a function f(x) 
# is to use what amounts to binary search.  To start, we need to know two values, x0 and x1, with x0<x1, 
# where f(x0) and f(x1) have different signs (so one is positive and the other is negative).  
# Hence, by the Intermediate Value Theorem, we know there is some value x in the range [x0,x1] such 
# that f(x)=0.  It is that value of x that we are seeking.  How?  First, try the value xmid, which is 
# the midpoint between x0 and x1.  If f(xmid) is exactly 0, we are done!  Otherwise, we can divide our 
# range in half as such:  if f(xmid) and f(x0) are the same sign, use the range [xmid, x1].  
# Otherwise, f(xmid) and f(x1) must share the same sign, so use the range [x0, xmid].  We repeat this 
# in a loop until x0 and x1 are within some suitably small epsilon.
# 
# With this in mind, write the function findZeroWithBisection that takes a function f, a float x0, 
# a float x1, and a float epsilon, and returns an approximate value x in [x0,x1] where f(x) is 
# approximately zero.  
# Your function should stop when x0 and x1 are within epsilon, and at that time should return the 
# midpoint of that range.  Note that if it is not true that exactly one of f(x0) and f(x1) is negative, 
# your function should return the Python value None, signifying that the bisection method cannot be used 
# on the given range.
def findZeroWithBisection(f, x0, x1, epsilon):
    epsilon = abs(epsilon)
    xmid = (x0 + x1) / 2
    if x0 >= x1:
        return(None)
    elif f(x0) * f(x1) >= 0:
        return(None)
    elif x1 - x0 < epsilon:
        return(xmid)
    elif f(xmid) == 0:
        return(xmid)
    elif f(xmid) * f(x0) > 0: # f(xmid) and f(x0) are the same sign
        return(findZeroWithBisection(f, xmid, x1, epsilon))
    else:
        return(findZeroWithBisection(f, x0, xmid, epsilon))
# print("use bisection to approximate sqrt(2):")
# def f1(x): return x*x - 2 # root at x=sqrt(2)
# x = findZeroWithBisection(f1, 0, 2, 0.000000001)
# print(" x =", x)                # prints  x = 1.41421356192
# print(" check: x**2 =", (x*x))  # prints  check: x**2 = 1.99999999871 (really close!)

# print("use bisection to approximate phi (the golden ratio):")
# def f2(x): return x**2 - (x + 1) # root at x=phi
# x = findZeroWithBisection(f2, 0, 2, 0.000000001)
# print(" x =", x)                  # prints x = 1.61803398887
# phi = (1 + 5**0.5)/2              # the actual value (to within Python's floating point accuracy)
# print(" check: x/phi =", (x/phi)) # prints check: check: x/phi = 1.00000000007 (nice!)

# print("use bisection to approximate x where x**5 == 2**x")
# def f3(x): return x**5 - 2**x # f(1)<0, f(2)>0
# x = findZeroWithBisection(f3, 1, 2, 0.000000001)
# print(" x =", x)                              # prints x = 1.17727855081
# print(" check: x**5 - 2**x =", (x**5 - 2**x)) # prints check: x**5 - 2**x = 3.63570817896e-09 (great!)

# Q6
# nthKaprekarNumber [required, 15 pts]
# Background: a Kaprekar number is a positive integer, the representation of whose square can be split 
# into two possibly-different-length parts (where the right part is not zero) that add up to the 
# original number again. For instance, 45 is a Kaprekar number, because 45**2 = 2025 and 20+25 = 45. 
# The first several Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,...
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n and 
# returns the nth Kaprekar number, where as usual we start counting at n==0.
def isKaprekarNumber(n):
    sq = n*n
    x = numberOfDigits(sq)
    i = 1
    while i <= x:
        # two conditions, right part is not zero AND sum of two parts == n
        if sq % pow(10, i) and n == sq // pow(10, i) + sq % pow(10, i):
            return(True)
        i+=1
    return(False)

def nthKaprekarNumber(n):
    i = 0
    ans = 1
    while True:
        #write a function to check if the number is a Kaprekar number
        if isKaprekarNumber(ans):
            if i==n:
                return(ans)
            i+=1
        ans+=1
    return(ans)
# print(nthKaprekarNumber(0))
# print(nthKaprekarNumber(1))
# print(nthKaprekarNumber(2))
# print(nthKaprekarNumber(3))
# print(nthKaprekarNumber(4))
# print(nthKaprekarNumber(5))
# print(nthKaprekarNumber(6))
# print(nthKaprekarNumber(7))
# print(nthKaprekarNumber(8))
# print(nthKaprekarNumber(9))
# print(nthKaprekarNumber(10))
# print(nthKaprekarNumber(11))