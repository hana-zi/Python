def sumof(n):
    s=0
    for i in range(1,n+1):
        s+=i
def sumof4(n):
        if n <=1:
            return n
        return n
    else:
        return n+sumof4(n-1)
    num=int(input('正の整数>'))
    ans=sumof4(num)
    print(ans)
