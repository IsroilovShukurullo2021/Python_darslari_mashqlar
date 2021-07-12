n=int(input('natural son kiriting'))
def fun(n):
    qiymat=[]
    for i in range(1,n):
        if i**2<n:
            qiymat.append(i)
    return qiymat
print(fun(n))

