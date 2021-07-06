# Maxsus masala
a=(1,2,3,4,5,6,8)
b=list(a)
mk=[]
k=len(b)-1
for i in range(len(b)//2):
    mk.append(b[i])
    mk.append(b[k])
    k-=1
print(mk)