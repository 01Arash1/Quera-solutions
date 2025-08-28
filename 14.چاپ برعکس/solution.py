my_list = []
i = 0

while True: 
    a = int(input())
    if a == 0:
        break
    my_list.append(a)
    i += 1

my_list.reverse()

for j in range(i):
    print(my_list[j])