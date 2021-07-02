sonlar=[4,8,7,6,12,9,11]
for i in range(len(sonlar),1):
    if sonlar.index(i)%2==0:
       sonlar.index(i)==sonlar.index(i-1)
    else:
        sonlar.index(i)==sonlar.index(i+1)
print(sonlar)


