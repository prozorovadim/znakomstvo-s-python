N=int(input())

i=0
while 2**i<N:
    if 2**i%2==0:
        print (2**i)
    i+=1
