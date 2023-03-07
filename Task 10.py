import random as rd
n=int(input())
lst=[]
for i in range(n):
    x = rd.randint(0,1)
    lst.append(x)
c1=0
c2=0
for i in range(n):
    if lst[i] == 0:
        c1+=1
    else:
        c2+=1
if c1<=c2:
    print(c1)
else:
    print(c2)
print(lst)
