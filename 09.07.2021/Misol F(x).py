def f(x):
    if x==0:
        return 0
    elif x%2==0:
        return 1
    else:
        return -1
x=int(input("x ni kiriting: "))
y=f(x)
print(y)