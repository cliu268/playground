# Recursion (all of the following functions should be done recursively)
# Write a function that takes in a positive integer (n) as input and returns the nth fibonacci number.
# fibonacci(1) = 1
# fibonacci(2) = 1
# fibonacci(3) = 2
def fibonacci(n):
    if n < 3:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(30))

# Write a function that takes in a positive integer (n) as input and returns the sum of the digits of n
# sumDigits(1234) = 10
# sumDigits(12) = 3
# sumDigits(5684958) = 45
def sumDigits(n):
    if n < 10:
        return n
    else:
        return n%10 + sumDigits(n//10)
# print(sumDigits(5684958))

# Write a function that takes in a string (s) as input and returns True if it is a palindrome and False otherwise
# isPalindrome(“abcd”) = False
# isPalindrome(“abba”) = True
def isPalindrome(s):
    if len(s) == 1:
        return True
    elif len(s) == 2:
        return True if s[0] == s[1] else False
    elif s[0] != s[-1]:
        return False
    else:
        return isPalindrome(s[1:-1])
# print(isPalindrome('aasdfsaasfdsaa'))

# Write a function that takes in two strings (s1, s2) and returns True if s1 is a substring of s2.
# isSubstring(“abc”, “abcd”) = True
# isSubstring(“def”, “abcd”) = False
def isSubString(a, b):
    if len(a) == len(b):
        return True if a == b else False
    else:
        return isSubString(a, b[:-1]) or isSubString(a, b[1:])
# print(isSubString('abc', 'abcd'))
# print(isSubString('def', 'abcd'))

# Write a function that takes in two integers (a,b) and computes a^b.
# pow(2,3) = 2^3 = 8
# pow(3,6) = 3^6 = 729
def myPow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return ZeroDivisionError if a == 0 else 1/myPow(a, -b)
    else:
        return a*myPow(a, b-1)
# print(myPow(2,3))
# print(myPow(3,6))
# print(myPow(0, -5))

# Write a function that takes in two strings of equal length (s1, s2) and returns the strings interleaved 
# with each other, starting s1 first.
# interleaveString(“abc”,”def”) = “adbecf”
# interleaveString(“12”, “ab”) = “1a2b”
def interleaveString(s1, s2):
    if len(s1) == 1:
        return s1 + s2
    else:
        return s1[0] + s2[0] + interleaveString(s1[1:], s2[1:])
# print(interleaveString('abc', 'def'))
# print(interleaveString('12', 'ab'))

# Data Science!
# In the email, there should be an attached file called “data.txt”. Using open, take the file and read the file into python!
# Copy and paste a screenshot of your code that reads the file into python! 
# Print out the contents of the txt file! What does it say?
openfile = open('./data.txt', 'r')
all = openfile.read()
print(all)
# for line in openfile:
#     print(line, end='')

# Inside the email there should also be a numwins.csv file containing the number of wins I had in brawl stars on various days, read it into python!
import pandas as pd
df = pd.read_csv('numwins.csv', header=None)  # the csv file has no header, if you don't specify this, first value becomes column header
# print(df)
# print(df.head())
# print(df.info())
# print(df.shape[0])

# What is the mean number of wins that I had?
print(df.mean())

# How many data entries do I have in total?
print(len(df))

# What is the maximum number of wins that I have had in a day?
print(df.max())

# What is the minimum number of wins that I have had in a day?
print(df.min())

# Make a dictionary similar to the one I made in class:
# Each key should be a multiple of 10 up to 100
# Each value should represent the number of days that I had a win total between key-9 and key
# Ex. The key-value pair {10:15} means that I had 15 days where I won between 1 and 10 times (inclusive)
d = {}
for i in range(1, 11):
    d[i*10] = 0
ds = df[df.columns[0]].value_counts()
# print(ds.to_string()) 
for i in ds.keys():
    if i == 0: # don't count days with 0 wins
        continue
    index = 10 * ((i-1)//10 + 1)
    d[index] += ds[i]
    # print({'key': i, 'index': 10 * ((i-1)//10 + 1), 'wins': ds[i]})
print(d)