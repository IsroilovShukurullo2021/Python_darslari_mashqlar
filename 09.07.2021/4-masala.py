# Berilgan sonni avval modulini topib keyin 2 ga ortiradigan funksiyani toping
def modul(n):
    if n>=0:
        return n
    else:
        return -n
def ikkilantirish(n):
    return 2*n
def masala(n):
    m=modul(n)
    return ikkilantirish(n)
print(masala(-5))