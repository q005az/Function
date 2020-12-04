def maxdel(a,b):
    c=0
    while a!=0:
        if a>b:
            c = a - b
            a=b
            b=c
        else:
            c=b-a
            a=b
            b=c
    return c
a,b=map(int,input().split())
print(maxdel(a,b))
