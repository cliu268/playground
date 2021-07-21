# binarySearchRight
# Inputs: A, target
# Output: int
# This function searches for a target in an integer list A. This function should return the rightmost index of the target inside of A (the target can appear more than one time inside of A).
# Ex. [1,2,2,3,3,3], 3 ⇒ 5
# 5 is the rightmost index/appearance of 3
def binarySearchRight(A, target):
    low = 0
    high = len(A)
    while low < high:
        mid = (low + high) // 2
        if A[mid] == target:
            if mid == len(A)-1 or A[mid+1] != target:
                return mid
            low = mid + 1
        elif A[mid] < target:
            low = mid + 1
        else:
            high = mid
    return -1
print(binarySearchRight([1,2,2,3,3,3], 3))

# squareRoot
# Inputs: n
# Output: int
# This function should search for the square root of the input n (we assume in this case that n is a positive integer that has a clearly defined, integer square root, that is to say that n is a square number).
# Rules: You are not allowed to do this with the ** operator
# Half credit for the O(n) solution, full credit for the O(nlog(n)) solution. 
def squareRoot1(n):    
    for i in range(n+1):
        if i*i == n:
            return i

def squareRoot2(n):
    low = 0
    high = n+1
    while low < high:
        mid = (low + high) // 2
        if mid*mid == n:
            return mid
        elif mid*mid < n:
            low = mid + 1
        else:
            high = mid
    return -1
print(squareRoot1(144))
print(squareRoot2(144))

# What are the recurrence relations and base cases for the following sequences?
# Ex. 1,2,3,4,5,6 … 
# xn = xn-1 + 1
# x0 = 1
# Or, use x(0)/x(n) to denote subscript

# 2,4,6,8,10…
# x(0) = 2
# x(n) = x(n-1) + 2

# 1,4,9,16,25,36 …
# x(0) = 1
# x(n) = x(n-1) + 2n + 1  ==> this is because x(n) = (n+1)^2, so the diff between x(n) and x(n-1) is (n+1)^2 - (n)^2 which is 2n+1

# 0,1,1,2,3,5,8,13,21…
# This is the fibonacci sequence, where each number is the sum of the previous two!
# Hint! There might be multiple base cases
# fibonacci sequence: x(n) = x(n-1) + x(n-2)
# base case: x(0) = 0 and x(1) = 1

# 1,3,1,3,1,3,1,3....
# This sequence repeats every two! 
# base case: x(0) = 1 and x(1) = 3
# sequence: x(n) = x(n-2)