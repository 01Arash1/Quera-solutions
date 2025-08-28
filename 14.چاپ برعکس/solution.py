my_list = []

while True: 
    a = int(input())
    if a == 0:
        break
    my_list.append(a)

my_list.reverse()

for x in my_list:
    print(x)