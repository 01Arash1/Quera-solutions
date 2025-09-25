def how_many_star(y , row):
    res = 0
    for i in range(y):
        if "*" == row[i]:
            res += 1
    return res

z = input()
my_list = z.split()
x, y = int(my_list[0]) ,int(my_list[1])
res = 0

for i in range(x):
    row = input()
    res += how_many_star(y ,row)

print(res)