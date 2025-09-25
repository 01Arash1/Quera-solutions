a = input()
b = input()

a_new = int(a[::-1])
b_new = int(b[::-1])

if a_new < b_new: 
    print(f"{a} < {b}")
elif a_new > b_new: 
    print(f"{b} < {a}")
else:
    print(f"{a} = {b}")