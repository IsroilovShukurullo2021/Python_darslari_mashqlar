k=int(input('k ni kirit '))
def buluvchi(m):
    tex=''
    for i in range(1,m+1):
          if m%i==0:
              tex+=str(i)+' '
    print(tex)
buluvchi(k)