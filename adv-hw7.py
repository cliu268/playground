# count12
# Inputs: int list A
# Output: int
# Recursively returns the number of times that the number 12 appears at index and after (in A)
# Ex. [12,12,3,12], 0 ⇒ 3
def count12(A, index):
    if index > 0:
        return count12(A[index:], 0)
    elif len(A) == 1:
        return 1 if A[0] == 12 else 0
    elif A[0] == 12:
        return 1 + count12(A[1:], 0)
    else:
        return count12(A[1:], 0)
print(count12([2,3,12,12,12,12,12,3,12,1,2,3], 9))

# evenFactorial
# Inputs: int n
# Output: int
# This function takes in an even number n and returns n! but only with the even numbers multiplied.
# Ex. 8 ⇒ 8*6*4*2 ⇒ 384
def evenFactorial(n):
    if n==2:
        return 2
    else:
        return n*evenFactorial(n-2)
print(evenFactorial(10))

# prefixList
# Inputs: int list A, int list B
# Output: boolean
# Without using the in operation, recursively determine if A is a sublist of B
def prefixList(A, B):
    if len(A) > len(B):
        return False
    elif len(A) == len(B):
        return A == B
    elif A[0] != B[0]:
        return prefixList(A, B[1:])
    else:
        return A == B[:len(A)]
print(prefixList([3,4,5], [1,2,3,4,5,6]))

# extraWeirdBunnies
# Inputs: int n
# Output: int
# In this new world, every bunny at a position with a multiple of 3 has 1 ear, 
# every bunny at a position with a multiple of 2 has 3 ears, 
# and every bunny at a position of 6 has 4 ears. 
# Recursively compute the total number of ears. 
def extraWeirdBunnies(n):
    if n==1:
        return 2
    elif n == 6:
        return 4 + extraWeirdBunnies(n-1)
    elif n % 3 == 0:
        return 1 + extraWeirdBunnies(n-1)
    elif n % 2 == 0:
        return 3 + extraWeirdBunnies(n-1)
    else:
        return 2 + extraWeirdBunnies(n-1)
print(extraWeirdBunnies(15)) # 2,3,1,3,2,4,2,3,1,3,2,1,2,3,1

# pruneString
# Inputs: String s
# Output: String
# Return a string that has all the characters ‘x’ removed. 
# “abcdxe” ⇒ “abcde”
def pruneString(s):
    if len(s) == 1:
        return "" if s == "x" else s
    else:
        return pruneString(s[1:]) if s[0] == 'x' else s[0] + pruneString(s[1:])
print(pruneString("abcdxexxyqxxii"))

# Challenge: stringClean
# Inputs: String s
# Output: String
# Recursively compute a new string where consecutive characters are grouped together. 
# Ex. “yyyyxxzz” ⇒ “yxz”
def stringClean(s):
    if len(s) <= 1:
        return s
    elif s[0] == s[1]:
        return stringClean(s[1:])
    else:
        return s[0] + stringClean(s[1:])
print(stringClean("yyyyxxzz"))



