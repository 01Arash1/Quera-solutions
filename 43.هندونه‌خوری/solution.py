n = int(input())
weights = list(map(int, input().split()))

for i in range(len(weights)):
    if weights[i] == max(weights):
        print(i+1)
        break