# P4
def triangularPattern(n):
    i = 1
    while i <= n:
        digit = 1
        line = 0
        while digit <= i:
            line += digit * pow(10, i - digit)
            digit += 1
        print(line)
        i += 1
# for index in range(1, 10):
#     triangularPattern(index)
#     print("---------------")

# Q1
# Write a function that takes in a string s as an input and returns True if the string is a palindrome 
# and false otherwise. 
def isPalindrome(s):
    x = 1
    y = len(s)
    while x < y:
        if s[x-1] != s[y-1]:
            return False
        x += 1
        y -= 1
    return True
#print(isPalindrome("ababccbaba"))

# Q2
# largestNumber
# Write the function largestNumber(text) that takes a string of text and returns the largest int value 
# that occurs within that text, or None if no such value occurs. You may assume that the only numbers 
# in the text are non-negative integers and that numbers are always composed of consecutive digits 
# (without commas, for example). For example:
#     largestNumber("I saw 3 dogs, 17 cats, and 14 cows!")
# returns 17 (the int value 17, not the string "17"). And
#     largestNumber("One person ate two hot dogs!")
# returns None (the value None, not the string "None").
# Hint: use isdigit
def largestNumber(text):
    hasNumbers = False
    ans = 0
    temp = 0
    for index in range(len(text)):
        if text[index].isdigit():
            hasNumbers = True
            temp = temp * 10 + int(text[index])
        elif ans < temp:
            ans = temp
            temp = 0
        else:
            temp = 0
    # the following syntax is called ternary conditional operator
    # it is the same as if you wrote if/else separately got it?
    return ans if hasNumbers else None
# print(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!"))
# print(largestNumber("One person ate two hot dogs!"))

# Q3 
# rotateStringLeft
# Write the function rotateStringLeft(s, n) that takes a string s and a possibly-negative integer n. 
# If n is non-negative, the function returns the string s rotated n places to the left. If n is negative, 
# the function returns the string s rotated |n| places to the right. So, for example:
# assert(rotateStringLeft('abcd',  1) == 'bcda')
# assert(rotateStringLeft('abcd', -1) == 'dabc')
def rotateStringLeft(s, n):
    n = n % len(s)
    return s[n:] + s[:n]
# print(rotateStringLeft('abcdefgh', 13))
# print(rotateStringLeft('abcdefgh', -13))
# print(rotateStringLeft('abcd', 1))
# print(rotateStringLeft('abcd', -1))

# Q4
# isRotation
# Write the function isRotation(s, t) that takes two possibly-empty strings and returns True if one is 
# a rotation of the other. Note that a string is not considered a rotation of itself. 
# Hint: The previous problem may be helpful here.
def isRotation(s, t):
    if len(s) != len(t):
        return False
    elif s == t: # same string
        return False
    else:
        for i in range(1, len(s)):
            if s == rotateStringLeft(t, i):
                return True
        return False
# print(isRotation('abcdef', 'cdefab'))

