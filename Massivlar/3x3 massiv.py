numbers=(1,2,3,4,5,6)
mk=[]
mb=[]
i=0
for k in numbers:
    i+=1
    if i%2==0:
        mk.append(k)
    else:
         mb.append(k)
print(mk)
print(mb)