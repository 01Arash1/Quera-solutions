n = int(input())
res = 0 

for i in range(n):
    name = input()
    my_set = set()
    for j in name:
        my_set.add(j)
    if res < len(my_set):
        res = len(my_set)

print(res)