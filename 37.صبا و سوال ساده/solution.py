def taghsim(a, b):
    res = a
    for i in range(b):
        res = res // 2
    return res

nums = input()
num = nums.split(" ")

print(taghsim(int(num[0]), int(num[1])))