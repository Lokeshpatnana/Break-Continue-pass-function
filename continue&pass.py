n=0
while n<10:
    n+=1
    if n==9:
        continue
    print(n)

"""2nd type"""
n=0
while n<10:
    n+=1
    if n<5:
        continue
    print(n)

"""3rd type"""
n=0
while n<10:
    n+=1
    if n>5:
        continue
    print(n)

"""4th type"""
n=0
while n<10:
    n+=1
    if n<=5:
        continue
    print(n)

"""pass loop"""
if (10>5):
    pass
else:
    print("Lokesh")


if (10<5):
    pass
else:
    print("Lokesh")