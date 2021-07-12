def katta(a,b):
    if a>b:
        return a
    elif a==b:
        return b+a
    else:
        return b
a=int(input('a ni: '))
b=int(input('a ni: '))
print(katta(a,b))
