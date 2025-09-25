n = int(input())
str1 = input()
str2 = input()
j = 0

for i in range(n):
    if str1[i] != str2[i]:
        j = j + 1

print(j)