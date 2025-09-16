def amaliat(x ,y ,z, k):
    my_list = []
    sums = x + y + z + k
    average = sums / 4
    product = x * y * z * k
    my_list.append(x)
    my_list.append(y)
    my_list.append(z)
    my_list.append(k)
    my_list.sort()
    return sums , average , product , my_list[3] , my_list[0]


a = int(input())
b = int(input())
c = int(input())
d = int(input())

res = amaliat(a, b, c, d)
print(f"Sum : {res[0]:1.6f}\nAverage : {res[1]:1.6f}\nProduct : {res[2]:1.6f}\nMAX : {res[3]:1.6f}\nMIN : {res[4]:1.6f}")