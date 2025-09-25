a = int(input())
b = int(input())

start = min(a, b)
end = max(a, b)

for num in range(start, end + 1):
    if num < 2:
        continue
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)