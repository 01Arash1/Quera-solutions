a = []
n = input()
my_list = n.split(" ")

for i in range(2):
    a.append(int(my_list[i]))

if a[1]<=10: 
    print("Right",11-a[0],a[1])
else: 
    print("Left",11-a[0],21-a[1])