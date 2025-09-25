n = int(input())
fib_n_1 = 0
fib_final = 1

for i in range(1 ,n+1 ):
    if i == fib_n_1 + fib_final:
        print("+" ,end="")
        fib_n_1 ,fib_final = fib_final ,fib_n_1 + fib_final
    else:
        print("-" ,end="")