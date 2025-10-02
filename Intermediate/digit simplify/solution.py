n = int(input())
x = 0

while n >= 10: 
    x = 0
    while n >=10 :
        x = x + n%10
        n = n//10
    if n<10 :
        x = x + n
    n = x

print(n)