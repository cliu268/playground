# strChange
# Inputs: a, b
# Output: int
# Given two strings a and b of the same length, recursively solve for the number of characters that differ between the two strings. 
# Ex. ‘abcd’, ‘aaaa’ ⇒ 3
# The characters at indices 1,2,3 are different but the character at index 0 is the same. 
def strChange(a, b):
    if len(a) == 0:
        return 0
    elif a[0] == b[0]:
        return strChange(a[1:], b[1:])
    else:
        return 1 + strChange(a[1:], b[1:])
print(strChange('abcdefgh', 'aaaakflh'))

# recursiveDict
# Inputs: a
# Output: dict (char -> int)
# This function takes in a string and outputs a dictionary with each letter mapping to its corresponding count inside of the string
# Ex. ‘aba’ ⇒ {‘a’ : 2, ‘b’ : 1}
def recursiveDict(a):
    if len(a)==0:
        return {}
    else:
        d = recursiveDict(a[1:])
        if a[0] in d:
            d[a[0]] += 1
        else:
            d[a[0]] = 1
        return d

def nonRecursiveDict(a):
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d    
print(recursiveDict('abaaabbccccdefggijjjabjjcfg'))
print(nonRecursiveDict('abaaabbccccdefggijjjabjjcfg'))

# permutations
# Inputs: A
# Output: int list list
# Given an int list A, return all permutations (or different orderings) of A in an int list list (list of all permutations).
# Ex. [1,2,3] ⇒ [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def permutatehelper(A, index):
    if index >= len(A) - 1:
        return [A.copy()]

    total = []
    for i in range(index, len(A)):
        swap(A, i, index)
        store = permutatehelper(A, index + 1)
        swap(A, i, index)
        total = total + store
    return total

def permutations(A):
    return permutatehelper(A, 0)
print(permutations([1,2,3]))    

# subsetSum
# Inputs: A, target
# Output: boolean
# Given an int list A, return if some subset of the integers inside of A sum up to target
# Ex. [1,2,3,4,5], 7 ⇒ True
# The numbers 2 and 5 sum up to 7
def subsetHelper(currentList, index, realList, target):
    if index >= len(realList):
        return sum(currentList) == target
    temp = currentList.copy()
    temp.append(realList[index])    
    alpha = subsetHelper(temp, index + 1, realList, target)
    beta  = subsetHelper(currentList.copy(), index + 1, realList, target)
    return alpha or beta

def subsetSum(A, target):
    return subsetHelper([], 0, A, target)
print(subsetSum([1,2,3,4,5], 7))