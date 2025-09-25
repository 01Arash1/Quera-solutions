n = input()
my_list = n.split(" ")
a = int(my_list[0])
b = int(my_list[1])
i = int(my_list[2])
s = 0

for j in range(i):
    if j % 2 == 0:
        s = s + a
    else:
        s = s + b

print(s)