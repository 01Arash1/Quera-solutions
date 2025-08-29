a = input()
my_list = a.split(" ")

if my_list[0] == my_list[2]:
    print("Vertical")
elif my_list[1] == my_list[3]:
    print("Horizontal")
else:
    print("Try again")