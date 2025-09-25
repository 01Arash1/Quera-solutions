text = input()

for i in range(len(text)):
    print(f"{text[i]*(i+1)}{text[i+1:]}")