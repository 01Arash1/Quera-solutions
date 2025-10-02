n = int(input())
num = input()
my_list = num.split(" ")
a = []

for i in range(n):
    a.append(int(my_list[i]))

print(max(a))