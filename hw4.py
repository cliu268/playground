# basic questions
# Write a function that takes in a string s and outputs the string in lowercase
# Ex. “HELLO” ⇒ “hello”
def convertLower(s):
    return(s.lower())
# print(convertLower("HELLO"))
    
# Write a function that takes in a string s and outputs the string in uppercase
# Ex. “hello” ⇒ “HELLO”
def convertUpper(s):
    return(s.upper())
# print(convertUpper("hello"))

# Write a function that takes in a string s and output true if the string contains the string “Yolo”
def isYolo(s):
    return 'Yolo' in s
# print(isYolo("GME Yolo Yoooo!!"))

# Write a function that takes in an integer list and returns the sum of all the elements
# Ex. [1,2,3,4,5,6] ⇒ 21
def listSum(l):
    sum = 0
    for i in l:
        sum += i
    return sum
# print(listSum([1,2,3,4,5,6]))    

# Write a function that takes in an integer list and an integer and returns true if the integer is in the integer list
def inIntList(l, i):
    return i in l
# print(inIntList([1,5,7,9,333], 8))    
# print(inIntList([1,5,7,9,333], 9)) 

# Write a function that takes in an integer list and returns the average of all the elements
def listAvg(l):
    return listSum(l)/len(l)
# print(listAvg([1,2,3,4,5,6,7,8,9,10]))

# Write a function that takes in an integer list and returns the second largest element in the array
def secondLargest(l):
    l.sort(reverse=True)
    return l[1]
# print(secondLargest([2,6,7,55,12,55,33,8,9]))

# Write a function that takes in an integer list and an integer and returns the integer list shifted to
# the right by the number Ex. ([1,2,3,4,5,6], 4) ⇒ [3,4,5,6,1,2]
def shiftRight(l, n):
    # ans = l[:]
    # n = n % len(l)
    # for i in range(len(l)):
    #     if i + n < len(l):
    #         ans[i + n] = l[i]
    #     else:
    #         ans[i + n - len(l)] = l[i] 
    # return ans
    return l[len(l)-n:] + l[:len(l)-n]
# print(shiftRight([1,2,3,4,5,6], 4))

# challenge questions
# 1. Returns the sum of the values of a given integer array
# 2. Returns the decimal average of the elements of a given integer array
# 3. Checks to see if an integer element exists in an integer array given the element and array
def isInList(L, n):
    return n in L
# print(isInList([1,2,3,4,5], 5))    

# 4. Returns another array with elements of the given array but in reverse order (w/o using built-in functions)
def reverseOrder(L):
    for i in range(len(L)//2):
        temp = L[i]
        L[i] = L[len(L) - 1 - i]
        L[len(L) - 1 - i] = temp
    return L
# print(reverseOrder([1,2,3,4,5,6]))

# 5. Returns an integer array that has no duplicate values given an integer arry (hint: loop multi-times)
def noDuplicate(L):
    res = []
    for i in L:
        if i not in res:
            res.append(i)
    return res
# print(noDuplicate([1,2,3,1,2,3,1,1,1,3,3,3,4,5,6,7,4,5,7,8,9,1]))

# 6. Returns the second largest element in an integer array
# 7. Given 2 arrays, checks to see if the arrays are equal (here the == doesn't work to compare arrays directly)
def equalArray(L1, L2):
    if len(L1) != len(L2):
        return False
    else:
        for i in range(len(L1)):
            if L1[i] != L2[i]:
                return False
        return True
# print(equalArray([1,2,3,4,5], [1,2,3,4,5]))        

# 8. Given an integer array, returns an array that contains the same numbers except all even numbers come 
#    before all the odd numbers
def evenBeforeOdd(L):
    even = []
    odd = []
    for i in L:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return even + odd
# print(evenBeforeOdd([0,6,9,3,5,7,9,1,2,3,10,4,6,88]))

# 9. Given an non-empty integer array that contains the element 4, return a new array that contains the
#    elements from the original array that come before the first 4
def elementBeforeFour(L):
    return L[:L.index(4)]
# print(elementBeforeFour([3,5,6,7,8,3,2,4,2,1]))

#10. Given an integer array and a non-negative number n, return a integer array with the same elements as
#    the input but shifted to the left by n. 
#    ex: [1,2,3,4,5], n=2 -> [3,4,5,1,2] 
#        [1,2,3,4], n=4 -> [1,2,3,4]
#        [1,2,3,4], n=0 -> [1,2,3,4]
def shiftLeft(l, n):
    # shift to left by n means to shif to right by len-n
    return shiftRight(l, len(l) - n)
# print(shiftLeft([1,2,3,4,5,6], 2))

# not covered questions
# 1. Prints out the 2D integer array in a grid-like format
def print2D(L):
    for x in L:
        for y in x:
            print(y, end=', ')
        print('')
# print2D([[33,55,66,7], [2,8,9], [77,33,22]])        

# 2. Returns the ith row of a given 2D string array
# 3. Returns the 2D integer array which is the sum of 2 input 2D integer arrays
# 4. Checks to see if all the rows in the 2D integer array sum to a number given the number and 2D array 
# 5. Checks to see if all the columns in the 2D integer array sum to a number given the number and 2D array
# 6. Returns an integer array of size 3 that contains the 3 smallest elements (ordered from least to greatest)
#    in a given 2D integer array

