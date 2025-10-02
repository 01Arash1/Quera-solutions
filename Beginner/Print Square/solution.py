n = int(input())

print(n*"*")
print((f"*{" "*(n-2)}*\n")*(n-2), end="" )
print(n*"*")