# Write a function that takes in a dictionary as input and returns the sum of all values in the dictionary
def dicSum(d):
    sum = 0
    for i in d:
        sum += d[i]
    return sum
# print(dicSum({'a':5, 'b':7, 'ff':99, 'rr':66}))   
 
# Write a function that takes in two lists (L1 and L2 of the same length) and returns a dictionary where each element from L1 is the key and the element with the same index in L2 is the value
# Ex. [1,2,3],[4,5,6] ⇒ {1:4,2:5,3:6}
def listToDic(L1, L2):
    d = {}
    for i in range(len(L1)):
        d[L1[i]] = L2[i]
    return d
# print(listToDic([1,2,3,4,5], [9,8,7,6,5])) 
   
# Write a function that takes in a dictionary and outputs the 3 highest values with their corresponding keys
def highestThree(d):
    key = [0,0,0]
    val = [0,0,0]
    for i in d:
        if d[i] >= val[0]:
            val[2] = val[1] 
            val[1] = val[0]
            val[0] = d[i]
            key[2] = key[1]
            key[1] = key[0]
            key[0] = i
        elif d[i] >= val[1]:
            val[2] = val[1] 
            val[1] = d[i]
            key[2] = key[1]
            key[1] = i        
        elif d[i] > val[2]:
            val[2] = d[i]
            key[2] = i
    return {key[0]:val[0], key[1]:val[1], key[2]:val[2]}
# print(highestThree({'aaa':333, 'hhh':456, 'r':123, 'pp':888, '123':678, 7:8, 9:888}))    

# Write a function that takes in a string (lowercase) as an argument and outputs a dictionary mapping each letter to its count
# Ex: “yayyyy: ⇒ {‘a’:1, ‘y’:5}
def letterCount(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d
# print(letterCount('yayyyy'))    

# Challenge Problems!
# Do all of the problems in 1 recursively!!
# Q1 Given an integer, returns the sum of the digits
def sumOfDigits(n):
    if n < 10:
        return n
    else:
        return n%10 + sumOfDigits(n//10)
# print(sumOfDigits(123450900))        

# Q2 Given an integer, rteurtns the binary representation of it
def binaryInt(n):
    if n < 2:
        return n
    else:
        return str(binaryInt(n//2)) + str(n%2)
# print(binaryInt(23))        

# Q3 Given two strings a, b with string a being a smaller string than b, returns True if a is a substring in b False otherwise
def isSubString(a, b):
    if len(a) == len(b):
        return True if a == b else False
    else:
        return isSubString(a, b[:-1]) or isSubString(a, b[1:])
# print(isSubString('abc', 'dflasjflkabcoijoj'))

# Q4 Given a string, prints it in reverse order. Ex: "abcd ef" => "fe dcba"
def printReverse(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + printReverse(s[:-1])
# print(printReverse('abcd ef'))

# Q5 Given a string, returns True if it is a palindrome and False otherwise
def palindrome(s):
    if len(s) == 1:
        return True
    elif len(s) == 2:
        return True if s[0] == s[1] else False
    elif s[0] != s[-1]:
        return False
    else:
        return palindrome(s[1:-1])
# print(palindrome('asdfabbafdsa'))
        

# print('abcdefg'[:len('abcdefg')-1]) # prints 'abcdef' no g
# print('abcdefg'[len('abcdefg')-1])  # prints g