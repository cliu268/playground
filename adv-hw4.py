# Let A = [[1,2,3,4,5],[3,4,5,6,7],[2,3,4,5,6]]
# What does print(A[0]) print out?
# What does print(A[1]) print out?
# What happens if I print out print(A[2])
A = [[1,2,3,4,5],[3,4,5,6,7],[2,3,4,5,6]]
print(A[0])
print(A[1])
print(print(A[2])) # there is no return value for print(A[2]), so it will print None

# sum
# Inputs: A
# Output: int
# This function returns the sum of all elements in the 2D array A
def sum(A):
    total=0;
    for i in A:
        for j in i:
            total+=j
    return total
print(sum(A))

# max
# Inputs: A
# Output: int
# This function returns the maximum of all elements in the 2D array A
def max(A):
    max=A[0][0]
    for i in A:
        for j in i:
            if j>max:
                max=j
    return max
print(max(A))

# first4
# Inputs: A
# Output: int
# This function returns the product of the row and column of the first 4 that is encountered (when iterated from left to right, up to down)
# [[1,2],[3,4]] ⇒ row = 1 col = 1 ⇒ 1*1 = 1
def first4(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j]==4:
                return i*j
    return None
print(first4([[1,2,3,5],[3,5,6,7],[2,3,5,4,6]]))

# coordDict
# Inputs: A
# Outputs: dict
# A is a 2D dictionary that contains only booleans. Return a dictionary that takes in an int*int key ((row, column)) and has the corresponding boolean value in the dictionary.
# Ex. [[True, False], [False, True]] ⇒ {(0,0):True, (0,1):False, (1,0):False, (1,1):True}
def coorDict(A):
    dict={}
    for i in range(len(A)):
        for j in range(len(A[i])):
            dict[(i,j)]=A[i][j]
    return dict
print(coorDict([[True, False, False, True, True], [False, True], [True, True, False]]))