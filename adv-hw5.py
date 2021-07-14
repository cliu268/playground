# Reduce each of the following big O notations to its simplest form
# O(n^3 + 2n^2) = O(n^3)
# O(n) = O(n)
# O(5n^2 + 2n + ln(n)) = O(n^2)
# O(max(n^3, n^2)) = O(n^3)
# O(sin(n)) = O(1) ==> this is because when you put a large n, sin(n) will be 1 which is a constant
# O(log3(n^15)) = O(log(n)) ==> this is because 3 and 15 are constant and can be removed 
# O(log(n!) = O(n log(n)) ==> I am not totally sure, but this will be the upper bound
# Challenge!
# What time complexity do the following algorithms run in?
# a. O(1)
# b. O(n^2)
# c. O(n)

# search 
# Inputs: int[] A, target
# Output: boolean
# Returns True if target exists inside of A and false otherwise
# Make sure the algorithm runs in O(n) time!
# Challenge, try to make it run in O(log(n)) time! (This is binary search)
def search(A, target):
    for i in range(len(A)):
        if target == A[i]:
            return True
    return False

def binarySearch(A, target):
    if len(A)<=1:
        return (A[0] == target)
    else:
        if A[len(A)//2] == target:
            return True
        elif A[len(A)//2] < target:
            return binarySearch(A[len(A)//2 + 1 :], target)
        else:
            return binarySearch(A[:len(A)//2], target)
print(binarySearch([1,2,3,4,5,6,7,8], 1))

# Write an algorithm that takes O(n^3) time to run
# This can be any algorithm! Just manipulate it so that it takes n^3 time to run
def cubeAlgo(A): #print a 3 dimentional array
    for i in range(len(A)):
        for j in range(len(A[i])):
            for k in range(len(A[i][j])):
                print(A[i][j][k])
cubeAlgo([[[1,2],[3,4,5]],[[3,4,5],[6,7]],[[2],[3,4,5,6]]])

# Challenge!
# Write an algorithm that takes O(log(n)) time to run!

# here is another O(log(n)) algorithm example from this website
# https://www.geeksforgeeks.org/count-fibonacci-numbers-given-range-log-time/

# Python3 program to count Fibonacci
# numbers in given range
 
# Returns count of fibonacci
# numbers in [low, high]
def countFibs(low, high):
     
    # Initialize first three
    # Fibonacci Numbers
    f1, f2, f3 = 0, 1, 1
 
    # Count fibonacci numbers in
    # given range
    result = 0
 
    while (f1 <= high):
        if (f1 >= low):
            result += 1
        f1 = f2
        f2 = f3
        f3 = f1 + f2
 
    return result
 
# Driver Code
low, high = 10, 10000
print("Count of Fibonacci Numbers is",
                 countFibs(low, high))
 
# This code is contributed
# by mohit kumar