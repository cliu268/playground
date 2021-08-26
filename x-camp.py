# Q1
# Ones digit of an integer
# Time Limit: 0.2s   Memory Limit: 32M 
# Description
# When an integer is inputted, output the ones digit of the integer.
# Input
# An integer.
# Output
# An integer.
# Sample Input
# 102
# Sample Output
# 2
def q1():
    n=int(input())
    print(n%10)

# Q2
# Find the remainder
# Time Limit: 0.2s   Memory Limit: 32M 
# Description
# Given two integer inputs a and b, output the remainder of a/b.
# Input
# Two integers.
# Output
# An integer.
# Sample Input
# 5 2
# Sample Output
# 1
def q2():
    a=input().split(" ")
    print(int(a[0])%int(a[1]))

# Q3
# complete number
# Enter N ,output all the complete numbers in 1~N (complete number means that the sum of all factors is equal to 
# its own, such as 6=1+2+3, 6 is the perfect number)
# Sample input:
# 10
# Sample output:
# 6
# time limit:
# 1000
# memory limit:
# 65536
def completeNumber(n):
    for i in range(1,n):
        sum=0
        for j in range(1,i):
            if i%j==0:
                sum+=j
        if sum==i:
            print(i)

def q3():
    n=int(input())
    completeNumber(n)

# Q4
# Prime number or not
# Time Limit：1s   Memory Limit：256M
# Description
# A prime number,which is the favorite in number theory, is the number which can only be divided by 1 and itself. 
# For example,2,3,5,7,11,13,17 are prime numbers. Given an integer n,please tell us whether n is a prime number.
# Input
# The first line is an integer T.  1<=T<=10
# The following T lines,each line contains an integer n.  1<=n<=105
# Output
# T lines. If the integer in this line is prime number,output "Yes",else,output "No".
# Sample Input
# 2
# 1
# 2
# Sample Output
# No
# Yes 
# Hint
# Use loop to take T inputs of n and output "Yes/No" results.
def q4():
    t=int(input())
    for i in range(t):
        n=int(input())
        if n>1:
            for j in range(2,n):
                if n%j==0:
                    print("No\n")
                    break
            else:
                print("Yes\n")
        else:
            print("No\n")

# Q5
# Pyramid
# Input: integer n where 2<=n<=40
# Output: n lines of * pyramid
# Sample Input
# 4
# Sample Output
#    *
#   * *
#  * * *
# * * * *
def q5():
    n=int(input())
    x=n
    for i in range(1,n+1):
        print((x-1)*" "+i*"* "+(n-1)*" ")
        x-=1

# Q6
# Palindrome
# Time Limit：1s   Memory Limit：256M 
# Description
# The palindrome numbers are the numbers which are read the same with read backwards.For example,
# the 141 is the palindrome number while 144 is not.Now,input an integer n,please find all the palindrome 
# numbers which are not larger than n. 
# Input
# One integer.  1<=n<=100000
# Output
# Each line contains one palindrome number.
# Sample Input
# 11
# Sample Output
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 11
def isPalindrome(x):
    if (len(x)<=1):
        return True
    elif (len(x)==2):
        return x[0]==x[1]
    elif x[0]==x[len(x)-1]:
        return isPalindrome(x[1:len(x)-1])
    else:
        return False
 
def q6(): 
    n=int(input())
    for i in range(1, n+1):
        s=str(i)
        if isPalindrome(s):
            print(str(i))

# Q7
# Sum of string digits
# Time limit: 0.2 memory limit: 32M
# Description of the topic:
# Enter an integer string N to find the sum of the digits of N.
# Please do it using N as a string.
# Input format:
# a number N
# Output format:
# An integer.
# Sample input 1:
# 12345
# Sample output 1:
# 15
# Appointment:
# The length of N is less than or equal to 100.
def sum(s):
    if (len(s)==1):
        return int(s)
    else:
        return int(s[0])+sum(s[1:])
 
def q7():
    n=input()
    print(sum(n))

# Q8
# Merge ordered arrays
# Time Limit:
# 1s Memory Limit: 256M
# Description :
# Give you two ordered arrays. Merge these two arrays into a new ordered array and output it.
# Input:
# Enter the first integer n,m in the first line.
# Enter n numbers in the second line to indicate the first ordered array
# Enter m numbers in the third line to indicate the second ordered array.
# Output :
# Output n+m numbers, indicating the result of the merge of the two arrays.
# Sample input:
# 3 4
# 4 5 8
# 1 3 6 7
# Sample output:
# 1 3 4 5 6 7 8
# Appointment:
# 1 <= n <= 5000000, 1 <= m <= 5000000 , all numbers are in the range of signed 32-bit integers
# Hint:
# Pay attention to the data range
def q8():
    a=[int(s) for s in input().split(" ")]
    n=[int(s) for s in input().split(" ")]
    m=[int(s) for s in input().split(" ")]
    size1=a[0]
    size2=a[1]
    result=[]
    i=0
    j=0
    while i<size1 and j<size2:
        if n[i]<m[j]:
            result.append(n[i])
            i+=1
        else:
            result.append(m[j])
            j+=1
    result+=n[i:]+m[j:]
    for i in result:
        print(i, end=" ")

