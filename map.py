a=['1','2','3','4','5']
for i in range(len(a)):
    a[i]=int(a[i])
    print(a[i])

b=['10','20','30','40']
c=list(map(int, b))
print(c)
print(*c)

def lr(a):
    return a*a
b=[2,3,4,5,6]
c=list(map(lr, b))
d=list(map(lambda x:x*x, b))
print(c)
print(d)

def square(s):return s*s
def cube(c):return c*c*c
a=[square,cube]
for i in range(1,6):
    b=list(map(lambda x:x(i), a))
    print(b)
    print(*b)
