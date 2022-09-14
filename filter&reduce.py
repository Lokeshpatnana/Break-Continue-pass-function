a=[1,2,3,4,5,6,7,8,9,10]
def gr(n):
    return n>5
def ls(n):
    return n<5
b=list(filter(gr,a))
c=list(filter(ls,a))
print(b)
print(c)

from functools import reduce
s=[5,10,15,20,25]
r=reduce(lambda x, y:x+y, s)
print(r)