# Q9
# A * B Problem again
# Time Limit : 0.2s Memory Limit: 32M
# Description:Give you two decimal numbers, up to 1000 digits, and find their product
# Input :Enter an integer in the first line. Enter an integer in the second line
# Output :Output an integer
# Sample input:123123123121423432543543544124354364565765456
# Sample output:50780339022481084579975969090509171076395424
# Appointment:A,B are non-negative integers
# Hint:10 153 1 2 3 6 1 1 1 1 1
# Sample output 2:5
# Appointment:10<n<10^5,0<ai<=10^4,0<=S<10^8
def q9():
    a=int(input())
    b=int(input())
    print(a*b)

# Q10
# Serpentine matrix
# Time Limit：1s   Memory Limit：256M
# Description
# Given an integer n,please input a serpentine n*n matrix.The format of the matirx is given in sample output.
# Input
# The first line is an integer n.  1<=n<=1000
# Output
# n lines.Each line contains n positive integer.
# Sample Input
# 4
# Sample Output
# 1 2 6 7
# 3 5 8 13
# 4 9 12 14
# 10 11 15 16


# Q11
# Expression evaluation
# Time Limit：1s   Memory Limit：64M 
# Description
# Expression evaluation:input expression which is made of number,'+','-','*','/','^','(',')',output the result of the expression.
# Input
# One expression
# The length of the expression is no more than 100.The value that appears in the operation is a small number. The data like 2^3^4 doesn't exist.
# Output
# The result of the expression.The result keep three decimal digits.
# Sample Input1
# 3*(5+3^2*(3-4)+6/2)+2.5
# Sample Output1
# -0.500 
# Sample Input2
# 2^0.5
# Sample Output2
# 1.414
def q11():
    s=input()
    new=s.replace("^", "**")
    print("%.3f" % eval(new))

# Q12
# maximize the minimum
# Time Limit: 0.2s Memory Limit: 32M
# Description:Farmer John took a hut with N cowsheds. The barn is lined up, the i-barn is in the xi position. 
# But his M cow are very dissatisfied with the hut and often attack each other. In order to prevent the cows 
# from hurting each other, John decided to put each cow in the barn as far as possible from other cows. That is 
# to maximize the distance between the two adjcent cows.
# Input :In the first line, enter 2 integers N,MIn the second line, enter N integer xi
# Output :Output an integer, the maximum closest distance
# Sample input:5 31 2 8 4 9
# Sample output:3
# Appointment:2<=N<=100000,2<=M<=N,0<=xi<=109


# Q13
# median node
# Find the median node of the tree, which is the node who has the smllest longest distance from itself to any node
# of the tree. In another word, it's a node that minimize the longest distance from the node to any other node.
# Input :
# In the first line enter the number of nodes n and the number of edges m, and then it's followed by a total of m 
# lines below, where each line contains one pair of integers describing one edge)
# Output :
# Print out all median nodes of the tree in sorted increasing order.
# Sample input:
# 6 5
# 1 2
# 1 3
# 1 4
# 1 5
# 5 6
# Sample output:
# 1 5
# time limit:
# 1000
# memory limit:
# 65536


# Q14
# Dynamic inversion pairs
# For a sequence A, its number of inverse pairs is defined as the number of pairs (i, j) satisfying i < j and A[i] > A[j]. 
# For an permutation of numbers from 1 to n as part of the input, we will delete m elements in some certain order as 
# another part of input, and your task is to count the number of inverse pairs of the entire sequence before deleting 
# each elements.
# Input :
# The first line of input contains two integers, n and m, representing number of elements and number of elements that 
# will be deleted. The following n lines each line contains a positive integer between 1 and n, which is the initial 
# permutation. The following m lines are a positive integer per line representing elements that will be deleted each 
# time.
# Output :
# The output contains m rows, , representing the number of reverse pairs before deleting each element in turn
# Sample input:
# 5 4
# 1
# 5
# 3
# 4
# 2
# 5
# 1
# 4
# 2
# Sample output:
# 5
# 2
# 2
# 1
# Data Limit:
# Test case No. 1-2, 3-4, 5-6, 7-8, 9-10
# n <=1000 <=30000 <=50000 <=60000 <=100000
# m <=100 <=10000 <=20000 <=40000 <=50000
# Time Limit:
# 1000
# Memory Limit:
# 512000


# Q15
# cipher machine
# A cipher machine generates a password in the following way: first enter a series of numbers into the machine, 
# then take a part of them, and XOR them to get a new number as a password. Now please simulate the operation of 
# such a cipher machine, the user generates a password by inputting a control command.
# A sequence of numbers is stored in the cipher machine, which is initially empty. There are three types of control 
# commands for the crypto machine:
# ADD
# Add to the end of the series.
# REMOVE
# Find the first equal number in the series and remove it from the series.
# XOR BETWEEN AND
# For all the numbers in the sequence that are greater than or equal to and less than or equal to, the XOR is 
# sequentially performed, and the final result is output as a password. If only one number satisfies the condition, 
# this number is output. If no number satisfies the condition, output 0.
# You can assume that the user will not REMOVE a number that does not exist in the series, and that all inputs do not 
# exceed 20,000.
# Input :
# The input file includes a series of control commands. Each control command occupies a separate line. There are no 
# extra blank lines in the input file.
# Output :
# For each XOR command, the password generated by your cipher machine is included in the output line. The output file 
# should not contain any extra characters.
# Sample input:
# ADD 5
# ADD 6
# XOR BETWEEN 1 AND 10
# REMOVE 5
# XOR BETWEEN 6 AND 8
# Sample output:
# 3
# 6
# data range:
# The file does not exceed 60,000 lines.
# time limit:
# 1s
# Memory Limit:
# 256M