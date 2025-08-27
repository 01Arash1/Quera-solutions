x ,y ,z = int(input()), int(input()), int(input())

if x>y and x>z :
    if x**2 == y**2 + z**2 :
        print("YES")
    else :
        print("NO")

elif y>x and y>z :
    if y**2 == x**2 + z**2 :
        print("YES")
    else :
        print("NO")

elif z>x and z>y :
    if z**2 == x**2 + y**2 :
        print("YES")
    else :
        print("NO")

else:
    print("NO")