n, k= list((map(int, input().split())))
my_list = list((map(int, input().split())))
sums = sum(my_list)

if sums < n * k:
    if sums // k == sums / k:
        res = n - sums//k
    else:
        res = n - (sums // k + 1)
elif sums == n * k:
    res = 0


print(res)