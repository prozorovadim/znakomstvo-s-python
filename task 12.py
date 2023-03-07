S = int(input())
P = int(input())
for X in range(1000):
    for Y in range(1000):
        if S == X + Y and P == X * Y:
            print(X, Y)