n = input()
my_list = n.split(" ")

king = 1 - int(my_list[0])
minister = 1 - int(my_list[1])
castles = 2 - int(my_list[2])
elephants = 2 - int(my_list[3])
horses = 2 - int(my_list[4])
soldiers = 8 - int(my_list[5])

print(king ,minister ,castles ,elephants ,horses ,soldiers )