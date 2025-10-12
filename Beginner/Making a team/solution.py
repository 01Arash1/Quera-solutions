a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
c1 = int(input())
c2 = int(input())

res = 0

while a1 > 0 and a2 > 0:
    a1 -= 1
    a2 -= 1
    res += 1

while b1 > 0 and b2 > 0:
    b1 -= 1
    b2 -= 1
    res += 1

while c1 > 0 and c2 > 0:
    c1 -= 1
    c2 -= 1
    res += 1

print(res)