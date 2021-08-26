def weirdAlgo(n):
    if n==1:
        print(n, end=' ')
        return n
    elif n%2==0:
        print(n, end=' ')
        return weirdAlgo(n//2)
    else:
        print(n, end=' ')
        return weirdAlgo(1+n*3)

#weirdAlgo(int(input()))

# a=input().split(" ")
# print(int(a[0])%int(a[1]))

def completeNumber(n):
    for i in range(1,n):
        sum=0
        for j in range(1,i):
            if i%j==0:
                sum+=j
        if sum==i:
            print(i)

n=int(input())
completeNumber(n)