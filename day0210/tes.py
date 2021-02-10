def sumof(n):
    sum=0
    for i in range(n+1):
        sum+=i
    return sum
n=int(input('正の整数>'))
ans=sumof(n)
print(ans)
