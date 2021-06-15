# q1 
# (Loops) Use a for loop to print out the multiples of 5 from 1-200 inclusive
def q1():
    for i in range(1, 201):
        if i%5 == 0:
            print(i)

# q2
# (Loops) Use a while loop to print out the first 25 powers of 3! (3, 9, 27, 81, … etc.)
def q2():
    n=1
    while n<=25:
        print(pow(3, n))
        n+=1

# q3
# (Loops) Use a for loop to calculate 25! (pronounced 25 factorial, let me know if you have questions)
def q3():
    ans=1
    for i in range(1, 26):
        ans*=i
    return ans

# q4
# (Loops and Lists) Start with an empty list and add the first 15 multiples of 3 to the list
def q4():
    ans=[]
    for i in range(1, 16):
        ans.append(3*i)
    return ans

# q5
# (Loops and Lists) Write a function that takes in a list and an integer and returns a boolean. The boolean should be true if the list contains the integer and false otherwise.
def q5(l, i):
    return i in l

# q6
# (Loops and Sets/Dictionaries) Write a function that takes in 2 sets and returns true if the sets have any elements in common and false otherwise. 
def q6(s1, s2):
    for x in s1:
        if x in s2:
            return True
    return False

# q7
# (Loops and Sets/Dictionaries) Write a function that takes in two dictionaries and returns a dictionary (representing the “union” of the dictionaries). For any key that exists in both dictionaries, the final dictionary should have the key and the corresponding value will be the values from the first and second dictionary multiplied. For any key that only exists in one dictionary, the final dictionary should just have the original key and value. 
def q7(d1, d2):
    ans={}
    for x in d1:
        if x in d2:
            ans[x] = d1[x]*d2[x]
        else:
            ans[x] = d1[x]
    for y in d2:
        if y not in d1:
            ans[y] = d2[y]
    return(ans)

# q8
# (Loops and Sets/Dictionaries) Write a function that takes in two dictionaries and outputs a list that contains all keys shared between both dictionaries.
def q8(d1, d2):
    ans=[]
    for x in d1:
        if x in d2:
            ans.append(x)
    return(ans)

#### test drivers ###
# q1()
# q2()
# print(q3())
# print(q4())
# print(q5([1,2,5,6,8,9], 7))
# print(q6({1,3,5,7,9}, {2,4,6,8,9}))
# print(q7({1:1,3:3,5:5,7:7,9:9}, {3:3,5:5,9:9,2:2,8:8}))
# print(q8({1:1,3:3,5:5,7:7,9:9}, {3:3,5:5,9:9,2:2,8:8}))
