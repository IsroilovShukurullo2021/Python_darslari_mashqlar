n=int(input('son kiriting: '))
def fun(num):
    yig = 0
    for i in str(num):
        yig+=int(i)
    print(yig)
fun(n)

# ikkinchi usul
def xona_yig(a):
    bir= a%10
    un=a//10%10
    yuz=a//100%10
    print(bir+un+yuz)
xona_yig(n)
## 3-usul
def xona_yig(a):
    bir= a%10
    un=a//10%10
    yuz=a//100%10
    print(bir+un+yuz)
xona_yig(n)