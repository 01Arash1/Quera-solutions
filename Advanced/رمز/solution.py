n = int(input())
digit = input()
res = 0 

for i in range(n):
    revolver = input()
    count = 0
    for j in range(9):
        if digit[i] != revolver[j]:
            count += 1
        else:
            break
    if count >= 5:
        res = res + (9 - count)
    else:
        res += count

print(res)