def is_prime_number(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

a = int(input())
b = int(input())
prime_nums = []

for i in range(a+1, b):
    if is_prime_number(i):
        prime_nums.append(i)

print(*prime_nums, sep=",")