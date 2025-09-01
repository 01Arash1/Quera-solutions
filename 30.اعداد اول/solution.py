a = int(input())
b = int(input())


while a <= b : 
    for i in range(2 , a +1):
        if a % i == 0:
            print(a)
    a += 1
