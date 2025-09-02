x = int(input())
text = input()
my_list = text.split()
list_rev = my_list[::-1]

for i in range(x):
    print(list_rev[i] ,end = " ")