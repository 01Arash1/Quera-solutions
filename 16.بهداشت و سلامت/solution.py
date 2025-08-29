x = int(input())
n = int(input())

if n == 0: 
    x = 20
elif n == 7:
    pass
else:
    x = x - n
    if x <= 0:
        x = 0

print(x)