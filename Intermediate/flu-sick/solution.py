def how_many(string):
    res = 0
    res += string.count("MOLANA")
    res += string.count("HAFEZ")
    return res

my_list = []
my_list.append(input())
my_list.append(input())
my_list.append(input())
my_list.append(input())
my_list.append(input())

for i in range(5):
    if (0 < how_many(my_list[i])):
        print(i + 1, end=" ")
